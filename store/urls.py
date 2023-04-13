
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import store.settings as settings

from landing.views import main_landing, sandbox, show_record

urlpatterns = [
    path('admin/', admin.site.urls),
    path('records', main_landing),
    path('records/<slug:slud_id>', show_record, name='product_link'),
    path('sandbox', sandbox)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
