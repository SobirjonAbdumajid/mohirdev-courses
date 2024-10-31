from django.contrib import admin
from ordering.models import User, Menu, OrderInfo

admin.site.register(User)
admin.site.register(Menu)
admin.site.register(OrderInfo)