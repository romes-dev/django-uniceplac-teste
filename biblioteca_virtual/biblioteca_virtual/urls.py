from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('livros.urls')),  # Inclui as URLs do app 'livros'
    path('accounts/', include('django.contrib.auth.urls')),  # Inclui todas as URLs de autenticação padrão
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
