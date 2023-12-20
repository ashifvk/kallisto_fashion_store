from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(login)
admin.site.register(UserRegister)
# admin.site.register(Products)
# admin.site.register(productsize)


class sizetabview(admin.TabularInline):
    model=productsize

class productlistview(admin.ModelAdmin):
    list_display=('id','name','actualprice','discountprice')
    inlines=[sizetabview,]
admin.site.register(Products,productlistview)
admin.site.register(cart)
admin.site.register(favourite)

