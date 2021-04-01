from typing import List
from django.shortcuts import render
from django.views.generic.list import ListView
from . import models

# Create your views here.
# def index(request):
#     return HttpResponse('Hello, world!!')

class PresentationListView(ListView):
    # Load all Presentations
    model = models.Presentation
    template_name = 'presentation_list.html'
    context_object_name = 'presentations'
