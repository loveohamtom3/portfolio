from http.client import HTTPResponse
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render
from .models import Restaurants
import re
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
    keyword = request.GET.get('keyword')
    restaurants = Restaurants.objects.order_by('-id')
    """ 検索機能の処理 """
    if keyword:
        keywords = keyword.split()
        for k in keywords:
         restaurants = restaurants.filter(
                      Q(Name__icontains=k)| 
                      Q(Description__icontains=k)
                      )
    else:
        restaurants = restaurants.filter(
                      Q(Name__icontains=keyword)| 
                      Q(Description__icontains=keyword)
                      )
        print("aaa")
        print([a.Name for a in restaurants])
        messages.success(request, '「{}」の検索結果'.format(keyword))
        
    return render(request, 'myapp/search.html', {'myapp': restaurants })
