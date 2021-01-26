from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from . import models
from Video.forms import Videocreate


def video_page(request):
    video = models.Video.objects.all().order_by('-date')
    args = {'video':video}
    return render(request, 'Video/video_list.html', args)

def profile_video_page(request):
    video = models.Video.objects.all().order_by('-date')
    args = {'video':video}
    return render(request, 'Video/profile_video_list.html', args)


def video_detail(request, slug):

    video = models.Video.objects.get(slug=slug)
    return render(request, 'Video/video_detail.html',{'video':video})




@login_required(login_url = "/Accounts/login")
def video_create(request):
    if request.method == 'POST':
        form = Videocreate(request.POST,request.FILES)
        if form.is_valid:
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('VIDEO_PAGE:video_page')
    else:
        form = Videocreate()
        return render(request , 'Video/video_create.html',{'form':form})

