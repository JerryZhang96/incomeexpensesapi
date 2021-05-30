from django.urls import path
from .views import ExpenseSummaryStats, IncomeSourcesSummaryStats

urlpatterns = [
    path('expense-category-data', ExpenseSummaryStats.as_view(),
         name="expense-category-summary"),
    path('income-source-data', IncomeSourcesSummaryStats.as_view(),
         name="income-source-summary")
]
