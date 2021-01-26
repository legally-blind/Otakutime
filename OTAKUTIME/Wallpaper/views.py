from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from . import models
from Wallpaper.forms import Wallpapercreate


def wallpaper_page(request):
    wallpaper = models.Wallpaper.objects.all().order_by('-date')
    args = {'wallpaper':wallpaper}
    return render(request, 'Wallpaper/wallpaper_list.html', args)

def profile_wallpaper_page(request):
    wallpaper = models.Wallpaper.objects.all().order_by('-date')
    args = {'wallpaper':wallpaper}
    return render(request, 'Wallpaper/profile_wallpaper_list.html', args)


def wallpaper_detail(request, slug):

    wallpaper = models.Wallpaper.objects.get(slug=slug)
    return render(request, 'Wallpaper/wallpaper_detail.html',{'wallpaper':wallpaper})




@login_required(login_url = "/Accounts/login")
def wallpaper_create(request):
    if request.method == 'POST':
        form = Wallpapercreate(request.POST,request.FILES)
        if form.is_valid:
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('WALLPAPER_PAGE:wallpaper_page')
    else:
        form = Wallpapercreate()
        return render(request , 'Wallpaper/wallpaper_create.html',{'form':form})
