from django.urls import path
from rest_framework.routers import DefaultRouter

from site_operation.views import IndexPageView, IndexImageView, TopBookByCategory, TopBookValueViewSet

router = DefaultRouter()
router.register(r'index_link', IndexPageView, basename='index_link')
router.register(r'index_image', IndexImageView, basename='index_image')

urlpatterns = [
    path('ranking/<request_item>', TopBookValueViewSet.as_view(), name='ranking-detail'),
    path('ranking/<requestCategory>/<request_item>', TopBookByCategory.as_view(), name='category-ranking-detail')
]
urlpatterns += router.urls
