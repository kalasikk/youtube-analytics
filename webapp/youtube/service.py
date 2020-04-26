import requests
from .models import Video_Statistic, Channel


def get(url):
    response = requests.get(url)
    data = response.json()
    return data

def getChannelById(channelId):
    url = 'https://www.googleapis.com/youtube/v3/channels?part=snippet,contentDetails,statistics&id=' + channelId + '&key=AIzaSyC0ht_PIzPECVTM_BF9QzjhJLIDHR5aTd4'
    data = get(url)
    setChannelModel(data)

def getVideosByPlaylistId(playlistId):
    url = 'https://www.googleapis.com/youtube/v3/playlistItems?playlistId=' + playlistId +'&key=AIzaSyC0ht_PIzPECVTM_BF9QzjhJLIDHR5aTd4&part=snippet&maxResults=20'
    return get(url)

def getVideoStatisticById(videoId):
    url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&id='+ videoId +'&key=AIzaSyC0ht_PIzPECVTM_BF9QzjhJLIDHR5aTd4'
    return get(url)

def setChannelModel(data):
    channel = Channel()
    channel.channel_id = data['items'][0]['id']
    channel.title = data['items'][0]['snippet']['title']
    channel.description = data['items'][0]['snippet']['description']
    channel.publishedAt = data['items'][0]['snippet']['publishedAt']
    channel.thumbnail = data['items'][0]['snippet']['thumbnails']['medium']['url']
    channel.width = data['items'][0]['snippet']['thumbnails']['medium']['width']
    channel.height = data['items'][0]['snippet']['thumbnails']['medium']['height']
    channel.country = data['items'][0]['snippet']['country']
    channel.viewCount = data['items'][0]['statistics']['viewCount']
    channel.subscriberCount = data['items'][0]['statistics']['subscriberCount']
    channel.videoCount = data['items'][0]['statistics']['videoCount']
    channel.playlist_id = data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    channel.save()

