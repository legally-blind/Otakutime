from django.urls import path
from . import views

app_name= "SONG_PAGE"
urlpatterns = [
    path('', views.song_page, name="song_page"),
    path('create',views.song_create, name="create"),
    path('<slug>',views.song_detail, name="detail"),
    path('',views.profile_song_page, name="profile_song_page"),

]