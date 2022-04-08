from .views import registrationView
from django.urls import path


urlpatterns = [
    path('register', registrationView.as_view(), name='register')
]
