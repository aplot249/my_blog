#@author: sareeliu
#@date: 2020/4/17 5:51
import xadmin
from .models import *

class ArticleColumnAdminx(object):
    list_display = ['title','created']
    search_fields = ['title','created']
    list_filter = ['title','created']
    model_icon = 'fa fa-plane'
    show_bookmarks = False

class ArticlePostAdminx(object):
    list_display = ['author','avatar','column','tags','title','short_body','total_views','likes','created','updated']
    search_fields = ['author','avatar','column','tags','title','body','total_views','likes','created','updated']
    list_filter = ['author','avatar','column','tags','title','body','total_views','likes','created','updated']
    model_icon = 'fa fa-plane'
    show_bookmarks = False

xadmin.site.register(ArticleColumn, ArticleColumnAdminx)
xadmin.site.register(ArticlePost, ArticlePostAdminx)