from django.contrib import admin

from .models import *

class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_id', 'en_title','de_title', 'ru_title','sex', 'price')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'en_title', 'de_title', 'ru_title', 'icon')

admin.site.register(Procedure,ProcedureAdmin)
admin.site.register(CategoryProcedure,CategoryAdmin)