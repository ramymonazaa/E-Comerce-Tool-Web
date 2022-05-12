from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
from .models import category, tool
 
def companyPage(request):
        rows=category.objects.all()
        return render(request, 'show_category.html',{'rows':rows})
def toolPage(request):
        rows=tool.objects.all().order_by('created_at')
        return render(request, 'show_tool.html',{'rows':rows})    
    
def category1(request,id_):
        rows=tool.objects.all().filter(category_id=id_).order_by('created_at')
        categories=category.objects.all()
        return render(request, 'index.html',{'rows':rows ,'categories':categories}) 
   
          
def show_category(request):
        return render(request, 'show_category.html')

def show_tool(request):
        return render(request, 'show_tool.html')         
         
def insert_tool(request):
        categories=category.objects.all()
        if request.method == 'POST':
             if request.POST.get('name'):
                Category=category()
                Tool=tool()
                Tool.name= request.POST.get('name')
                Tool.image= "images/"+request.POST.get('image')
                Tool.expiration_date= request.POST.get('expiration_date')
                Tool.price= request.POST.get('price')
                Category.id=request.POST.get('category_selected')
                Tool.category= Category
                Tool.save()
                return render(request, 'insert_tool.html',{'categories':categories})  

        else:
                return render(request,'insert_tool.html',{'categories':categories})
        
        
def insert_category(request):
        if request.method == 'POST':
             if request.POST.get('title') and request.POST.get('category'):
                Category=category()
                Category.name= request.POST.get('name')
                

        else:
                return render(request,'insert_cat.html')
# def index(request):
#   return HttpResponse("Hello Geeks")


# from django.shortcuts import render
# from app1.forms import EntryForm

# def ins(request):
#     form = EntryForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()

#     return render(request, 'homepage/index.html', {'form': form})
