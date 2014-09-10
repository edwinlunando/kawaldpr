from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from models import Legislature, Medium


class LegislatureList(ListView):
    model = Legislature
    template_name = 'legislature/legislature-list.html'
    context_object_name = 'legislatures'


class LegislatureDetail(DetailView):
    model = Legislature
    template_name = 'legislature/legislature-detail.html'
    context_object_name = 'legislature'


class MediumDetail(DetailView):
    model = Medium
    template_name = 'legislature/medium-detail.html'
    context_object_name = 'medium'
