from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Post
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.
class Form_new_hw(forms.Form):
    title = forms.CharField(label = "title:")
    clas = forms.CharField(label = "class:")
    due_date = forms.CharField(label = "due date:")
    link = forms.CharField(label = "google doc link:", 
                    widget=forms.TextInput(attrs={'placeholder': 'in none type "none"'}))


def index(request):
    homeworks = Post.objects.filter(done="no")
    return render(request, "homework/index.html", {
        "homeworks":homeworks,
    })

def classes(request):
    return render(request, "homework/index.html")

def past_hw(request):
    homeworks = Post.objects.filter(done="yes")
    return render(request, "homework/past.html", {
        "homeworks":homeworks
    })

def new_hw(request):
    if request.method == "GET":
        return render(request, "homework/add_new.html", {
            "form": Form_new_hw()
        })
    else:
        form = Form_new_hw(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            clas = form.cleaned_data["clas"]
            due_date = form.cleaned_data["due_date"]
            link = form.cleaned_data["link"]
            done = "no"

            new_assigment = Post(title=title, clas=clas, due_date=due_date, link=link, done=done)
            new_assigment.save()
        return render(request, "homework/index.html")

@csrf_exempt
def done(request):
    if request.method == "POST":
        data = json.loads(request.body)
        content = data.get("content")
        id = data.get("id")
        done = data.get("done")
        if done == "yes":
            Post.objects.filter(id=id).update(done="yes")
        elif done == "no":
            Post.objects.filter(id=id).update(done="no")
    return HttpResponse(status=204)

@csrf_exempt
def edit(request, idd):
    if request.method == "GET":
        homework = Post.objects.get(id=idd)
        data = {
        "id": homework.id,
        "class": homework.clas,
        "title": homework.title,
        "due_date": homework.due_date,
        "link": homework.link,
        "done": homework.done
        }
        return JsonResponse(data, safe=False)

@csrf_exempt
def edit2(request):
     if request.method == "POST":
        data = json.loads(request.body)
        id = data.get("id")
        title = data.get("title")
        link = data.get("link")
        due_date = data.get("due_date")
        clas = data.get("clas")
        Post.objects.filter(id="3").update(title=title, link=link, due_date=due_date, clas=clas)
        return HttpResponse(status=204)