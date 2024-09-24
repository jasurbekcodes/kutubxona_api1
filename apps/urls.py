from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.views import AuthorViewSet, BookViewSet, GenreViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'genres', GenreViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
