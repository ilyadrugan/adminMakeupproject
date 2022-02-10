from django.contrib import admin

from .models import *

class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_id', 'en_title','de_title', 'ru_title', 'price_women', 'price_men')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'en_title', 'de_title', 'ru_title', 'icon')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'map_position', 'email', 'facebook_link', 'instagram_link')

admin.site.register(Procedure,ProcedureAdmin)
admin.site.register(CategoryProcedure,CategoryAdmin)
admin.site.register(Contacts,ContactAdmin)