from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth import authenticate, get_user_model

from rest_framework import generics, permissions, status
from rest_framework.response import  Response
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied

from rest_framework_simplejwt.tokens import RefreshToken


from .models import file, User
from .serializers import UserSerializer, FileSerializer




class UserSignupView(generics.CreateAPIView):
    serializer_class = UserSerializer


    def perform_create(self, serializer):
        user = serializer.save()

        token = RefreshToken.for_user(user)
        verify_url = f" {settings.FRONTEND_URL}/verify-email/{str(token.access_token)} "
        send_mail(
            'verify Your Email',
            f"Clcik the following link to verfiy your email : {verify_url}",
            settings.DEFAULT_FROM_EMAIL,
            [user.email]
        )
        return super().perform_create(serializer)


class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token = RefreshToken.for_user(user)
            return Response({
                'refresh' : str(token),
                'access' : str(token.access_token),
            })
        
        return Response({
            'error' : 'Invalid Credentials'
        }, status=status.HTTP_401_UNAUTHORIZED)
    

class fileuploadViews(generics.CreateAPIView):

    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        if not User.is_ops_user:
            raise PermissionDenied("Only ops users can upload files.")

        serializer.save(uploaded_by=user)
        return super().perform_create(serializer)
    

class FileListView(generics.ListAPIView):
    serializer_class  = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def  get_queryset(self):
        user =  self.request.user
        if user.is_client_user:
            return file.objects.all()
        raise PermissionDenied("Only Client users Can views the lsist of files.")
        return super().get_queryset()
    

class fileDownloadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        user = self.request.user
        if not user.is_client_user:
            raise PermissionDenied("Only Client users can download files. ")
        
        File = get_object_or_404(file, pk = pk)
        download_url = f"{settings.FRONTEND_URL}/download/{File.pk}"
        
        return Response({
            'download-link' : download_url,
            'message' : 'success'
        })
