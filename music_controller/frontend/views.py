from django.shortcuts import render

# Create your views here.

# render the index template in index.html
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')
