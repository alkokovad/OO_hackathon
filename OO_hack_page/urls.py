from django.urls import path
from . import views


urlpatterns = [
    path('cards_list/', views.CardsListView.as_view(), name='cards_list'),
    path('dashboard/', views.DashBoardView.as_view(), name='dashboard'),
]
