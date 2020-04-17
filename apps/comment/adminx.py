#@author: sareeliu
#@date: 2020/4/17 5:51
import xadmin
from .models import *

class CommentAdminx(object):
    list_display = ['article','user','parent','reply_to','body','created']
    search_fields = ['article','user','parent','reply_to','body','created']
    list_filter = ['article','user','parent','reply_to','body','created']
    model_icon = 'fa fa-plane'
    show_bookmarks = False

xadmin.site.register(Comment,CommentAdminx)