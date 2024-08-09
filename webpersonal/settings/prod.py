from .base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost', 'web-production-b610.up.railway.app']

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

#Media file

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"