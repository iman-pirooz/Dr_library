from django.urls import path , include
from . import views

urlpatterns = [
    path( '' , views.days_list ),
    path ( '<int:day>' , views.day_test_by_number ),
    path ( '<day>' , views.day_test ),
    
]