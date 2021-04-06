from django.urls import path
from Emp import views

urlpatterns=[
    path('',views.home,name="hm"),
    path('abt/',views.about,name="ab"),
    path('co/',views.contact,name="pn"),
    path('log/',views.login,name="hg"),

]
