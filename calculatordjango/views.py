from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def index(request):
    return render(request,'calculator.html')

def submitquery(request):
    q = request.GET['query']
    try:
        ans = eval(q)
        print(ans)
        mydictionary = {
            'q': q,
            'ans': ans,
            'error':False
        }
        return render(request,'calculator.html', mydictionary)
    except:
        mydictionary ={
            'error':True
        }
        return render(request,'calculator.html', mydictionary)