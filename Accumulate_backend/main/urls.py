from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, WordViewSet, SentenceViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'words', WordViewSet)
router.register(r'sentences', SentenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]