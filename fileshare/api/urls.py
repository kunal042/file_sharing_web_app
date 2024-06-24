from django.urls import path
from .views import UserSignupView, UserLoginView, fileuploadViews, FileListView,fileDownloadView


urlpatterns = [
    path('singup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('upload/', fileuploadViews.as_view(), name='file-upload'),
    path('files/', FileListView.as_view(), name='file-list'),
    path('files/', FileListView.as_view(), name='file-list'),
    path('download/<int:pk>/', fileDownloadView.as_view(), name='file-download'),
]
