from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from churn.models import Customer
from churn.serializers import CustomerSerializer
import joblib
import json
from datetime import datetime

class HomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Render the homepage with upload form
        return render(request, "home.html")

class ChurnPredictionAPIView(APIView):
    def post(self, request):
        # Get the data from the request
        data = request.data

        # Extract features for prediction
        customer_id = data.get('customer_id')
        last_purchase_date = data.get('last_purchase_date')
        total_orders = data.get('total_orders')
        total_spent = data.get('total_spent')
        average_order_value = data.get('average_order_value')
        days_since_last_purchase = data.get('days_since_last_purchase')

        # Validate the input data
        if not all([customer_id, total_orders, total_spent, average_order_value, days_since_last_purchase]):
            return Response({"error": "Missing required fields"}, status=400)

        # Convert last_purchase_date to datetime object
        try:
            last_purchase_date = datetime.strptime(last_purchase_date, "%Y-%m-%d").date()  # Parse string to date
        except ValueError:
            return Response({"error": "Invalid date format. Please use YYYY-MM-DD."}, status=400)

        # Load the trained model and the scaler
        model = joblib.load(r'E:\Customer_Churn_Prediction\churn_predictor\churn\static\models\churn_model.pkl')  # Adjust the path to your model
        scaler = joblib.load(r'E:\Customer_Churn_Prediction\churn_predictor\churn\static\models\scaler.pkl')  # Adjust the path to your scaler

        # Prepare the features for prediction
        features = [
            total_orders,
            total_spent,
            average_order_value,
            days_since_last_purchase
        ]

        # Scale the features using the saved scaler
        scaled_features = scaler.transform([features])

        # Make prediction
        prediction = model.predict(scaled_features)

        # Check if customer exists, and create or update it
        customer, created = Customer.objects.update_or_create(
            customer_id=customer_id,
            defaults={
                'last_purchase_date': last_purchase_date,
                'total_orders': total_orders,
                'total_spent': total_spent,
                'average_order_value': average_order_value,
                'days_since_last_purchase': days_since_last_purchase,
                'churned': prediction[0]  # Set churn prediction result
            }
        )

        return Response({"customer_id": customer.customer_id, "churn_prediction": prediction[0]})