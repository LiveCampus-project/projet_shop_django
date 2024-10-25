from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import signup, user_detail

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('signup/', views.signup, name='signup'),

     path('<int:user_id>/', user_detail, name='user_detail'),
]