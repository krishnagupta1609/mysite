from django.shortcuts import render
from django.http import request,response




def resume(request):

    return render(request,"srt-resume.html")
