"""
URL configuration for mypr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from proj.views import  generate_pdf_broken_pcs, generate_pdf_department, generate_pdf_office, generate_pdf_pc, generate_pdf_printer, redirect_to_main, report_broken_pcs, report_department, report_office, report_pc, report_printer, search_broken_pcs, search_department, search_office, search_pc, search_printer, view_go, user_login, user_logout, redirect_to_admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", view_go, name="main_page"),
    path("login/", user_login, name="login"),
    path("redirect-to-admin/", redirect_to_admin, name="redirect_to_admin"),
    path("logout/", user_logout, name="logout"),
    path('redirect/main/', redirect_to_main, name='redirect_to_main'),
    path('report/pc/', report_pc, name='report_pc'),
    path('report/pc/generate_pdf', generate_pdf_pc, name='generate_pdf_pc'),
    path('report/printer/', report_printer, name='report_printer'),
    path('report/pc/search_printer', search_printer, name='search_printer'),
    path('report/pc/generate_pdf_printer', generate_pdf_printer, name='generate_pdf_printer'),
    path('report/pc/search_pc', search_pc, name='search_pc'),
    path('report/department/', report_department, name='report_department'),
    path('report/department/search_department', search_department, name='search_department'),
    path('report/department/generate_pdf_department', generate_pdf_department, name='generate_pdf_department'),
    path('report/office/', report_office, name='report_office'),
    path('report/search_office/', search_office, name='search_office'),
    path('report/generate_pdf_office/', generate_pdf_office, name='generate_pdf_office'),
    path('report/broken_pcs/', report_broken_pcs, name='report_broken_pcs'),
    path('report/broken_pcs/search_broken_pcs', search_broken_pcs, name='search_broken_pcs'),
    path('report/broken_pcs/generate_pdf_broken_pcs', generate_pdf_broken_pcs, name='generate_pdf_broken_pcs'),
]
