from django.conf.urls import include, url
from . import views

# ^ in regex means "the beginning"; from this sign we can start looking for our pattern
# $ matches only "the end" of the string, which means that we will finish looking for our pattern here

urlpatterns = [
    url(r'^$', views.home),
    url(r'^postlist', views.post_list),
    url(r'^r.translate', views.realtime),
    url(r'^a.translate', views.audio_translate),
    
]