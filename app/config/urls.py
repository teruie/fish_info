from django.contrib import admin
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fish.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('social_django.urls', namespace='social')),
]

urlpatterns += static(
  settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)