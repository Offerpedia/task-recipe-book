from django.contrib import admin
from .models import CustomUser,Customer,Chef


# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Customer)
admin.site.register(Chef)
