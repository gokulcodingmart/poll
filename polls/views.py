from django.shortcuts import render
from .models import Polllist

# Create your views here.
def index(request):	
    polls = Polllist.objects.all()

    return render(request, 'polls/index.html',{'poll':polls})
