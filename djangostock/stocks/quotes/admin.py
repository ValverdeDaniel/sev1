from django.contrib import admin
from .models import Stock
from .models import Crypto

# Register your models here.
admin.site.register(Stock)
admin.site.register(Crypto)