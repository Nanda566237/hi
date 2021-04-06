from django.urls import path
from nandakishore import views

urlpatterns=[
	path('rt',views.home,name="home"),
    path('demo/',views.chk),
    path('hm/',views.homepage),
    path('lg/',views.lgn),
    path('rg/',views.reg,name='register'),
    path('ht/',views.bthm),
    path('about/',views.about,name="about"),
    path('contact',views.about,name="contact")
]