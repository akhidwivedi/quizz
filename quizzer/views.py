from django.shortcuts import render
from quizzer.models import Exam

# Create your views here.
def onlineExam(request):
    result = Exam.objects.all()
    return render(request,'index2.html',{'Exam':result})

