from django.shortcuts import render
# Create your views here.
def show_user_info(request):

    return (request,'user_info/user_info.html')