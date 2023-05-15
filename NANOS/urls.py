from django.urls import path
from .views import Terminal, Index, Nano, Screenshot, Landing, Nano2

urlpatterns = [
    path("all-nanos", Index.as_view(), name='index'),
    path("nano/<str:hostname>/terminal", Terminal.as_view(), name='page-nano'),
    path("nano/<str:hostname>", Nano.as_view(), name='nano'),
    path("nano2/<str:hostname>", Nano2.as_view(), name='nano2'),
    path("nano/<str:hostname>/screenshot", Screenshot.as_view(), name='screenshot'),
    path("", Landing.as_view(), name='landing')
]
