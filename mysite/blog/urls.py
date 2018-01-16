from django.urls import path, re_path
from blog.views import *

app_name='blog'
urlpatterns = [

    # Example: /
    path('', PostLV.as_view(), name='index'),

    # Example: /post/ (same as /)
    path('post/', PostLV.as_view(), name='post_list'),

    # Example: /post/django-example/
    re_path('post/(?P<slug>[-\w]+)/', PostDV.as_view(), name='post_detail'),

    # Example: /archive/
    re_path('^archive/$', PostAV.as_view(), name='post_archive'),

    # Example: /2012/
    re_path('^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),

    # Example: /2012/nov/
    re_path('^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),

    # Example: /2012/nov/10/
    re_path('^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),

    # Example: /today/
    path('today/', PostTAV.as_view(), name='post_today_archive'),
    
    path('tag/', TagTV.as_view(), name='tag_cloud'),
    
    re_path('tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tagged_object_list'),
    
    path('search/', SearchFormView.as_view(), name='search'),
]
