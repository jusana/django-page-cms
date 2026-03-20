
from django.urls import re_path, include, path
from django.contrib import admin
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from pages.views import PageSitemap, MultiLanguagePageSitemap


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

    path('pages/', include('pages.urls')),

    # this is only used to enable the reverse url to work with documents
    re_path(r'^pages/(?P<path>.*)', include('pages.testproj.documents.urls')),

    path('admin/', admin.site.urls),
    # make tests fail if a backend is not present on the system
    #(r'^search/', include('haystack.urls')),

    path('sitemap.xml', sitemap,
        {'sitemaps': {'pages':PageSitemap}}),

    path('sitemap2.xml', sitemap,
        {'sitemaps': {'pages':MultiLanguagePageSitemap}})
]
