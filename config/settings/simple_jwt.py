from datetime import timedelta


SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
        'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
        'ROTATE_REFRESH_TOKENS': True, # Optional: For refreshing tokens
        'BLACKLIST_AFTER_ROTATION': True, # Optional: Requires 'token_blacklist' app
    }