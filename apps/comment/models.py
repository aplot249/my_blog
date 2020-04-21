from django.db import models
from django.contrib.auth.models import User
from article.models import ArticlePost
# django-ckeditor
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# django-mptt
from mptt.models import MPTTModel, TreeForeignKey

# 博文的评论
class Comment(MPTTModel):
    article = models.ForeignKey(ArticlePost,on_delete=models.CASCADE,related_name='comments')   #对哪个文章进行评论
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')             #谁评论的
    # mptt树形结构
    parent = TreeForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='children')
    # 记录二级评论回复给谁, str
    reply_to = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,related_name='replyers')    #评论给谁
    body = RichTextUploadingField()   #RichTextField()      #评论的内容
    created = models.DateTimeField(auto_now_add=True)       #评论时间
    class MPTTMeta:
        order_insertion_by = ['created']
    def __str__(self):
        return self.body[:20]
    class Meta:
        verbose_name = "文章评论"
        verbose_name_plural = verbose_name
