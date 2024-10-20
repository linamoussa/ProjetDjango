from django.urls import path
from .views import *

urlpatterns = [
    path('list/',conferenceList,name="ListConf"),
    path('listViewConference/',ConferenceListView.as_view(),name="ListViewConf"),
    path('details/<int:pk>/',DetailsViewConference.as_view(),name="detailConf"),
]