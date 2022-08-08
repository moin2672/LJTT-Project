from django.urls import path

from . import views

urlpatterns = [
    path('cards', views.LJTTCardListView.as_view(), name="cards.list"),
    path('cards/<int:pk>', views.LJTTCardDetailView.as_view(), name="cards.detail"),
    path('cards/new', views.LJTTCardCreateView.as_view(), name="cards.new"),
    path('cards/<int:pk>/edit', views.LJTTCardUpdateView.as_view(), name="cards.update"),
    path('cards/<int:pk>/delete', views.LJTTCardDeleteView.as_view(), name="cards.delete"),
    path('like/<int:pk>', views.LikeView, name="like"),
    path('mylikedpost/<int:pk>', views.MyLikedCardsView, name="cards.like"),
    path('lessons', views.LessonListView, name="lessons.list"),
    path('lessons/new', views.LessonCreateView.as_view(), name="lessons.new"),
    path('lessons/<int:pk>/edit', views.LessonUpdateView.as_view(), name="lessons.update"),
    path('lessons/<int:lName_id>', views.LessonWiseLJTTCardView, name="lessons.cards"),
]