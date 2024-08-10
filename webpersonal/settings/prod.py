from .base import *
import dj_database_url
from dotenv import load_dotenv 
import os

load_dotenv()

DEBUG = False

ALLOWED_HOSTS = ['localhost', 'web-production-b610.up.railway.app']

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'core/static/core',
]
STATIC_ROOT = BASE_DIR /  'staticfiles'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

CSRF_TRUSTED_ORIGINS = ['http://*', 'https://web-production-b610.up.railway.app/']

#Media file

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"