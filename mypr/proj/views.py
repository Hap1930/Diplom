from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required 
from django.contrib import messages 
from django.shortcuts import redirect 
from django.db.models import Prefetch
from django.views.decorators.cache import cache_control


from .models import Computers, Computersoftware, Departments, Employees, Graphicscards, Monitors, Motherboards, Powersupplies, Printers, Processors, Rams, Software 



@login_required
def view_go(request):
    print(request.user)
    pc_count = Computers.objects.count()
    monitor_count = Monitors.objects.count()
    printer_count = Printers.objects.count()
    employ_count= Employees.objects.count()
    return render(request, "index.html", {'pc_count': pc_count, 'monitor_count': monitor_count,'employ_count':employ_count, 'printer_count': printer_count})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_login(request):
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            
            return redirect("main_page")
        else:
            messages.error(request, 'Неправильный логин или пароль')
        
    return render(request, "login.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_logout(request):
    logout(request)
    return redirect("login")

@login_required
def redirect_to_admin(request):
    return redirect('/admin/')

@login_required
def redirect_to_main(request):
    pc_count = Computers.objects.count()
    monitor_count = Monitors.objects.count()
    printer_count = Printers.objects.count()
    print(pc_count)
    return redirect('main_page')

@login_required
def search_pc(request):
    print('3')
    if request.method == 'POST':
        serialnumber1 = request.POST["serial"]
        print(serialnumber1)

        computer = Computers.objects.filter(serialnumber=serialnumber1).prefetch_related(
            Prefetch('employeeid', queryset=Employees.objects.all()),
            Prefetch('model_motherboards', queryset=Motherboards.objects.all()),
            Prefetch('model_graphicscards', queryset=Graphicscards.objects.all()),
            Prefetch('model_processors', queryset=Processors.objects.all()),
            Prefetch('model_ram', queryset=Rams.objects.all()),
            Prefetch('model_powersupplies', queryset=Powersupplies.objects.all())
        ).first()
        software= Computersoftware.objects.filter(serialnumber=serialnumber1)

        if computer:
            inf0= {
                'serial_number': computer.serialnumber,
                'inventory_number': computer.inventory_number,
                'model': computer.model,
                'employee_firstname':computer.employeeid.firstname,
                'employee_lastname':computer.employeeid.lastname,
                'department_name': computer.employeeid.departmentid,
                'corpus':computer.employeeid.corpus,
                'cabinet':computer.employeeid.office,
                'post':computer.employeeid.post,
                'phone':computer.employeeid.tel,
                'ip_address':computer.ip_adress,
                'date_of_entry':computer.datу_use,
                'status':computer.status,
                'processor_model':computer.model_processors.model_processors,
                'motherboard_model':computer.model_motherboards.model_motherboards,
                'ram_model':computer.model_ram.model_ram,
                'count_slots':computer.quantity,
                'hard_disk_model':computer.model_harddrives.model_harddrives,
                'second_disk_model':computer.second_model_harddrives.model_harddrives,
                'power_supply_model':computer.model_powersupplies.model_powersupplies,
                'graphic_card_model':computer.model_graphicscards.model_graphicscards,
                'software_list':[software.name for software in software.all()],
                'software_key':[software.licensekey for software in software.all()],
                'software_data':[software.installdate for software in software.all()]
            }
            info1={
                'serial_number': str(computer.serialnumber),
                'inventory_number': str(computer.inventory_number),
            }
            print(inf0)
            return JsonResponse(info1)
            # return render(request, 'report_pc.html', inf0)
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')
    

@login_required
def report_pc(request):
    
    return render(request, 'report_pc.html')


@login_required
def report_department(request):
    # Логика для получения данных для отчета по отделу
    # ...
    return render(request, 'report_department.html')

@login_required
def report_office(request):
    # Логика для получения данных для отчета по кабинету
    # ...
    return render(request, 'report_office.html')

@login_required
def report_broken_pcs(request):
    # Логика для получения данных для отчета по сломанным ПК
    # ...
    return render(request, 'report_broken_pcs.html')
