
from rest_framework import status, views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import FileData, InFileData
from .serializers import FileSerializers, StandardResultsSetPagination, InFileDataSerializers


class Fileupload(viewsets.ModelViewSet):
    queryset = FileData.objects.all()
    serializer_class = FileSerializers
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']


class InFileMeta(viewsets.ModelViewSet):
    queryset = InFileData.objects.all()
    serializer_class = InFileDataSerializers
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['original_file']
