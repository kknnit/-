from django.conf.urls import url

from App import views

urlpatterns=[
    url(r'^index/',views.index),
    url(r'^dog/',views.dog ,name='dog'),
    url(r'^cat/',views.cat,name='cat'),
    # 模板和静态资源的区别
    url(r'^testst/',views.testst,name='testst'),
    # 文件上传源码
    url(r'^upload/',views.upload,name='upload'),
    url(r'^uploaddjango/',views.uploaddjango,name='uploaddjango'),
    # 将文件显示在页面中
    url(r'^getimage/',views.getimage),
]