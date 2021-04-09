from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("classes", views.classes, name="classes"),
    path("past_hw", views.past_hw, name="past"),
    path("new_hw", views.new_hw, name="new"),
    
    
    path("edit", views.edit2, name="edit2"),
    path("edit/<int:idd>", views.edit, name="edit"),

    path("homework/done", views.done, name="done"),
]