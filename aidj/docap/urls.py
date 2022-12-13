from django.urls import path, include
from . import views


file_upload_url = [
    path('load/', views.Fileupload.as_view({'get': 'list', 'post': 'create'})),
]

in_file_meta_url = [
    path('list/', views.InFileMeta.as_view({'get': 'list', 'post': 'create'}))
]


urlpatterns = [
    path('', include(file_upload_url)),
    path('', include(in_file_meta_url)),
]