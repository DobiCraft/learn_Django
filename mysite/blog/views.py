from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from blog.models import Post
from django.views.generic.base import TemplateView
from tagging.views import TaggedObjectList

# Create your views here.

#--- ListView
class PostLV(ListView) :
    model = Post
    template_name = 'blog/post_all.html'
    #template_name = 'blog/post_list.html' # 
    context_object_name = 'posts'
    paginate_by = 2

#--- DetailView
class PostDV(DetailView) :
    model = Post

#--- ArchiveView
class PostAV(ArchiveIndexView) :
    model = Post
    #template_name = 'blog/post_archive.html' # 
    date_field = 'modify_date'

class PostYAV(YearArchiveView) :
    model = Post
    #template_name = 'blog/post_archive_year.html' #
    date_field = 'modify_date'
    make_object_list = True

class PostMAV(MonthArchiveView) :
    model = Post
    #template_name = 'blog/post_archive_month.html' #
    date_field = 'modify_date'

class PostDAV(DayArchiveView) :
    model = Post
    #template_name = 'blog/post_archive_day.html' #
    date_field = 'modify_date'

class PostTAV(TodayArchiveView) :
    model = Post
    #template_name = 'blog/post_archive_day.html' # same as DayArchiveVies's template_name
    date_field = 'modify_date'

class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'

class PostTOL(TaggedObjectList):
    model = Post ;
    template_name = 'tagging/tagging_post_list.html'
    