from django.conf import settings
from django.contrib import admin
from django.utils.html import mark_safe
from django.db import transaction
from django import forms
from helpers import helper
from findjob_api.admin import custom_admin_site
from .models import (
    User,
    ForgotPasswordToken
)
from common.models import File
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter
)
from console.jobs import queue_mail
from configs import variable_system as var_sys
from helpers.cloudinary_service import CloudinaryService

class UserForm(forms.ModelForm):
    avatar_file = forms.FileField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    password_edit = forms.CharField(widget=forms.PasswordInput, required=False)
    
    class Meta:
        model = User
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["avatar_file"].required = False
        instance = kwargs.get("instance")
        if instance and instance.pk:
            self.fields["password"].widget = forms.HiddenInput()
        else:
            self.fields["password_edit"].widget = forms.HiddenInput()
            
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "show_avatar", "email", "full_name", "is_verify_email", "is_active", "role_name")
    list_display_links = ("id", "show_avatar", "email")
    search_fields = ("full_name", "email")
    list_filter = [
        ("role_name", DropdownFilter),
        ("is_verify_email", DropdownFilter),
        ("is_active", DropdownFilter),
        ("email_notification_active", DropdownFilter),
        ("sms_notification_active", DropdownFilter),
        ("has_company", DropdownFilter),
    ]
    ordering = ("id", "email", "full_name", "is_verify_email", "is_active", "role_name")
    readonly_fields = ("show_avatar",)
    list_per_page = 25
    
    fieldsets = (
        (None, {
            'fields': ('show_avatar', 'avatar_file', 'full_name', 'email')
        }),
        ('Permission', {
            'fields': ('password', 'password_edit', 'role_name', 'user_permissions',
                       'groups', 'is_superuser', 'is_staff')
        }),
        ('Action', {
            'fields': (
                'is_active', 'is_verify_email', 'has_company',
                'email_notification_active', 'sms_notification_active')
        }),
        ('Logs', {
            'fields': ('last_login',)
        }),
    )

    def show_avatar(self, user):
        if user:
            avatar_url = var_sys.AVATAR_DEFAULT["AVATAR"]
            if user.avatar:
                avatar_url = user.avatar.get_full_url()
            return mark_safe(
                r"""<img src='{0}'
                    alt='{1}' style="border-radius: 50px;" width='50px' height='50px'/>"""
                    .format(avatar_url,user.full_name))

    show_avatar.short_description = "Avatar"
    
    form = UserForm
    
    def save_model(self, request, user, form, change):
        old_user = None
        if not change:
            user.set_password(user.password)
        else:
            password_edit = form.data.get("password_edit", None)
            if password_edit:
                user.set_password(password_edit)

            old_user = User.objects.filter(id=user.id).first()

        # save
        super().save_model(request, user, form, change)
        if 'avatar_file' in request.FILES:
            file = request.FILES['avatar_file']
            try:
                # Start transaction
                with transaction.atomic():
                    public_id = None
                    # Overwrite if image already exists
                    if user.avatar:
                        path_list = user.avatar.public_id.split('/')
                        public_id = path_list[-1] if path_list else None
                    # Upload to cloudinary
                    avatar_upload_result = CloudinaryService.upload_image(
                        file,
                        settings.CLOUDINARY_DIRECTORY["avatar"],
                        public_id=public_id
                    )
                    # Update or create file
                    user.avatar = File.update_or_create_file_with_cloudinary(
                        user.avatar,
                        avatar_upload_result,
                        File.AVATAR_TYPE
                    )
                    user.save()
            except Exception as ex:
                helper.print_log_error("user_save_model", ex)

        if change:
            new_is_active = user.is_active
            if old_user and old_user.is_active and not new_is_active:
                # Send an account deactivation email
                queue_mail.send_an_account_deactivation_email.delay(
                    to=[user.email],
                    full_name=user.full_name, email=user.email)

class ForgotPasswordTokeAdmin(admin.ModelAdmin):
    list_display = ("id", "token", "code", "expired_at", "is_active", "platform", "user")
    list_display_links = ("id", "token", "code")
    search_fields = ("token", "code", "user__email")
    list_filter = [
        ("platform", DropdownFilter),
        ("is_active", DropdownFilter),
    ]
    ordering = ("id", "token", "code", "expired_at", "is_active", "platform")
    readonly_fields = ("token", "code", "expired_at", "is_active", "platform", "user")
    list_per_page = 25

    autocomplete_fields = ('user',)

custom_admin_site.register(User, UserAdmin)
custom_admin_site.register(ForgotPasswordToken, ForgotPasswordTokeAdmin)