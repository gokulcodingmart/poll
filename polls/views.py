from django.shortcuts import render
from .models import Polllist, Choice, Vote
from django.contrib.auth.models import User
from django.core import serializers
from django.db.models import Sum, Max

# Create your views here.
def index(request):	
    
    votechart = Choice.objects.all()
    data = list()
    label = list()
    label.append('x')
    data.append(2)
    for c in votechart:
        data.append(c.votes)
        label.append(c.option)
    
    print(data)
    print(label)
    totalvote = dict()
    
    if request.method == "POST":
        if request.POST.get('title'):
            title  = request.POST.get('title')
            option  = request.POST.get('option')
            question  = request.POST.get('question')
            optionlist = option.split(',')
            user = request.user
            poll = Polllist.objects.create(title=title, question=question, user=user)

            for p in optionlist:
                Choice.objects.create(poll=poll, option=p)

    if request.user.id:
        polls = Polllist.objects.filter(user_id= request.user.id)
    else:
        polls = Polllist.objects.all()
    
    for p in polls:
        
        choicevote = list(Choice.objects.filter(poll_id=p.id).aggregate(totalvotes=Sum('votes')).values())[0]
        totalvote[p.id]=choicevote
  
    print(totalvote)
    return render(request, 'polls/index.html',{'poll':polls, 'charttrail':data, 'label':label, 'choice':votechart, 'votes':totalvote })


def about(request):	
    

    return render(request, 'polls/about.html')


def details(request,id):
    polls = Polllist.objects.get(id= id)
    votechart = Choice.objects.filter(poll_id=id)
    data = list()
    label = list()
    label.append('x')
    data.append(polls.title)
    for c in votechart:
        data.append(c.votes)
        label.append(c.option)
    # max = Choice.objects.filter(poll_id=id).aggregate(totalvotes=Max('votes'))
    max = Choice.objects.filter(poll_id=id).order_by('-votes')[0]
    report = Vote.objects.filter(option__poll__id=id)
    return render(request, 'polls/details.html', {'report':report, 'charttrail':data, 'label':label, 'poll':polls, 'max':max})


def contact(request):	
    

    return render(request, 'polls/contact.html')


def vote(request,id):
    alert = ""	
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
    question = poll[0].question
    return render(request, 'polls/vote.html', {'choice':choice, 'id':id, 'question':question, 'title':title, 'alert':alert})




def create(request):	
    if request.method == "POST":
        if request.POST.get('title'):
            title  = request.POST.get('title')
            option  = request.POST.get('option')
            question  = request.POST.get('question')
            optionlist = option.split(',')
            user = request.user
            poll = Polllist.objects.create(title=title, question=question, user=user)

            for p in optionlist:
                Choice.objects.create(poll=poll, option=p)
        return render(request, 'polls/index.html')


    return render(request, 'polls/create.html')



def tovote(request):	
    
    polls = Polllist.objects.exclude(user_id= request.user.id)
    return render(request, 'polls/tovote.html', {'poll':polls})
