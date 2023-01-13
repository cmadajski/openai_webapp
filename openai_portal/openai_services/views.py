from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return redirect('/openai/')

def services(request):
    return render(request, 'openai_services/index.html')