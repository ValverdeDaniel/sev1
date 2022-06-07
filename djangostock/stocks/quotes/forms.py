from django import forms
from .models import Stock
from .models import Crypto

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["ticker"]

class CryptoForm(forms.ModelForm):
    class Meta:
        model = Crypto
        fields = ["coin"]
        