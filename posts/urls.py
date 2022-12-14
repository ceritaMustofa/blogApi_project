from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import PostViewset, UserViewSet

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", PostViewset, basename="posts")

urlpatterns = router.urls
