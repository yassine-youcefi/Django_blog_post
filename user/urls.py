from django.urls import path
from django.contrib.auth import views as auth_views

from . import views as user_views

urlpatterns = [
    path('register/', user_views.sign_up, name='sign_up'),
    path('login/', auth_views.LoginView.as_view(template_name='templates/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='templates/logout.html'), name='logout')
]
