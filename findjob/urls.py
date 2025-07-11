from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

app_router = DefaultRouter()

web_router = DefaultRouter()
web_router.register(r'feedbacks', views.FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('', include([
        path('send-noti-demo/', views.send_notification_demo),
    ])),
    path('web/', include([
        path("", include(web_router.urls)),
        path("sms-download-app/", views.send_sms_download_app),
        path('banner/', views.get_web_banner)
    ]))
]
