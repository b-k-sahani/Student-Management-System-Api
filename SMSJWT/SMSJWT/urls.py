#
# from django.contrib import admin
# from APP import views
# from django.urls import path,include
# #ROUTER
# from rest_framework import routers
# router=routers.DefaultRouter()
# router.register('api',views.RegisterAPI,basename='register')
# #TOKEN
# from rest_framework.authtoken import views
# from rest_framework_jwt import views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',include(router.urls)),
#     #TOKEN AUTHENTICATION
#     # path('get-api-token/',views.obtain_auth_token),
#     #JWT
#     path('auth-jwt/',views.obtain_jwt_token),
#     path('auth-jwt-refresh/',views.refresh_jwt_token),
#     path('auth-jwt-verify/',views.verify_jwt_token),
# ]
from django.urls import path, include

urlpatterns = [
    path('api/', include('APP.API1.urls')),
    path('api/', include('APP.API2.urls')),
]