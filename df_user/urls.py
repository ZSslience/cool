from django.conf.urls import url
from df_user import views

urlpatterns = [
    url(r'^register/$', views.register), # 用户注册页面
    #url(r'^register_handle/$', views.register_handle), # 进行用户注册处理
]