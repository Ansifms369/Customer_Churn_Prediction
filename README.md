Customer Churn Prediction

This project is a Django-based application that predicts customer churn based on activity data. The application includes a machine learning model, a REST API for predictions, and an admin panel for managing customer data. The project also features authentication and role-based authorization using JWT.

Features

Machine Learning Model:

Predicts customer churn using features like total orders, total spent, average order value, and days since last purchase.
Includes standard scaling for feature normalization.

Model trained and saved as a .pkl file.

Django Application:

REST API endpoints for making predictions.

Authentication and authorization using JWT.
Admin panel for managing customer records and viewing predictions.

Deployment:

Local deployment using Django’s development server.

Authentication:

Secure access using token-based authentication (JWT).
Role-based access control for API endpoints.
Installation
Prerequisites
Python 3.8 or higher
pip (Python package manager)
Git
Steps

Clone the repository:

git clone https://github.com/Ansifms369/Customer_Churn_Prediction.git
cd Customer_Churn_Prediction

Set up a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install the required dependencies:

pip install -r requirements.txt

Apply database migrations:

python manage.py migrate

Create a superuser for the admin panel:

python manage.py createsuperuser

Start the server:

python manage.py runserver

Access the application:

Home Page: http://127.0.0.1:8000/
Admin Panel: http://127.0.0.1:8000/admin/

Authentication

Obtain a JWT token by logging in at the /api/token/ endpoint with valid credentials.
Use the token to authenticate API requests by including it in the Authorization header:

Authorization: Bearer <your-token>

You can use postman for prediction

Admin Panel
Log in to the admin panel (http://127.0.0.1:8000/admin/) with superuser credentials.
Manage customer records and view predictions.

File Structure

churn/: Django app containing views, models, serializers, and URLs.
static/models/churn_model.pkl: Trained machine learning model.
requirements.txt: List of Python dependencies.
README.md: Documentation for the project.

Evaluation Metrics

Accuracy: Measured the overall correctness of the model.
Precision: Evaluated the proportion of true positives among predicted positives.
Recall: Assessed the ability to detect all actual positives.
F1-score: Harmonic mean of precision and recall.
ROC-AUC: Visualized model performance across different thresholds.

Future Improvements

Make frontend with better design and interactivity.
Deploy the application to a cloud platform for accessibility.
Add support for real-time data processing and streaming predictions.
