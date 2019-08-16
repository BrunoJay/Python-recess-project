from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, "main_template.html", {})

def hello(request):
   text = """<h1>Welcome!</h1><br><br>"""
   return HttpResponse(text)

def mymap(request):
   return render(request, "map_showing_accident_severity.html", {})