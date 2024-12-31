from django.contrib import admin
from .models import Customer

# Create a custom admin class for the Customer model
class CustomerAdmin(admin.ModelAdmin):
    # Display the following fields in the list view
    list_display = ('customer_id', 'total_orders', 'total_spent', 'average_order_value', 
                    'days_since_last_purchase', 'churned', 'last_purchase_date')

    # Add search functionality to search by customer_id
    search_fields = ('customer_id', 'total_orders', 'total_spent', 'average_order_value')

    # Add filters for churn status and number of orders
    list_filter = ('churned', 'total_orders')

    # Allow sorting by customer_id, total_spent, and churned status
    ordering = ('customer_id', 'total_spent')

    # Allow the admin to add and edit customer records
    list_editable = ('total_orders', 'total_spent', 'average_order_value', 'days_since_last_purchase', 'churned')

# Register the model and the custom admin class
admin.site.register(Customer, CustomerAdmin)



