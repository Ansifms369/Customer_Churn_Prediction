from django.urls import path
from churn.views import HomeView, ChurnPredictionAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login endpoint
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', HomeView.as_view(), name='home'),  # Home page
    path('predict/', ChurnPredictionAPIView.as_view(), name='predict'),  # API for churn prediction
]
