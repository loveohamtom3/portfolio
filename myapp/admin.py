from django.contrib import admin
from myapp.models import Restaurants,Menu,Review,Like,Consideration

admin.site.register(Restaurants)
admin.site.register(Menu)
admin.site.register(Like)
admin.site.register(Consideration)

@admin.register(Review) 
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('restaurant_id', 'restaurant_name', 'user', 'score')
    list_display_links = ('restaurant_name',)
    list_editable = ('score',)




# Register your models here.
