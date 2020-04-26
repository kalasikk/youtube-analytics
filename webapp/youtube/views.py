import requests
import json
from django.shortcuts import render
from django.http import HttpResponse
from youtube.models import Video, Profile , Channel , Profile_Channel , Video_Statistic
from .service import getChannelById
from .forms import IdForm
# Create your views here.

def video(request):
    # response = requests.get('https://www.googleapis.com/youtube/v3/videos?part=statistics&id=HFyGEbLHM3A&key=AIzaSyC0ht_PIzPECVTM_BF9QzjhJLIDHR5aTd4')
    # data = response.json()
    form = IdForm
    # getChannelById('UC8M5YVWQan_3Elm-URehz9w')
    channels_list = Channel.objects.all()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = IdForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            getChannelById(form.cleaned_data['channel_id'])
            # redirect to a new URL:
            # return HttpResponse(form)
    form=IdForm()
    return render(request, 'youtube/video.html', {
        'channel': channels_list[0],
        'form':form,
    })


