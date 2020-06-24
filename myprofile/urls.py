from django.urls import path
from django.http import HttpResponse

def top(request):
    return HttpResponse("トップページです")

def resume(request):
    return HttpResponse("職務経歴ページです")

urlpatterns = [
    path('',top),
    path('resume/',resume,),
]