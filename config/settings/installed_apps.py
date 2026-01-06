DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'apps.ai_assistant',
    'apps.articles',
    'apps.books',
    'apps.general',
    'apps.orders',
    'apps.users',
    'apps.tests',
    'apps.utils',
    'apps.authentication',

]

THIRD_PARTY = [
    'corsheaders',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    'debug_toolbar'
    # 'rest_framework_simplejwt.token_blacklist',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY

AUTH_USER_MODEL = 'users.CustomUser'



