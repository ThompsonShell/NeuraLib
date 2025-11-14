MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



# self.queryset.filter(authot=requsest.user)
# if request.method = = 'POST':
#     return serializer


# filter queryset

# django-filter package 
# filter backends

# RESTfrm
# search filter
#ordering filter



#get_serializer_Class

# get_serileralizer_context
# return {'request': self.request, 'view': self.view, 'format': self.format_kwarg}


#filterset_fields = ['author', 'category']

