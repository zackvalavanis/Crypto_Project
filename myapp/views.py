from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
import os

def get_cryptocurrencies(request): 
  url = f"https://api.twelvedata.com/price?symbol=BTC/USD&apikey={os.getenv('CRYPTO_API_KEY')}" 
  
  print(url)
  
  response = requests.get(url)

  if response.status_code == 200:
    return JsonResponse(response.json())
  else:
    return JsonResponse('error', 'failed to fetch data')
  

  # https://api.twelvedata.com/price?symbol=[SYMBOL]&apikey=[YOUR 
