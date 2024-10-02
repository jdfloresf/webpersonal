from .base import *
from dj_database_url import config
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = True

ALLOWED_HOSTS = ['localhost', 'web-production-b610.up.railway.app', 'jonathan-flores.up.railway.app', 'jdfloresf.asdrome.com/', '127.0.0.1']

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': config(default=os.getenv("DATABASE_PUBLIC_URL"))
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'core/static/core',
]

STATIC_ROOT = BASE_DIR /  'staticfiles'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

CSRF_TRUSTED_ORIGINS = ['http://*', 'https://jonathan-flores.up.railway.app']

# Media file
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Configurar Cloudinary
api_key = os.getenv('api_key')
api_secret = os.getenv('api_secret')
cloud_name = os.getenv('cloud_name')

CLOUDINARY_STORAGE = {
    'api_key': api_key,
    'api_secret': api_secret,
    'cloud_name': cloud_name,
}

# Configurar almacenamiento predeterminado en Cloudinary
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'