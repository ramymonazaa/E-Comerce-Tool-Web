from django.http import HttpResponse
from django.shortcuts import render, redirect
from app1.models import category, tool
def homepage(request):
    rows=tool.objects.all().order_by('created_at')
    categories=category.objects.all()
    return render(request, 'index.html',{'rows':rows,'categories':categories})   

# def about(request):
#     # return HttpResponse('about')
#     return render(request, 'about.html')

# def homepage(request):
#         if request.method == 'POST':
#             if request.POST.get('name') and request.POST.get('content'):
#                 manager=manager()
#                 manager.name= request.POST.get('name')
#                 manager.age= request.POST.get('content')
#                 manager.save()
#                 print(request.POST.get('name'))
#                 # print('ssss')
#                 return render(request, 'index.html') 
#             return render(request, 'index.html') 
#         return render(request, 'index.html') 