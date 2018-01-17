from django.urls import include, path
from django.contrib import admin
from mysite.views import HomeView, UserCreateView, UserCreateDoneTV

#from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', HomeView.as_view(), name = 'home'),
    path('bookmark/', include('bookmark.urls', namespace='bookmark')),
    path('blog/', include('blog.urls', namespace='blog')),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),
]
