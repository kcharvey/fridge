from fridge.settings.base import *

DEBUG = os.environ.get('DJANGO_DEBUG', False)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', None)

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

