from django.shortcuts import render
from .models import Polllist, Choice, Vote
from django.contrib.auth.models import User

# Create your views here.
def index(request):	
    if request.method == "POST":
        if request.POST.get('title'):
            title  = request.POST.get('title')
            option  = request.POST.get('option')
            optionlist = option.split(',')
            user = request.user
            poll = Polllist.objects.create(title=title, user=user)

            for p in optionlist:
                Choice.objects.create(poll=poll, option=p)


    polls = Polllist.objects.filter(user_id= request.user.id)

    return render(request, 'polls/index.html',{'poll':polls})


def about(request):	
    

    return render(request, 'polls/about.html')


def details(request,id):	
    
    report = Vote.objects.filter(option__poll__id=id)
    return render(request, 'polls/details.html', {'report':report})


def contact(request):	
    

    return render(request, 'polls/contact.html')


def vote(request,id):
    alert = "a"	
    if request.method == "POST":
       
        select  = request.POST.get('option')
        votermail  = request.POST.get('votermail')
        
        optionobject = Choice.objects.get(pk=select)
        poll = optionobject.poll.id

        match = Vote.objects.filter(option__poll__id=id, email = votermail)
        print(match)
        if not match:
            optionobject.votes = optionobject.votes +1
            optionobject.save(update_fields=["votes"]) 
            vote = Vote.objects.create(email=votermail, option=optionobject)
        else:
            alert = "You have already voted"   

        

    
    choice = Choice.objects.filter(poll_id=id)
    poll = Polllist.objects.filter(id=id)
    title = poll[0].title
    return render(request, 'polls/vote.html', {'choice':choice, 'id':id, 'title':title, 'alert':alert})