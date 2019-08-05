from django.shortcuts import render
from .models import Expense
# Create your views here.
def my_expense(request):
    expense=Expense.objects.all()
    context={'expense':expense}
    return (request,'cost/expense.html',context)
