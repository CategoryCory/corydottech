import environ
import os
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
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'tailwind',
    'taggit',
    'tinymce',

    # Local
    'theme.apps.ThemeConfig',
    'custom_user.apps.CustomUserConfig',
    'jobs.apps.JobsConfig',
    'projects.apps.ProjectsConfig',
    'home_sensors.apps.HomeSensorsConfig',
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
    'home_sensors': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('HS_DB_NAME'),
        'USER': env('HS_DB_USER'),
        'PASSWORD': env('HS_DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

DATABASE_ROUTERS = ('home_sensors.router.HomeSensorsRouter', )

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
