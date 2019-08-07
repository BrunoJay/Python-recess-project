from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	welcome = """<h1>Hello, world. You're at the web index.</h1><br><br>
   			<a href="hello">Home</a>
			<a href="mymap">Map</a>
   """
	return HttpResponse(welcome)

def hello(request):
   text = """<h1>welcome to my app !</h1><br><br>
   			<a href="/ourProject/">Home</a>
			<a href="/ourProject/mymap">Map</a>
   """
   return HttpResponse(text)

def mymap(request):
   return render(request, "map.html", {})