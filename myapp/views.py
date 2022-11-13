from http.client import HTTPResponse
from django.contrib import messages
from .models import Post
from django.db.models import Q
from django.shortcuts import render
from .forms import SearchForm
from myapp.models import Restaurants

# Create your views here.

def top(request):
    return render(request,'myapp/top.html')

def myapp_new(request):
    return HTTPResponse('登録')

def myapp_edit(request,myapp_id):
    return HTTPResponse('編集')

def myapp_detail(request,myapp_id):
    return HTTPResponse('詳細閲覧')

def myapp_search(request):
     if request.method == 'GET':
        searchform = SearchForm(request.POST)

     if searchform.is_valid():
            name = request.GET['name']
            address = request.GET['address']

     if keyword:
           restaurants = restaurants.filter(
                 Q(name__icontains=keyword),
               ).all()
           print([a.name for a in restaurants])
           messages.success(request, '「{}」の検索結果'.format(keyword))

     return render(request, 'myapp/search.html', {'myapp': restaurants })
