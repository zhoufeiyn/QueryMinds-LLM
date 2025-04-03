from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.db import connection
from django.http import HttpResponseRedirect
from .models import ExerciseLlm,StudentEvaluationLlm


def llm_interact_stu(request):

    return render(request,'llminteract/llminteractstu.html')

def llm_interact_ins(request):

    return render(request,'llminteract/llminteractins.html')