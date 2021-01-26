from django.urls import path
from . import views

app_name= "WALLPAPER_PAGE"
urlpatterns = [
    path('', views.wallpaper_page, name="wallpaper_page"),
    path('create',views.wallpaper_create, name="create"),
    path('<slug>',views.wallpaper_detail, name="detail"),
    path('',views.profile_wallpaper_page, name="profile_wallpaper_page"),

]