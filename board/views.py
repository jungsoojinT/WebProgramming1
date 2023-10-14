from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):
    """목록출력"""
    question_list = Question.objects.order_by("-create_date")
    context = {'question_list':question_list}
    return render(request, 'board/question_list.html', context)

def detail(request, question_id):
    """내용 출력"""
    question = get_object_or_404(Question, pk=question_id) #URL로 매핑 할때 저장된 id전달
    context = {'question':question}
    return render(request, 'board/question_detail.html', context) # context에 있는 Question 모델 데이터를 html 파일에 적용해 HTML 코드로 변환