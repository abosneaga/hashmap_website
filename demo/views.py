from django.shortcuts import render
from django.http import HttpResponse

def demo(request):
    # return HttpResponse("This is a landing page.")
    return render(request, 'demo/demo.html', {})
