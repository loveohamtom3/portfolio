from http.client import HTTPResponse
from django.views.generic import View
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render,redirect
from .models import Restaurants
from .forms import SearchForm 
import re

class SearchView(View):
    def get(self,request,*args,**kwargs):
        form = SearchForm(request.POST or None)
        
        return render(request,'myapp/search.html',{
            'form':form,
        })
   


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
    #session
    request.session['aaa'] = 'keyword'
    keyword = request.GET.get('keyword')
    request.session['aaa'] = keyword
    session_data = request.session['aaa']
    
    #search
    restaurants = Restaurants.objects.order_by('-id')
    """ 検索機能の処理 """
    if keyword:
       keywords = keyword.split()
       for k in keywords:
        restaurants = Restaurants.objects.filter(
                      Q(Name__icontains=k)| 
                      Q(Description__icontains=k)
                      )
    else:
        restaurants = Restaurants.objects.filter(
                      Q(Name__icontains=keyword)| 
                      Q(Description__icontains=keyword)
                      )
        print("aaa")
        print([a.Name for a in restaurants])
        messages.success(request, '「{}」の検索結果'.format(keyword))
    print(session_data)
    return render(request, 'myapp/search.html', {'myapp': restaurants,'keyword':session_data})

def myapp_search_info(request):
    
    request.session['aaa'] = 'keyword'
    keyword = request.GET.get('keyword')
    request.session['aaa'] = keyword
    session_data = request.session['aaa']
    return render(request, 'myapp/search_info.html',{'keyword':session_data})
