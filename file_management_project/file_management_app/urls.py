from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, FolderViewSet, FileViewSet, ShareViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'folders', FolderViewSet)
router.register(r'files', FileViewSet)
router.register(r'shares', ShareViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
