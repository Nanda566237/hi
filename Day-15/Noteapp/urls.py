from django.urls import path
from Noteapp import views
from django .contrib.auth import views as ad

urlpatterns =[
    path('',views.home,name="hm"),
    path('abt/',views.about,name="ab"),
    path('con/',views.contact,name="cs"),
    path('lg/',ad.LoginView.as_view(template_name='stc/login.html'),name="log"),
    path('rg/',views.regi,name="rge"),
    path('ds/',views.dashboard,name="dsh"),
    path('lgo/',ad.LoginView.as_view(template_name='stc/logout.html'),name="logo"),
]


