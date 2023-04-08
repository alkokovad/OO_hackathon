from django.urls import path

from OO_hack_page import views

urlpatterns = [
    path('', views.CardsEditView.as_view(), name=''),
]
