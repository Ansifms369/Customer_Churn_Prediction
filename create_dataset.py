import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate dummy data
np.random.seed(42)
data = {
    "customer_id": [f"CUST{i}" for i in range(1, 101)],
    "last_purchase_date": [datetime.now() - timedelta(days=np.random.randint(1, 365)) for _ in range(100)],
    "total_orders": np.random.randint(1, 50, 100),
    "total_spent": np.random.uniform(50, 5000, 100).round(2),
    "average_order_value": np.random.uniform(10, 200, 100).round(2),
    "days_since_last_purchase": np.random.randint(1, 365, 100),
    "churned": np.random.choice([0, 1], size=100),
}

df = pd.DataFrame(data)
df.to_csv("customer_activity.csv", index=False)
