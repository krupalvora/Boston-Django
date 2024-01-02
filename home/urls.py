from django.contrib import admin
from django.urls import path
from home import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from .views import UserLoginView, CustomObtainAuthToken
urlpatterns=[
    path("",views.index,name='home'),
    path("get_books",views.get_books,name='get_books'),
    path("get_book/<book>/",views.get_book,name='get_book'),
    path("rotate_video/<angle>/",views.rotate_video,name='rotate_video'),
    path("add_book",csrf_exempt(views.add_book)),
    path('api/token/', CustomObtainAuthToken.as_view(), name='get_token'),
    path('api/login/', UserLoginView.as_view(), name='user_login'),
]
