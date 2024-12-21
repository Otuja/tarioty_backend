from django.urls import path
from .views import MediaUploadAPIView, MediaList, FilterMediaList, MediaUpdateAPIView, MediaDeleteAPIView


urlpatterns = [
    path('list_view', MediaList.as_view(), name='list-view'),
    path('filter_list', FilterMediaList.as_view(), name='filter-list-view'),
    path('upload_view', MediaUploadAPIView.as_view(), name='upload-view'),
    path('<int:pk>/update_view/', MediaUpdateAPIView.as_view(), name='list-view'),
    path('<int:pk>/delete_view/', MediaDeleteAPIView.as_view(), name='delete-view'),
]