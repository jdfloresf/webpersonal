from .base import *
import os

from dotenv import load_dotenv

load_dotenv()


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

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

# Configurar Cloudinary

# CLOUD_NAME = os.getenv('CLOUD_NAME')
# API_KEY = os.getenv('API_KEY')
# API_SECRET = os.getenv('API_SECRET')

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': 'CLOUD_NAME',
#     'API_KEY': 'API_KEY',
#     'API_SECRET': 'API_SECRET',
# }

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

STATIC_URL = 'static/'

#Media file

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"