from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from . import models
from Song.forms import Songcreate


def song_page(request):
    song = models.Song.objects.all().order_by('-date')
    args = {'song':song}
    return render(request, 'Song/song_list.html', args)

def profile_song_page(request):
    song = models.Song.objects.all().order_by('-date')
    args = {'song':song}
    return render(request, 'Song/profile_song_list.html', args)


def song_detail(request, slug):

    song = models.Song.objects.get(slug=slug)
    return render(request, 'Song/song_detail.html',{'song':song})




@login_required(login_url = "/Accounts/login")
def song_create(request):
    if request.method == 'POST':
        form = Songcreate(request.POST,request.FILES)
        if form.is_valid:
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('SONG_PAGE:song_page')
    else:
        form = Songcreate()
        return render(request , 'Song/song_create.html',{'form':form})
