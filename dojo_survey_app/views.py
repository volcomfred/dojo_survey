from django.shortcuts import render, redirect

def index(request):
    return render(request, 'form.html')

def process(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'lang': request.POST['language'],
            'loc': request.POST['location']
        }
        return render(request, 'result.html', context)
    return render (request, 'result.html')
    
# Create your views here.
