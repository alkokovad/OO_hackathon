from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .models import REstate


class CardsListView(View):
    template_name = 'CardsList/cards_list.html'

    def get(self, request, *args, **kwargs):
        cards_list = REstate.objects.all()
        context = {'cards_list': cards_list}
        return render(request, CardsListView.template_name, context=context)
