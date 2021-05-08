from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.sign_up, name='sign_up'),
]
