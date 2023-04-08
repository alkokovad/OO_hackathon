from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View


class CardsEditView(View):
    template_name = 'CardsPages/cards_edit.html'

    def get(self, request):
        return render(request, CardsEditView.template_name)
