from django.urls import path
from .views import cleaning_companies_list, company_detail

urlpatterns = [
    path('cleaning_companies/', cleaning_companies_list),
    path('cleaning_company/<int:pk>', company_detail)
]