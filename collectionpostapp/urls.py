# collectionpostapp/urls.py

from django.urls import path
from . import views
from .views import CollectionPostList

urlpatterns = [
    #post api
    path('api/collectionpostinfo/', views.collection_post_info, name='collection_post_info'),
    #get api
    path('collection-posts/', CollectionPostList.as_view(), name='collectionpost-list'),
]
