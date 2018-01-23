from django.shortcuts import render

from .models import Video


def video(request):
    video_list = Video.objects.all()
    return render(request, 'videos/video.html', {'video_list': video_list})


def detail(request, pk):
    detail = Video.objects.get(pk=pk)
    return render(request, 'videos/detail.html', {'detail': detail})
