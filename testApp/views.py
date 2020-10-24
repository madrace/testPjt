from django.shortcuts import render
from .models import Memo

# Create your views here.
def index(request) :
    context = dict()
    all_Memo = Memo.objects.all()
    context["all_Memo"] = all_Memo
    return render(request, "index.html", context)

def second(request) :
    return render(request, "second.html")

def test(request) :
    return render(request, "test/test.html")   