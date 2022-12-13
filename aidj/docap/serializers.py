
from rest_framework import serializers
from . import models
from .db_method import PyExcel
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from .models import InFileData

import threading


class FileSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.FileData
        fields = ('id', 'file_save',)

    def create(self, validated_data):
        try:
            print(validated_data.get('file_save',))
            fs = models.FileData.objects.create(file_save=validated_data.get('file_save',))
            file_id = fs.id
            test = models.FileData.objects.get(pk=fs.id)
            threading.Thread(target=PyExcel.go_to_db, args=(test.file_save, int(file_id))).start()
            return fs
        except Exception as e:
            return e


class InFileDataSerializers(serializers.ModelSerializer):

    class Meta:
        model = InFileData
        fields = '__all__'


# Pagination classes
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 10000
