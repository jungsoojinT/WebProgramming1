from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Question

def index(request):
    """목록출력"""
    question_list = Question.objects.order_by("-create_date")
    context = {'question_list':question_list}
    return render(request, 'board/question_list.html', context)