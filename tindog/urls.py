from django.contrib import admin
from django.urls import path, include

# Important: para que se puedan ver las imagenes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('dogs.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
