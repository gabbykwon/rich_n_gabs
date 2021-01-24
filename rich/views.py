from django.shortcuts import render

def index(request):
	return render(request, 'rich/index.html')

# Create your views here.
