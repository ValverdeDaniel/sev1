from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('add_stock', views.add_stock, name = 'add_stock'),
    path('delete/<stock_id>', views.delete, name="delete"),
    path('delete_stock_stock', views.delete_stock, name = 'delete_stock'),
    path('add_crypto', views.add_crypto, name = 'add_crypto'),
    path('cryptoHome', views.cryptoHome, name = 'cryptoHome'),
]