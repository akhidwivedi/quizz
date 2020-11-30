from django.shortcuts import render
from user.models import User


# Create your views here.
def index(request):
    if (request.method == 'POST'):
        form = User()
        form.uname = request.POST.get('name')
        form.save()
    else:
        form = User()
    return render(request,'index1.html',{})
