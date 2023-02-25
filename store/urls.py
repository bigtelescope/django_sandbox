
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import store.settings as settings

from landing.views import main_landing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('records', main_landing)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
