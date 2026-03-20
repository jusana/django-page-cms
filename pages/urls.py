"""Django page CMS urls module."""

from django.urls import path
from django.urls import re_path
from pages import views
from pages import settings

urlpatterns = []

if settings.PAGE_API_ENABLED:
    try:
        from pages import api
    except ImportError as detail:
        print("API not present because of import error: %s" % detail)
    else:
        urlpatterns += [
            path('api/', api.PageList.as_view()),
            path('api/pages/', api.PageList.as_view()),
            path('api/pages/<int:pk>/', api.PageEdit.as_view()),
            path('api/contents/', api.ContentList.as_view()),
            path('api/contents/<int:pk>/', api.ContentEdit.as_view())
        ]

if settings.PAGE_USE_LANGUAGE_PREFIX:
    urlpatterns += [
        re_path(r'^(?P<lang>[-\w]+)/(?P<path>.*)$', views.details,
            name='pages-details-by-path'),
        path('', views.details, {'path': '', 'name': 'pages-root'}),
    ]
else:
    urlpatterns += [
        re_path(r'^(?P<path>.*)$', views.details, name='pages-details-by-path'),
        path('', views.details, {'path': '', 'name': 'pages-root'}),
    ]
