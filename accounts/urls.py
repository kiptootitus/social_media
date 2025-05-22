from django.urls import path

from accounts.views import home_api

urlpatterns = [
  path('', home_api, name='home')
]