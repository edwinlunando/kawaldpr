from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from models import Legislature


class LegislatureList(ListView):
    model = Legislature
    template_name = 'legislature/legislature-list.html'
    context_object_name = 'legislatures'


class LegislatureDetail(TemplateView):
    template_name = 'legislature/legislature-detail.html'


class MediumDetail(TemplateView):
    template_name = 'legislature/medium-detail.html'
