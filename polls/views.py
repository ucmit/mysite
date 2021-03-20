from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "questions"

    def get_queryset(self):
        return Question.objects.all()


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, q_id):
    # Ответы пользователя - хранит pk
    choices = request.POST.getlist("choice")
    question = Question.objects.get(pk=q_id)

    for c_pk in choices:
        choice = question.choice_set.get(pk=c_pk)
        choice.votes += 1
        choice.save()

    return HttpResponseRedirect( reverse("polls:results", args=(q_id, ))  )


def meme(request):
    return HttpResponse("<img src='https://images-ext-2.discordapp.net/external/evKmOd-kO2vay98CKhzu_pH-SfEDlLRc1OUw0zaA2ic/https/n1s1.hsmedia.ru/c8/9f/cb/c89fcb31dd077084bc8bbc2284586b7f/1000x600_0xac120003_16946826431608901545.jpg?width=400&height=240'>")
