from django.views.generic import CreateView
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render,redirect,get_object_or_404
from .models import Restaurants,Menu
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
def top(request):
    return render(request,'myapp/top.html')


def myapp_search(request):
    #session
    request.session['aaa'] = 'keyword'
    keyword = request.GET.get('keyword')
    request.session['aaa'] = keyword
    session_data = request.session['aaa']
    
    #search
    restaurants = Restaurants.objects.all().order_by('-id')
    """ 検索機能の処理 """
    if keyword:
       keywords = keyword.split()
       for k in keywords:
        restaurants = Restaurants.objects.filter(
                      Q(name__icontains=k)| 
                      Q(address__icontains=k)
                      )
    else:
        restaurants = Restaurants.objects.filter(
                      Q(name__icontains=keyword)| 
                      Q(address__icontains=keyword)
                      )
        print("aaa")
        print([a.name for a in restaurants])
        messages.success(request, '「{}」の検索結果'.format(keyword))
    print(session_data)
    return render(request, 'myapp/search.html', {'myapp': restaurants,'keyword':session_data})

def myapp_detail_search(request,Restaurant_id):
    restaurant = get_object_or_404(Restaurants,pk=Restaurant_id)
    menus = Menu.objects.filter(
        Q(restaurant_id=Restaurant_id)
    )
    print(menus)
    return render(request, 'myapp/detail_search.html',{'restaurant':restaurant,'menus':menus})

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'myapp/signup.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('myapp:top')
        return render(request, 'myapp/signup.html', {'form': form})


class Login(LoginView):
    form_class = LoginForm
    template_name = 'myapp/login.html'


class Logout(LogoutView):
    template_name = 'myapp/logout.html'
