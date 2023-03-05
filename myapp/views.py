from asyncio.log import logger
from django.views.generic import CreateView,DetailView,UpdateView
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404,resolve_url
from .models import Restaurants,Menu,Review,Like,Consideration
from .forms import SignUpForm,LoginForm,ReviewForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User
from django.db.models import Avg
from django.contrib.auth.mixins import UserPassesTestMixin
from .mixins import OnlyYouMixin 
from django.contrib.auth.decorators import login_required
from .forms import UserForm
import urllib.parse


def base(request):
    return render(request, 'base.html')
 
def myapp_search(request):
    # session
    request.session['aaa'] = 'keyword'
    keyword = request.GET.get('keyword')
    request.session['aaa'] = keyword
    session_data = request.session['aaa']

    # search
    restaurants = Restaurants.objects.all().order_by('-id')
    myapp_restaurants = Menu.objects.select_related('restaurant_id').all().order_by('-id')
    #restaurant_search
    if keyword:
        keywords = keyword.split()
        for k in keywords:
            restaurants = Restaurants.objects.filter(
                Q(name__icontains=k) |
                Q(description__icontains=k) |
                Q(address__icontains=k) |
                Q(category__icontains=k)
            )
            print("restaurants")
            print([a.name for a in restaurants])
            messages.success(request, '「{}」の検索結果'.format(keyword))
    #menu_search    
    myapp_restaurants = Menu.objects.filter(name=keyword).select_related('restaurant_id')
    if keyword:
        keywords = keyword.split()
        for k in keywords:
            myapp_restaurants = Menu.objects.filter(
                Q(name__icontains=k) 
            )
            print("myapp_restaurants")
    #count
    restaurants_count = restaurants.count()
    myapp_restaurants_count = myapp_restaurants.count()
    
    param = {
      'myapp':restaurants,
      'myapp_restaurants':myapp_restaurants,
      'keyword':session_data,
      'restaurant':restaurants_count,
      'menus':myapp_restaurants_count,
    }
    return render(request, 'myapp/search.html', param)

class Detail(DetailView):
    template_name = 'myapp/detail.html'
    
def myapp_detail(request,Restaurant_id):
    restaurant = get_object_or_404(Restaurants, pk=Restaurant_id)
    menus = Menu.objects.filter(
        Q(restaurant_id=Restaurant_id)
    )
    print(restaurant)
    
    # review
    review_list = Review.objects.all()[:10]
    review_count = Review.objects.filter(restaurant_id=Restaurant_id).count()
    score_ave = Review.objects.filter(restaurant_id = Restaurant_id).aggregate(Avg('score'))
    average = score_ave['score__avg']
    if average:
        average_rate = average / 5 * 100
    else:
        average_rate = 0

    if request.method == 'GET':        
       review_form = ReviewForm()
       review_list = Review.objects.filter(restaurant_id = Restaurant_id)
    else:
       form = ReviewForm(data=request.POST)
       score = request.POST['score']
       comment = request.POST['comment']
       
       if form.is_valid():
        review = Review()
        review.restaurant_id = Restaurant_id
        review.restaurant_name  
        review.user = request.user
        review.score = score
        review.comment = comment
        review.save()
        return redirect(request.get_full_path())
       return render(request, 'myapp/detail.html', {})
    #like,consider 
    is_like = Like.objects.filter(user=request.user.id, restaurant=Restaurant_id).exists()
    is_consider = Consideration.objects.filter(user=request.user.id, restaurant=Restaurant_id).exists()
    
    params = {
    'title': '店舗詳細',
    'review_count': review_count,
    'review_form': review_form,
    'review_list': review_list,
    'average': average,
    'average_rate': average_rate,
    'review_list': review_list,
    'restaurant': restaurant,
    'menus':menus,
    'is_like':is_like,
    'is_consider':is_consider,
    }  
    return render(request, 'myapp/detail/detail.html',params)
  

@login_required
def like(request,restaurant_id):
    restaurant = get_object_or_404(Restaurants, id=restaurant_id)
    like, created = Like.objects.get_or_create(
      user=request.user,
      restaurant=restaurant
    )
    if not created:
        like.delete()
    return redirect('myapp:detail', restaurant.id)


@login_required
def consider(request,restaurant_id):
        restaurant = get_object_or_404(Restaurants, id=restaurant_id)
        consider, created = Consideration.objects.get_or_create(
                user=request.user, restaurant=restaurant)
        if not created:
            consider.delete()


        if "keyword" in request.POST:

            from django.urls import reverse
            url         = reverse("myapp:search")
            
            parameters  = f"mode={request.POST['mode']}&keyword={request.POST['keyword']}"

            return redirect(f"{url}?{parameters}") 
        return redirect('myapp:detail',restaurant.id)
class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'myapp/signup.html'

    def post(self, request):

        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            print(username)
            print(raw_password)

            user = authenticate(request, username=username, password=raw_password)
            print("==========")
            login(request, user)
            if "next" in request.GET:
             return redirect(to=request.GET["next"])
        else:
            next = request.GET.get('next')

        param = {
            'form': form,
            'next': next,
        }
        return render(request, 'myapp/signup.html',param)


def LoginView(request):
    print('ppp')
    if request.method == 'POST':
        print('ccc')
        logger.debug('pppppppppppppppppppppppppppppppppppp')
        next = request.POST.get('next')
        logger.debug(next)
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
        if next == 'None':
            return redirect(to='myapp/signup.html')
        else:
            next = urllib.parse.unquote(next)
            return redirect(to=next)
    else:
        form = LoginForm()
        next = request.GET.get('next')
    param = { 
        'form': form,
        'next': next,
    }   
    return render(request, 'myapp/login.html', param)


class Logout(LogoutView):
    template_name = 'myapp/logout.html'
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser   
class UserDetailView(DetailView):
    model = User
    template_name = "myapp/user/userDetail.html"
   #like,considerList
    def get_context_data(self, **kwargs):        
      context = super().get_context_data(**kwargs)
      print(kwargs["object"].id)
      context['likes']=Like.objects.filter(user=kwargs["object"].id)
      context['consideration']=Consideration.objects.filter(user=kwargs["object"].id)
      return context
      
class UserUpdateView(OnlyYouMixin,UpdateView):
  model = User
  template_name = "myapp/user/update.html"
  form_class = UserForm
  
  def get_success_url(self): 
    return resolve_url('myapp:userDetail',pk=self.kwargs['pk'])
  
