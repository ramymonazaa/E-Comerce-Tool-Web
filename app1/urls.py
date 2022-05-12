from django.urls import path
#now import the views.py file into this code
from django.conf.urls import url
from app1 import views
urlpatterns=[
#   path('',views.index)
#   path('',views.createpost)
    url(r'insert_tool/',views.insert_tool), 
    url(r'insert_category/',views.insert_category), 
    url(r'show_tool/',views.show_tool), 
    url(r'show_category/',views.show_category), 
    url(r'company/',views.companyPage), 
    url(r'tool/',views.toolPage)
]