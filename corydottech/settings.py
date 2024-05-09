import environ
import os
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from pathlib import Path
from shutil import which

env = environ.Env(
    DEBUG=(bool, False),
)

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(env_file=BASE_DIR / '.env')

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(' ')

INSTALLED_APPS = [
    # Core
    'unfold',
    'unfold.contrib.filters',
    'unfold.contrib.forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'ninja',
    'tailwind',
    'taggit',
    'tinymce',
    'django_recaptcha',

    # Local
    'theme.apps.ThemeConfig',
    'custom_user.apps.CustomUserConfig',
    'auth_keys.apps.AuthKeysConfig',
    'jobs.apps.JobsConfig',
    'projects.apps.ProjectsConfig',
    'contacts.apps.ContactsConfig',
    'sensors.apps.SensorsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG is True:
    INSTALLED_APPS += ['django_browser_reload', ]
    MIDDLEWARE += ['django_browser_reload.middleware.BrowserReloadMiddleware', ]

ROOT_URLCONF = 'corydottech.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'corydottech.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    },
}

# Password validation
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


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    BASE_DIR / 'staticfiles',
]

# Media files
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication and authorization
AUTH_USER_MODEL = 'custom_user.CustomUser'

# CSRF settings
CSRF_TRUSTED_ORIGINS = env('CSRF_TRUSTED_ORIGINS').split(' ')

# Tailwind
TAILWIND_APP_NAME = 'theme'
NPM_BIN_PATH = which('npm')
INTERNAL_IPS = ['127.0.0.1', ]

# Taggit
TAGGIT_CASE_INSENSITIVE = True

# TinyMCE Configuration
TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    "height": "450px",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
    "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline | fontsizeselect formatselect | alignleft "
    "aligncenter alignright alignjustify | outdent indent | numlist bullist | forecolor "
    "backcolor | link anchor codesample | "
    "a11ycheck ltr rtl | showcomments addcomment code",
}

# Encryption key
ENCRYPTION_KEY = env('ENCRYPTION_KEY')

# Unfold options
UNFOLD = {
    'SITE_TITLE': 'cory{dot}tech',
    'SITE_HEADER': 'cory{dot}tech',
    'SIDEBAR': {
        'show_search': True,
        'show_all_applications': False,
        'navigation': [
            {

                'title': _('Navigation'),
                'separator': True,
                'items': [
                    {
                        'title': _('Users'),
                        'icon': 'person',
                        'link': reverse_lazy('admin:custom_user_customuser_changelist'),
                    },
                    {
                        'title': _('Groups'),
                        'icon': 'groups',
                        'link': reverse_lazy('admin:auth_group_changelist'),
                    },
                    {
                        'title': _('API Auth Keys'),
                        'icon': 'key',
                        'link': reverse_lazy('admin:auth_keys_authkey_changelist'),
                    },
                    {
                        'title': _('Contacts'),
                        'icon': 'feed',
                        'link': reverse_lazy('admin:contacts_contact_changelist'),
                    },
                    {
                        'title': _('Jobs'),
                        'icon': 'work',
                        'link': reverse_lazy('admin:jobs_job_changelist'),
                    },
                    {
                        'title': _('Projects'),
                        'icon': 'cognition',
                        'link': reverse_lazy('admin:projects_project_changelist'),
                    },
                    {
                        'title': _('Temp/Humidity Readings'),
                        'icon': 'sensors',
                        'link': reverse_lazy('admin:sensors_temphumiditysensor_changelist'),
                    },
                    {
                        'title': _('Tags'),
                        'icon': 'style',
                        'link': reverse_lazy('admin:taggit_tag_changelist'),
                    },
                ],
            },
        ],
    },
}

# ReCAPTCHA settings
RECAPTCHA_PUBLIC_KEY = env('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = env('RECAPTCHA_PRIVATE_KEY')
RECAPTCHA_REQUIRED_SCORE = 0.5

# Email settings
if DEBUG is True:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
ADMIN_EMAIL = env('ADMIN_EMAIL')
SENDGRID_API_KEY = env('SENDGRID_API_KEY')

# Logging settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'corydottech.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        }
    }
}
