import io
import base64
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for non-GUI rendering
import matplotlib.pyplot as plt
from django.http import HttpResponse

from django.shortcuts import render

def plot_view(request):
    # Create your plot
    plt.figure(figsize=(10, 5))
    plt.plot([2, 4, 3], [1, 2, 3])  # Example plot data

    # Save the plot to a BytesIO object and convert it to base64
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph = base64.b64encode(img.getvalue()).decode('utf-8')
    plt.close()  # Close the plot to free memory

    # Pass the graph to your template
    return render(request, 'crypto_chart.html', {'graph': graph})
