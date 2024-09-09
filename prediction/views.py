# views.py
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.views import LoginView
import pickle
import numpy as np
import os

model_path = os.path.join('house_price_prediction', 'house_price_model.pkl')

# Load the model
model = pickle.load(open(model_path, 'rb'))

def custom_login(request):
    return render(request, 'prediction/admin_login.html')


def predict_price(request):
    if request.method == 'POST':
        # Get user input
        size = float(request.POST['size'])
        bedrooms = int(request.POST['bedrooms'])
        bathrooms = int(request.POST['bathrooms'])
        location_score = float(request.POST['location_score'])

        # Predict the price
        features = np.array([[size, bedrooms, bathrooms, location_score]])
        predicted_price = model.predict(features)[0]

        return render(request, 'prediction/result.html', {'price': predicted_price})
    else:
        return render(request, 'prediction/home.html')
