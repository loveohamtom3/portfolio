from django.contrib import admin
from django.urls import path,include

from myapp.views import top

urlpatterns = [
    path('',include('myapp.urls')),
    path('admin/',admin.site.urls),
]