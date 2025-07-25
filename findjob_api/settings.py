"""
Django settings for findjob_api project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import json
import os
import firebase_admin
import cloudinary
from pathlib import Path
from decouple import config
from firebase_admin import credentials
from datetime import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# COMMON SETTING
APP_ENVIRONMENT = config('APP_ENV')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
BASE_URL = 'http://localhost:8000'

COMPANY_NAME = 'FindJob'

AUTH_USER_MODEL = 'authentication.User'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'configs.paginations.CustomPagination',
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'drf_social_oauth2.authentication.SocialAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

REDIRECT_LOGIN_CLIENT = {
    "JOB_SEEKER": "dang-nhap",
    "EMPLOYER": "dang-nhap"
}

# Web client URL
WEB_JOB_SEEKER_CLIENT_URL = config("WEB_JOB_SEEKER_CLIENT_URL")
WEB_EMPLOYER_CLIENT_URL = config("WEB_EMPLOYER_CLIENT_URL")

DOMAIN_CLIENT = {
    "job_seeker": WEB_JOB_SEEKER_CLIENT_URL if WEB_JOB_SEEKER_CLIENT_URL else "http://127.0.0.1:4200/",
    "employer": WEB_EMPLOYER_CLIENT_URL if WEB_EMPLOYER_CLIENT_URL else "http://localhost:4200/",
    "development": WEB_EMPLOYER_CLIENT_URL if WEB_EMPLOYER_CLIENT_URL else "http://localhost:4200/",
}

# FACEBOOK CONFIGURATION
# SOCIAL_AUTH_FACEBOOK_DIALOG_URL = 'https://www.facebook.com/v15.0/dialog/oauth/'
# SOCIAL_AUTH_FACEBOOK_OAUTH2_REVOKE_TOKEN_URL = 'https://graph.facebook.com/v15.0/me/permissions'
SOCIAL_AUTH_FACEBOOK_KEY = config('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = config('SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email,first_name,last_name'
}

# GOOGLE
# Google configuration
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
# Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]

AUTHENTICATION_BACKENDS = (
    # Facebook OAuth2
    'social_core.backends.facebook.FacebookOAuth2',
    # Django
    'django.contrib.auth.backends.ModelBackend',
    # Google OAuth2
    'social_core.backends.google.GoogleOAuth2',
    # drf_social_oauth2
    'drf_social_oauth2.backends.DjangoOAuth2',
)

# EMAIL
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# REDIS
SERVICE_REDIS_HOST = config('SERVICE_REDIS_HOST')
SERVICE_REDIS_PORT = config('SERVICE_REDIS_PORT', cast=int)
SERVICE_REDIS_USERNAME = config('SERVICE_REDIS_USERNAME')
SERVICE_REDIS_PASSWORD = config('SERVICE_REDIS_PASSWORD')
SERVICE_REDIS_DB = config('SERVICE_REDIS_DB', cast=int)

# CELERY
CELERY_BROKER_URL = f"redis://{SERVICE_REDIS_USERNAME}:{SERVICE_REDIS_PASSWORD}@{SERVICE_REDIS_HOST}:{SERVICE_REDIS_PORT}/{SERVICE_REDIS_DB}"
CELERY_RESULT_BACKEND = f"redis://{SERVICE_REDIS_USERNAME}:{SERVICE_REDIS_PASSWORD}@{SERVICE_REDIS_HOST}:{SERVICE_REDIS_PORT}/{SERVICE_REDIS_DB}"
# CELERY_BROKER_URL = f"redis://:@findjob-redis:{SERVICE_REDIS_PORT}/{SERVICE_REDIS_DB}"
# CELERY_RESULT_BACKEND = f"redis://:@findjob-redis:{SERVICE_REDIS_PORT}/{SERVICE_REDIS_DB}"
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = 'Asia/Ho_Chi_Minh'
DJANGO_CELERY_BEAT_TZ_AWARE = True

# Cấu hình CORS
# CORS_ALLOWED_ORIGINS = [
#     "http://127.0.0.1:4200",
#     "http://localhost:4200",
# ]

# Nếu bạn muốn cho phép tất cả origins (chỉ dùng trong phát triển)
CORS_ALLOW_ALL_ORIGINS = True

# Cho phép các tiêu đề tùy chỉnh như Authorization
CORS_ALLOW_HEADERS = [
    'accept',
    'authorization',
    'content-type',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# Cho phép các phương thức HTTP
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

MYJOB_AUTH = {
    "VERIFY_EMAIL_LINK_EXPIRE_SECONDS": 7200,
    "RESET_PASSWORD_EXPIRE_SECONDS": 7200,
    "TIME_REQUIRED_FORGOT_PASSWORD": 120
}

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'authentication.pipeline.custom_social_user',
    'authentication.pipeline.custom_create_user',
    'info.pipeline.save_profile',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details'
)

# FIREBASE SETTINGS
FIREBASE_CONFIG = {
    "apiKey": config('FIREBASE_API_KEY', default=''),
    "authDomain": config('FIREBASE_AUTH_DOMAIN', default=''),
    "projectId": config('FIREBASE_PROJECT_ID', default=''),
    "storageBucket": config('FIREBASE_STORAGE_BUCKET', default=''),
    "messagingSenderId": config('FIREBASE_MESSAGING_SENDER_ID', default=''),
    "appId": config('FIREBASE_APP_ID', default=''),
    "databaseURL": config('FIREBASE_DATABASE_URL', default=''),
}

FIREBASE_CREDENTIALS_PATH = config('FIREBASE_CREDENTIALS_PATH', default='')
FIREBASE_DATABASE_URL = config('FIREBASE_DATABASE_URL', default='')

if FIREBASE_CREDENTIALS_PATH and os.path.exists(FIREBASE_CREDENTIALS_PATH):
    with open(FIREBASE_CREDENTIALS_PATH, 'r') as f:
        firebase_config = json.load(f)
    
    cred = credentials.Certificate(firebase_config)

    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred, {
            'databaseURL': FIREBASE_DATABASE_URL
        })
else:
    print("⚠️ Firebase credentials file not found or path is missing.")

CLOUDINARY_CLOUD_NAME = config('CLOUDINARY_CLOUD_NAME')

CLOUDINARY_BUCKET_NAME = 'my-job-bucket'

# Set the Cloudinary configuration
cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=config('CLOUDINARY_API_KEY'),
    api_secret=config('CLOUDINARY_API_SECRET'),
)

CLOUDINARY_PATH = "https://res.cloudinary.com/" + CLOUDINARY_CLOUD_NAME + "/image/upload/v{0}/"

CLOUDINARY_DIRECTORY = {
    "avatar": f"{CLOUDINARY_BUCKET_NAME}/{APP_ENVIRONMENT}/avatar/{datetime.now().year}/{datetime.now().month}/",
    "cv": f"{CLOUDINARY_BUCKET_NAME}/{APP_ENVIRONMENT}/cv/{datetime.now().year}/{datetime.now().month}/",
    "logo": f"{CLOUDINARY_BUCKET_NAME}/{APP_ENVIRONMENT}/logo/{datetime.now().year}/{datetime.now().month}/",
    "cover_image": f"{CLOUDINARY_BUCKET_NAME}/{APP_ENVIRONMENT}/cover-image/{datetime.now().year}/{datetime.now().month}/",
    "company_image": f"{CLOUDINARY_BUCKET_NAME}/{APP_ENVIRONMENT}/company-image/{datetime.now().year}/{datetime.now().month}/",
    "career_image": f"{CLOUDINARY_BUCKET_NAME}/{APP_ENVIRONMENT}/career-images/{datetime.now().year}/{datetime.now().month}/",
    "web_banner": f"{CLOUDINARY_BUCKET_NAME}/{APP_ENVIRONMENT}/banners/web-banners/{datetime.now().year}/{datetime.now().month}/",
    "mobile_banner": f"{CLOUDINARY_BUCKET_NAME}/{APP_ENVIRONMENT}/banners/mobile-banners/{datetime.now().year}/{datetime.now().month}/",
    "system": f"{CLOUDINARY_BUCKET_NAME}/system/",
    "icons": f"{CLOUDINARY_BUCKET_NAME}/icons/",
    "about_us": f"{CLOUDINARY_BUCKET_NAME}/about_us/",
}
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-k!_lx8uk2xb4_5je6-1mc1y7)l9=@15a=fq-az0i24n4vl9nax"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # BASE
    "authentication",
    "common",
    "info",
    "job",
    "findjob",
    'corsheaders',
    
    # ADD
    'cloudinary',
    'ckeditor',
    'django_otp',
    'rest_framework',
    'django_filters',
    'drf_yasg',
    'oauth2_provider',
    'social_django',
    'drf_social_oauth2',
    'celery',
    'django_admin_listfilter_dropdown',
    'django_extensions',
    'django_celery_beat',
    'import_export',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = "findjob_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [BASE_DIR / 'findjob_api/templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "findjob_api.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('POSTGRES_HOST'),
        'PORT': config('POSTGRES_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "findjob_api", "static")]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
