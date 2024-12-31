from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    last_purchase_date = serializers.DateField()
    total_orders = serializers.IntegerField()
    total_spent = serializers.FloatField()
    average_order_value = serializers.FloatField()
    days_since_last_purchase = serializers.IntegerField()

