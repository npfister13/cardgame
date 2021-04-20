import json

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template.loader import render_to_string

from .models import Card, CardManager, monsters

# Create your views here.

with open('C:/Users/herpa/Documents/programming/python/cardgame/cardgamesite/monsters.json') as d:
    data = json.load(d)

def load_json_table_format(request):
    print(data)
    html = render_to_string()
    return HttpResponse({'d':data}, 'cardglossary/index.html', content_type="text/html")
    

class IndexView(generic.ListView):
    template_name = 'cardglossary/index.html'

    def get_queryset(self):
        return Card.objects
    
class DetailView(generic.DetailView):
    model = Card
    template_name = 'cardglossary/detail.html'

    def get_queryset(self):
        return Card.objects
    

def index(request):
    return HttpResponse("Hello world. You're at the cardglossary index.")