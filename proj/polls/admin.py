from django.contrib import admin
from polls.models import Books 

class MyBook(admin.ModelAdmin):
    list_display = ['author','name','pub_date']

admin.site .register(Books,MyBook)
# Register your models here.
