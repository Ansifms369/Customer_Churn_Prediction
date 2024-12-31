from django.db import models

class Customer(models.Model):
    customer_id = models.IntegerField(unique=True)
    last_purchase_date = models.DateField()
    total_orders = models.IntegerField()
    total_spent = models.FloatField()
    average_order_value = models.FloatField()
    days_since_last_purchase = models.IntegerField()
    churned = models.BooleanField(default=False)  # Churn prediction result

    def __str__(self):
        return f"Customer {self.customer_id}"


