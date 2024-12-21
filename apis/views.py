from rest_framework.views import APIView
from rest_framework import generics

from .models import Media
from .serializers import MediaSerializer

# create api
class MediaUploadAPIView(generics.CreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

# view api
class MediaList(generics.ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class FilterMediaList(generics.ListAPIView):
    queryset = Media.objects.filter(is_tarioty_original=True)
    serializer_class = MediaSerializer

# update
class MediaUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    lookup_field = 'pk'

# delete
class MediaDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    lookup_field = 'pk'
