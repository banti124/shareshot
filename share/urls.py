from django.conf.urls import patterns, include, url

urlpatterns = patterns('share.views',
    url(r'^$', 'index', name='index'),
    url(r'^albums/(?P<pk>\d+)/$', 'album', name='album'),
    url(r'^photos/(?P<pk>\d+)/$', 'photo', name='photo'),
    url(r'^albums/delete/(\d+)/$', 'delete_album', name='delete_album'),
    url(r'^photos/delete/(\d+)/$', 'delete_photo', name='delete_photo'),
    url(r'^albums/privacy/(\d+)/(\w+)/$', 'change_album_privacy', name='change_album_privacy'),
    url(r'^photos/privacy/(\d+)/(\w+)/$', 'change_photo_privacy', name='change_photo_privacy'),
    url(r'^img/(\d+)/$', 'img', name='img'),
    url(r'^upload/photo/$', 'upload_photo', name='upload_photo'),
    url(r'^add/album/$', 'add_album', name='add_album'),
    url(r'^search/$', 'search', name='search'),
)
