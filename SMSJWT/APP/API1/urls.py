from django.urls import path
from APP.API1.views import UserRegistrationView
from APP.API1.views import UserLoginView

urlpatterns = [
    path('signup', UserRegistrationView.as_view()),
    path('signin', UserLoginView.as_view()),
    ]