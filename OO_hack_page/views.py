from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View


class CardsListView(View):
    template_name = 'CardsList/cards_list.html'

    def get(self, request):
        return render(request, CardsListView.template_name)
