# artist_api/urls.py
from django.urls import path
from .views import WorkListCreateView, ArtistWorkListView, ArtistRegistrationView, ArtistLoginView

urlpatterns = [
    path('works/', WorkListCreateView.as_view(), name='work-list-create'),
    path('works/<str:artist_name>/', ArtistWorkListView.as_view(), name='artist-work-list'),
    path('register/', ArtistRegistrationView.as_view(), name='artist-register'),
    path('login/', ArtistLoginView.as_view(), name='artist-login'),
]
