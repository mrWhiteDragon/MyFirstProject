from django.shortcuts import render

def index(request):
	return render(request, 'LifeManager/basic.html', {'values': ['Звоните по телефону:', '8-901-389-82-27']})
