"""Forus_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Forus_Webapp.views import *
from Forus_Webapp.views import ListUsers, CustomAuthToken

urlpatterns = [
    path('api/users/', ListUsers.as_view()),
    path('api/token/auth/', CustomAuthToken.as_view()),
    path('admin/', admin.site.urls),
    path("",index),
    path('index',index),
    path('indexd',indexd),
    path('admin_log',admin2),
    path('logout',logout),
    path('dash1',dash1),
    path('dash2',dash2),
    path('reg',reg),
    path('login12',login12),
    path('reg3',reg3),
    path('ClassicR1',classic),
    path('classichd',classichd),
    path('classic64',classic64),
    path('flora',flora),
    path('Aberro',Aberro),
    path('Neo',Neo),
    path('cbin',cbin),
    path('Bin_info',Bin_info),
    path('cbin2',cbin2),
    path('dash3',dash3),
    path('dash4',dash4),
    path('d',d),
    path('productedit',productedit),
    path('bincard',bincard),
    path('viewdata',viewdata),
    path('editdata<int:pk>',editdata),
    path('editform',editform),
    # path('edelete<int:binid>',edelete),
    path('index1',index1),
    path('FG',FG),
    path('addfg',addfg),
    path('recedit<int:pk1>',recedit),
    path('recstock',recstock),
    path('Issuededit<int:pk2>',Issuededit),
    path('recstockaad',recstockaad),
    path('addissue',addissue),
    path('Issued',Issued),
    path('adbin<int:pk>',adbin),
    path('newitem<int:pki>',newitem),
    path('Classic6_4R2',Classic6_4R2),
    path('ClassicHDR2',ClassicHDR2),
    path('ClassicR2',ClassicR2),
    path('ClassicR3',ClassicR3),
    path('Classic6_4R3',Classic6_4R3),
    path('ClassicHDR3',ClassicHDR3),
    path('Flora1',Flora1),
    path('Flora2',Flora2),
    path('Aberro1',Aberro1),
    path('Aberro2',Aberro2),
    path('Neo1',Neo1),
    path('Neo2',Neo2),
    path('Neohd',Neohd), 
    path('Neohd1',Neohd1), 
    path('Neohd2',Neohd2),  
    path('device_datalist',device_datalist), 
    path('ddelete<int:did>',ddelete),
    path('FGslider',FGslider), 
    path('slider',slider), 
    path('TVslider',TVslider),
    path('mobile_slider',mobile_slider),
   
    
    
]
