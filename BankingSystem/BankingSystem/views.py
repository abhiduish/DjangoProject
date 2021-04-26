from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def hello_Ever(request):

    return HttpResponse("<h1>hi Anukriti||||</h1>")
def index_page(request):

    return HttpResponse("<h1>welcome to index page||||</h1>")

def home_view(request):
    return render(request,"home.html")
def home_view1(request):
    return render(request,"todos.html")
    
class AboutUs(View):
    def get(self,request):
        return HttpResponse('<h1>we are here to knowe about class its abhijeet</h1>') 