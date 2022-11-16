from http.client import HTTPResponse
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render
from .forms import SearchForm
from .models import Restaurants
from functools import reduce
from operator import and_


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
    if request.method == 'POST':
       form = SearchForm(request.POST)
    restaurants = Restaurants.objects.order_by('-id')
    """ 検索機能の処理 """
    keyword = request.GET.get('keyword')
    
    if keyword:
        restaurants = restaurants.filter(
                      Q(name__icontains=keyword))| Q(text__icontains=keyword).all()
        messages.success(request, '「{}」の検索結果'.format(keyword))
 
    return render(request, 'myapp/search.html', {'myapp': restaurants })
