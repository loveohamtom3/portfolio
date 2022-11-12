from django.urls import path
from myapp import views
from.import views

app_name = 'myapp'

urlpatterns = [
  path("", views.top, name="top"),
  path("new/",views.myapp_new,name="myapp_new"),
  path("<int:myapp_id>/",views.myapp_detail,name="myapp_detail"),
  path("<int:myapp_id>/edit/",views.myapp_edit,name="snippet_edit"),
  path("search/",views.myapp_search,name="myapp_search"),
]