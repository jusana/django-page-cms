from django.urls import path
from pages.plugins.jsonexport.actions import import_pages_from_json

urlpatterns = [
    path('import-json/', import_pages_from_json,
        name='import-pages-from-json'),
]
