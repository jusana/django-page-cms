# Admin bindings
from django.contrib import admin
from pages.testproj.documents.models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):

    list_display = ('title', 'page',)

