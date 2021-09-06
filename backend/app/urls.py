from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .viewset import CustomerViewSet

router = DefaultRouter()
router.register(r'customer', CustomerViewSet, basename='customer')

urlpatterns = [
    path('', include(router.urls))
]