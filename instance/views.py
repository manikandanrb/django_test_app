from django.shortcuts import render
from instance import tasks
# Create your views here.

def index(request):
    return render(request, 'index.html')
