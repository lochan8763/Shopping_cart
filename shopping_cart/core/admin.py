from django.contrib import admin
from .models import (User, Role  ,Category ,Product ,CartItem ,OrderItem 
                     ,CustomerAddress ,OrderStatus ,PaymentType ,OrderDetails)

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Role)