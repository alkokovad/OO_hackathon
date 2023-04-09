from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .models import REstate, Workgroup_time


class CardsListView(View):
    template_name = 'CardsList/cards_list.html'

    def get(self, request, *args, **kwargs):
        cards_list = REstate.objects.all()
        context = {'cards_list': cards_list}
        return render(request, CardsListView.template_name, context=context)

    def post(self, request, *args, **kwargs):
        cards_list = REstate.objects.get(pk=kwargs['pk'])
        context = {'cards_list': cards_list}
        return render(request, CardsListView.template_name, context=context)


class DashBoardView(View):
    template_name = 'DashBoard/dashboard.html'

    def get(self, request, *args, **kwargs):
        dashboards = Workgroup_time.objects.all()
        context = {'dashboards': dashboards}
        return render(request, DashBoardView.template_name, context=context)
