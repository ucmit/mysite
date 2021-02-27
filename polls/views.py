from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello world</h1>")


def meme(request):
    return HttpResponse("<img src='https://images-ext-2.discordapp.net/external/evKmOd-kO2vay98CKhzu_pH-SfEDlLRc1OUw0zaA2ic/https/n1s1.hsmedia.ru/c8/9f/cb/c89fcb31dd077084bc8bbc2284586b7f/1000x600_0xac120003_16946826431608901545.jpg?width=400&height=240'>")