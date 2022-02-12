from django.contrib import admin

from .models import *

class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_id', 'en_title','de_title', 'ru_title', 'price_women', 'price_men')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'en_title', 'de_title', 'ru_title', 'icon', 'picture')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'map_position', 'email','site', 'facebook_link', 'instagram_link')

class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'procedure_name', 'price','first_name', 'last_name', 'email', 'phone', 'time','time_create')

admin.site.register(Procedure,ProcedureAdmin)
admin.site.register(CategoryProcedure,CategoryAdmin)
admin.site.register(Contacts,ContactAdmin)
admin.site.register(Requests,RequestAdmin)