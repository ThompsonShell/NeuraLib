from django.conf import settings

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
}

if settings.DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = list(REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'])

    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = list(REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'])
    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] += [
        'rest_framework.authentication.BasicAuthentication',
    ]