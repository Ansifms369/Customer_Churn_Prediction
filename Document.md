Approach

Data Preparation:

Created a synthetic dataset with customer activity data.
Scaled features using StandardScaler for optimal model performance. Model Development:

Used Logistic Regression, Random Forest, Decision Tree, Gradient Boosting, Support Vector Machine (SVM), XGBoost for churn prediction.

Implemented hyperparameter tuning

Evaluated using accuracy, precision, recall, F1-score, ROC-AUC

Django Integration:

Integrated the ML model with Django views and APIs. Implemented authentication and admin panel functionalities.

Assumptions

The churn_model.pkl file is pre-trained and saved in the correct directory.

Challenges

Handling edge cases in input data validation. 
Integrating machine learning with Django REST Framework. 
Ensuring secure authentication and role-based access control.