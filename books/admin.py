from django.contrib import admin
from .models import User,Order,Login,Inventory


admin.site.register(User)
admin.site.register(Order)
admin.site.register(Login)
admin.site.register(Inventory)
