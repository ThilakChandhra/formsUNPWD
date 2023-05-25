from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def form(request):
    if request.method=='POST':
        name=request.POST['un']
        pwd=request.POST['pd']
        print(name)
        print(pwd)
        return HttpResponse('Successfully completed!..')
    return render(request,'form.html')