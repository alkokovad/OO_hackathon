from django.urls import path

from OO_hack_page import views

urlpatterns = [
    path('cards_list/', views.CardsListView.as_view(), name='cards_list'),
]
