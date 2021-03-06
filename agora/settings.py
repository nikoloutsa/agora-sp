"""
Django settings for agora project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from os import path


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DIR_RESOURCES = 'resources'
PATH_RESOURCES = os.path.join(BASE_DIR, DIR_RESOURCES)

FILE_SPEC = 'agora.spec'
FILEPATH_SPEC = os.path.join(PATH_RESOURCES, FILE_SPEC)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret-key'

# SECURITY WARNING don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',
		 'sp.eudat.eu'
		]

DEFAULT_FROM_EMAIL = 'no-reply@agora.com'

USER_CREATION_EMAIL_LIST = [
    'iliaboti@grnet.gr',
    'strezoski.g@gmail.com',
    'stojanovski.dario@gmail.com',
]

CORS_ORIGIN_ALLOW_ALL = True

CORS_EXPOSE_HEADERS = [
    'authorization',
]

# Application definition

INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'rest_framework',
    'djoser',
    'corsheaders',
    'reversion',
    'component',
    'options',
    'owner',
    'common',
    'service',
    'accounts',
    'ckeditor',
    'ckeditor_uploader',
]


def generate_service_menu():
    import service
    import inspect

    MEMBER_NAME = 0
    MEMBER_MODULE = 1

    def is_service_model(member):
        return member[MEMBER_MODULE].__module__ == 'service.models'

    def is_not_blacklisted(member):
        blacklist = [
            'ServiceStatus',
            'ServiceTrl',
        ]
        return member[MEMBER_NAME] not in blacklist

    def to_menu_structure(member):
        return {
            'url': '/api/adminservice/' + member[MEMBER_NAME].lower(),
        }

    members_all = inspect.getmembers(
        getattr(service, 'models'),
        inspect.isclass)
    members_valid = []
    for m in members_all:
        if is_service_model(m) and is_not_blacklisted(m):
            members_valid.append(to_menu_structure(m))

    return tuple(members_valid)


SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Agora Write Beta 1.0',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,

    # menu
    'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
        'service': 'icon-leaf',
        'component': 'icon-leaf',
        'owner': 'icon-leaf',
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
    },
    'MENU_OPEN_FIRST_CHILD': True,
    'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        'service',
        'component',
        'owner',
        'options',
        'sites',
    ),
    'LIST_PER_PAGE': 15
}

AUTH_USER_MODEL = "accounts.User"

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = "/api/admin/"

PROJECT_APPS = ['component', 'options', 'owner', 'service']

SITE_ID = 2
ALLOWED_HOST = 'sp.eudat.eu';

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ),
    'EXCEPTION_HANDLER': 'agora.views.custom_exception_handler'
}

ROOT_URLCONF = 'agora.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'agora.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/srv/db.agora.sqlite3'
    }
}

DATABASES = SQLITE

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',)

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CLIENT_ID = ''
APPLICATION_NAME = 'API-Client'



SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',  # <--- enable this one
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    # 'accounts.views.save_avatar'
)


MEDIA_ROOT = '/var/www/agora/media'
MEDIA_URL = 'media/'
AVATAR_LOCATION = MEDIA_ROOT + '/avatar'

# Default name for service area logo. Should exist in MEDIA_ROOT
SERVICE_AREA_ICON = 'service-area-icon-default.jpg'
# Default name for service logo. Should exist in MEDIA_ROOT
SERVICE_LOGO = 'service-logo-default.jpg';

CKEDITOR_UPLOAD_PATH = "uploads/"

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/API-Client

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "assets/")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


SWAGGER_SETTINGS = {
    'exclude_namespaces': [],
    'api_version': '1.0',
    'api_path': str(ALLOWED_HOST) + '/api',
    'enabled_methods': [
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    'host': 'str(ALLOWED_HOST)',
    'info': {
        'contact': 'admin@agora.com',
        'description': (
            'This is a demonstration of the API documentation engine. '
            'The full Git repository is availible at '
            '<a href="https://code.vi-seem.eu/stdario/agora">Agora Git</a> '
            'where the current development version is availible '
            ' in the DEV branch. '
            'The current stable version is availible at the MASTER branch.'
        ),
        'license': 'Apache 2.0',
        'licenseUrl': 'http://www.apache.org/licenses/LICENSE-2.0.html',
        'termsOfServiceUrl': '/',
        'title': 'Agora API v1.0',
    },
    'api_key': '',
    'is_authenticated': False,
    'is_superuser': False,
    'permission_denied_handler': None,
    'resource_access_handler': None,
    'base_path': '{}/api/docs'.format(ALLOWED_HOST),
    'doc_expansion': 'list',
    'operationsSorter': 'method'
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
        },

    },
    'loggers': {
        'agora': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True,
        },
    },
}

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'width': '100%',
        'toolbar_Custom': [
            {
                'name': 'basic styles',
                'items': [
                    'Bold',
                    'Italic',
                    'Underline',
                    'Strike',
                    'RemoveFormat',
                ]
            },
            {
                'name': 'font',
                'items': [
                    'Font',
                    'FontSize',
                    'Format',
                    'TextColor',
                    'BGColor',
                ]
            },
            {
                'name': 'general',
                'items': [
                    'Image',
                    'ImageButton',
                    'Table',
                    'Undo',
                    'Redo',
                    'Cut',
                    'Copy',
                    'Paste',
                    'PasteText',
                    'PasteFromWord',
                    'Anchor',
                ]
            },
            {
                'name': 'paragraph',
                'items': [
                    'NumberedList',
                    'BulletedList',
                    '-',
                    'Outdent',
                    'Indent',
                    '-',
                    'JustifyLeft',
                    'JustifyCenter',
                    'JustifyRight',
                    'JustifyBlock',
                ]
            },
            {
                'name': 'link',
                'items': [
                    'Link',
                    'Unlink',
                ]
            },
            {
                'name': 'rest',
                'items': [
                    'Source',
                ]
            }
        ]
    }
}

AAI_ID_KEY = 'edupersonuniqueid'
TOKEN_LOGIN_URL = '/auth/login'

SETTINGS_DIR = os.environ.get('AGORA_SETTINGS_DIR', '/etc/agora')
SETTINGS_FILE = 'settings.conf'
SETTINGS_PATH = os.path.join(SETTINGS_DIR, SETTINGS_FILE)

if not os.path.isfile(SETTINGS_PATH):
    m = "Cannot find settings file {0!r}. Consider using AGORA_SETTINGS_DIR "
    m += "environment variable to set a custom path for settings.conf file."
    m = m.format(SETTINGS_PATH)
    raise RuntimeError(m)

execfile(SETTINGS_PATH)
