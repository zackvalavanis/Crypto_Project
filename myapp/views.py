import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
import os

from django.http import JsonResponse
from django.shortcuts import render
import requests
import os
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
# import logging 

# logger = logging.getLogger(__name__)


def cryptocurrency(request): 
    api_key = os.getenv("CRYPTO_API_KEY")
    url = f"https://api.twelvedata.com/time_series?symbol=BTC/USD&interval=1h&apikey={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        # Print to console (debugging)
        print(json.dumps(data, indent=2))  # Pretty print the JSON response 
        
        return JsonResponse(data)  # Return JSON response to browser/Postman
    else:
        return JsonResponse({"error": "Failed to fetch data"}, status=500)






def get_crypto_price_chart(request): 
    api_key = os.getenv("CRYPTO_API_KEY")
    url = f"https://api.twelvedata.com/time_series?symbol=BTC/USD&interval=1h&apikey={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(data)
     
        print(df.head())
        if "values" in data:
            df = pd.DataFrame(data["values"])
            df["datetime"] = pd.to_datetime(df["datetime"])
            df["close"] = df["close"].astype(float)
            df = df.sort_values("datetime")

            # Plot the graph
            plt.figure(figsize=(10, 5))
            plt.plot(df["datetime"], df["close"], marker="o", linestyle="-", color="blue")
            plt.xlabel("Time")
            plt.ylabel("Price (USD)")
            plt.title("Bitcoin Price Over Time")
            plt.xticks(rotation=45)
            plt.grid()

            # Save the plot as a PNG in memory
            buffer = BytesIO()
            plt.savefig(buffer, format="png")
            buffer.seek(0)
            image_png = buffer.getvalue()
            buffer.close()

            graph = base64.b64encode(image_png).decode("utf-8")
            return render(request, "crypto_chart.html", {"graph": graph})
        else:
            return JsonResponse({"error": "Invalid API response format"})
    
    return JsonResponse({"error": "Failed to fetch data"})
