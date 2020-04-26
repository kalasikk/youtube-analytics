from django.contrib import admin
from youtube.models import Video, Profile , Channel , Profile_Channel , Video_Statistic
# Register your models here.

admin.site.register(Video)
admin.site.register(Profile)
admin.site.register(Channel)
admin.site.register(Profile_Channel)
admin.site.register(Video_Statistic)