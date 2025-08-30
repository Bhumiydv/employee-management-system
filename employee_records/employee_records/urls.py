"""
URL configuration for employee_records project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from employee.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='home'),
    path('login',login,name='login'),
    path('feedback',feedback,name='feedback'),
    path('admin_dashboard',admin_home,name='admin_home'),
    path('add_employee',add_employee,name='add_employee'),
    path('view_records',view_records,name='view_records'),
    path('edit_records/<int:id>',edit_records,name='edit_records'),
    path('del_records/<int:id>',del_records,name='del_records'),
    path('account',account,name='account'),
    path('logout',Logout,name='logout'),
    path('change_pass',change_pass,name='change_pass'),
    path('search',search,name='search_records'),
    path('search_emp',search_emp,name='search_emp'),
    path('view_feedbacks',view_feedbacks,name='view_feedbacks'),
    path('del_feedbacks/<int:id>',del_feedbacks,name='del_feedbacks'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)