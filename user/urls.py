from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('my_account/', views.my_account, name='my_account'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='account/password_change.html', success_url=reverse_lazy('my_account')), name='password_change'),
]