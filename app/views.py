from django.shortcuts import render

# Create your views here.
def aj(request):
    d={'a':123222,'b':5399,'c':400000}
    return render(request,"aj.html",context=d)