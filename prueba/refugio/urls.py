"""refugio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth.views import logout_then_login, LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pedidos/', include('apps.pedidos.urls')),
    path('tipo/', include('apps.tipo.urls')),
    path('usuario/', include('apps.usuario.urls')),
    path('logout/', logout_then_login, name='logout'),
    path('accounts/login/', LoginView.as_view(template_name='index.html', success_url=reverse_lazy('tipo_listar')), name='login'),
    path('reset/password_reset', PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
         {'email_template': 'registration/password_reset_email.html'}, name="password_reset"),
    path('reset/password_reset_done',
         PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name="password_reset_confirm"),
    path('reset/done', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name="password_reset_complete"),
]