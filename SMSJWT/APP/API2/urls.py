from django.urls import path
from APP.API2.views import AdminProfileView


urlpatterns = [
    path('sAdmin/', AdminProfileView.as_view()),
    ]