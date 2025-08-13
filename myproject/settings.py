from pathlib import Path
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-123'
DEBUG = True
ALLOWED_HOSTS = ['*']

# Языки
LANGUAGE_CODE = 'ru'

LANGUAGES = [
    ('ru', _('Русский')),
    ('kk', _('Қазақша')),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
MODELTRANSLATION_LANGUAGES = ('ru', 'kk')
MODELTRANSLATION_FALLBACK_LANGUAGES = ('ru',)

# Настройки для modeltranslation
TRANSLATABLE_MODEL_MODULES = [
    'myapp.translation',
    'news.translation',
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'

# Приложения
INSTALLED_APPS = [
    'modeltranslation',  # Обязательно ДО admin
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'users',
    'news',
]

# Middleware
MIDDLEWARE = [
#    'myproject.middleware.maintenance.MaintenanceModeMiddleware', 
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'myproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []

TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Статика и медиа - ИСПРАВЛЕНО
STATIC_URL = '/static/'

# Используем существующую папку staticfiles
STATICFILES_DIRS = [
    BASE_DIR / 'staticfiles',
]

# Для продакшена (когда DEBUG=False)
STATIC_ROOT = BASE_DIR / 'collected_static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'