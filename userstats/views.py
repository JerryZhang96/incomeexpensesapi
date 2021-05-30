from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from expenses.models import Expense
from incomes.models import Income
import datetime

# Create your views here.


class ExpenseSummaryStats(APIView):

    def get_category(self, expense):
        return expense.category

    def get_amount_for_category(self, expense_list, category):
        expenses = expense_list.filter(category=category)
        amount = 0

        for expense in expenses:
            amount += expense.amount

        return {'amount': str(amount)}

    def get(self, request):
        today_date = datetime.date.today()
        a_year_ago = today_date-datetime.timedelta(days=30*12)
        expenses = Expense.objects.filter(
            owner=request.user, date__gte=a_year_ago, date__lte=today_date)

        final = {}
        categories = list(set(map(self.get_category, expenses)))

        for category in categories:
            final[category] = self.get_amount_for_category(
                expenses, category)

        return Response({'data': final}, status=status.HTTP_200_OK)


class IncomeSourcesSummaryStats(APIView):

    def get_source(self, income):
        return income.source

    def get_amount_for_source(self, income_list, source):
        incomes = income_list.filter(source=source)
        amount = 0

        for income in incomes:
            amount += income.amount

        return {'amount': str(amount)}

    def get(self, request):
        today_date = datetime.date.today()
        a_year_ago = today_date-datetime.timedelta(days=30*12)
        incomes = Income.objects.filter(
            owner=request.user, date__gte=a_year_ago, date__lte=today_date)

        final = {}
        sources = list(set(map(self.get_source, incomes)))

        for source in sources:
            final[source] = self.get_amount_for_source(
                incomes, source)

        return Response({'data': final}, status=status.HTTP_200_OK)
