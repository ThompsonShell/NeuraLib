from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'library',
        'USER': 'acer',
        'PASSWORD': '1',
        'PORT': '5432',
        'HOST': 'localhost'
    }

}
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Optional: Use Redis for sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'
