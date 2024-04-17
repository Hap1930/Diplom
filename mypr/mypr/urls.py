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
from proj.views import redirect_to_main, report_broken_pcs, report_department, report_office, report_pc, search_pc, view_go, user_login, user_logout, redirect_to_admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", view_go, name="main_page"),
    path("login/", user_login, name="login"),
    path("redirect-to-admin/", redirect_to_admin, name="redirect_to_admin"),
    path("logout/", user_logout, name="logout"),
    path('redirect/main/', redirect_to_main, name='redirect_to_main'),
    path('report/pc/', report_pc, name='report_pc'),
    path('search_pc', search_pc, name='search_pc'),
    path('report/department/', report_department, name='report_department'),
    path('report/office/', report_office, name='report_office'),
    path('report/broken_pcs/', report_broken_pcs, name='report_broken_pcs'),
]
