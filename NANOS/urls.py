from django.urls import path
from .views import Terminal, Index, Nano, Screenshot, Landing, AddNewNano, ShowUploadedVideo

urlpatterns = [
    path("all-nanos", Index.as_view(), name='index'),
    path("nano/<str:hostname>/terminal", Terminal.as_view(), name='terminal'),
    path("nano/<str:hostname>", Nano.as_view(), name='nano'),
    path("nano/<str:hostname>/screenshot", Screenshot.as_view(), name='screenshot'),
    path("", Landing.as_view(), name='landing'),
    path("add-new-nano", AddNewNano.as_view(), name='add'),
    path("nano/uploaded-video/<str:hostname>", ShowUploadedVideo.as_view(), name="uploaded-video")
]
