from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'conditions.html',context=d)
def for_loop(request):
    d={'name':'rohan','age':70,'gender':'female'}
    return render(request,'for_loop.html',context=d)



