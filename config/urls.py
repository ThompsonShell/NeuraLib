from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="NeuraLib",
        default_version='v1',
        description="AI-Driven Reading Platform",
        terms_of_service="https://github.com/ThompsonShell/NeuraLib/",
        contact=openapi.Contact(email="asilbek.rajabov.official@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # SWAGGER
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    path('admin/', admin.site.urls),


    # BOOK URLS
    path('api/v1/books/', include('apps.books.urls')),


    # ORDER URLS
    path('api/v1/books/', include('apps.orders.urls')),


    # USER URLS
    path('api/v1/books/', include('apps.users.urls')),


    # GENERAL URLS
    path('api/v1/books/', include('apps.general.urls')),


    # ARTICLE URLS
    path('api/v1/books/', include('apps.articles.urls')),


    # ARTICLE URLS
    path('api/v1/auth/', include('apps.authentication.urls')),
    
    
    # RESTFRAMEWORK
    path('api-auth/', include('rest_framework.urls'))
    
    # #JWT
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]       
