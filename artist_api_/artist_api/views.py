
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Artist
from .serializers import ArtistSerializer, UserSerializer


from rest_framework import generics, permissions
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer

class WorkListCreateView(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class ArtistWorkListView(generics.ListAPIView):
    serializer_class = WorkSerializer

    def get_queryset(self):
        artist_name = self.kwargs['artist_name']
        return Work.objects.filter(artist__name=artist_name)

class ArtistRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ArtistSerializer

class ArtistRegistrationView(generics.CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to register

    def perform_create(self, serializer):
        user = serializer.save(user=self.request.user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class ArtistLoginView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to login

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
