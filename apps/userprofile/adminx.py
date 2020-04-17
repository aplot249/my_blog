#@author: sareeliu
#@date: 2020/4/17 5:51
import xadmin
from xadmin import views

class GlobalSetting(object):
    site_title ="博客后台管理"
    site_footer ="Three个人博客"
    menu_style ="accordion"

class BaseSetting(object):
    enable_themes =True
    use_bootswatch =True

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)