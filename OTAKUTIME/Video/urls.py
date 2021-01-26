from django.urls import path
from . import views

app_name= "VIDEO_PAGE"
urlpatterns = [
    path('', views.video_page, name="video_page"),
    path('create',views.video_create, name="create"),
    path('<slug>',views.video_detail, name="detail"),
    path('',views.profile_video_page, name="profile_video_page"),

]