from django.urls import path

from .views import AuthorViewSet, BookViewSet, GenreViewSet, AuthorCreateView, AuthorListView, AuthorUpdateView, AuthorDeleteView


urlpatterns = [
    path('author/', AuthorViewSet.as_view, name='author'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/create/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/update/', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
    path('book/', BookViewSet.as_view, name='book'),
    path('genre/', GenreViewSet.as_view, name='genre'),
]
