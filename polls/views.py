from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice

# Create your views here.
def index(request):
    q_all = Question.objects.all()
    res = "<ol>"
    for q in q_all:
        res += "<li>%s</li>" % q.text
    res += "</ol>"

    return HttpResponse(res)

def detail(request, q_id):
    res = "Question number %s." % q_id 
    return HttpResponse(res)

def results(requst, q_id):
    res = "Result for question number %s." % q_id 
    return HttpResponse(res)

def vote(request, q_id):
    res = "Vote for question number %s." % q_id 
    return HttpResponse(res)











def meme(request):
    return HttpResponse("<img src='https://images-ext-2.discordapp.net/external/evKmOd-kO2vay98CKhzu_pH-SfEDlLRc1OUw0zaA2ic/https/n1s1.hsmedia.ru/c8/9f/cb/c89fcb31dd077084bc8bbc2284586b7f/1000x600_0xac120003_16946826431608901545.jpg?width=400&height=240'>")
