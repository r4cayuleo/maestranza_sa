from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('inventory/', include('inventory.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Redirigir la raíz a la vista de login
urlpatterns += [
    path('', include('django.contrib.auth.urls')),  # Para manejar la autenticación
    path('', include('inventory.urls')),  # Incluir URLs del app inventory
]
