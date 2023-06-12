from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('allauth.urls')),  # django-allauth
    path('accounts/', include('accounts.urls')),  # cccounts App
    path('get-regions/', views.get_regions, name='get_regions'),
    path('get-cities/', views.get_cities, name='get_cities'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
