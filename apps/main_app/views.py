from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string
def index(request):
    if 'count' in request.session:
        request.session['count'] = request.session['count'] + 1
    else:
        request.session['count'] = 1
    request.session['randomword'] = get_random_string(length=14)
    return render(request, "main_app/index.html")
def reset(request):
    del request.session['count']
    return redirect('/random_word')

# Create your views here.
