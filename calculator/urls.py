
from django.urls import path,include
from .views import CalculatorView

urlpatterns = [
    
    path('',CalculatorView,name="calculator"),
]
