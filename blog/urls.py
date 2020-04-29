from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog_list,name="post_home"),
    path('post/<int:id>/',views.blog_detail,name="post_detail"),
    path('post/new/',views.blog_create,name="post_create"),
    path('post/<int:id>/edit/',views.blog_update,name="post_update"),
    path('post/<int:id>/delete/',views.blog_delete,name="post_update"),
]
