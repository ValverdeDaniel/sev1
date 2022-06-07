from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages
# Create your views here.
# myPublicKey = 'pk_6768926b557d4f909e5ef4d36cfcd87f'

def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://sandbox.iexapis.com/stable/stock/" + ticker + "/quote?token=Tpk_514a8ac4edff420791d70ba761be8d89")
        
        try:
            api = json.loads(api_request.content)
            print('4')
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})


def cryptoHome(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://sandbox.iexapis.com/stable/stock/" + ticker + "/quote?token=Tpk_514a8ac4edff420791d70ba761be8d89")
        
        try:
            api = json.loads(api_request.content)
            print('4')
        except Exception as e:
            api = "Error..."
        return render(request, 'cryptoHome.html', {'api': api})

    else:
        return render(request, 'cryptoHome.html', {'ticker': "Enter a Ticker Symbol Above..."})



def about(request):
    return render(request, 'about.html', {})


def add_stock(request):
    import requests
    import json
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Has been Added"))  
            return redirect('add_stock')  

    else:
        ticker = Stock.objects.all()
        output = []
        for ticker_item in ticker:
            api_request = requests.get("https://sandbox.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=Tpk_514a8ac4edff420791d70ba761be8d89") 
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."
        
        return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock has been Deleted"))
    return redirect(delete_stock)

    
def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html', {'ticker': ticker})


def add_crypto(request):
    import requests
    import json
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Has been Added"))  
            return redirect('add_stock')  

    else:
        ticker = Stock.objects.all()
        output = []
        for ticker_item in ticker:
            api_request = requests.get("https://sandbox.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=Tpk_514a8ac4edff420791d70ba761be8d89") 
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."
        
        return render(request, 'add_crypto.html', {'ticker': ticker, 'output': output})