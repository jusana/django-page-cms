from django.urls import path
from pages.testproj.documents.views import document_view

urlpatterns = [
    path('doc-<int:document_id>', document_view, name='document_details'),
    path('', document_view, name='document_root'),
]
