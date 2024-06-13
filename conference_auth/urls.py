from django.urls import path
from . import views
# import logout view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='users-register'),
    path('login', views.LoginUserView.as_view(), name='users-login'),
    path('logout', LogoutView.as_view(), name='users-logout'),
]
