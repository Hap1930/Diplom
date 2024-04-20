from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required 
from django.contrib import messages 
from django.shortcuts import redirect 
from django.db.models import Prefetch
from django.views.decorators.cache import cache_control
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


from .models import Computers, Computersoftware, Departments, Employees, Graphicscards, Incidenthistory, Monitors, Motherboards, Powersupplies, Printers, Processors, Rams, Software 



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
            if computer.status:
                computer.status='Рабочий'
            else:
                computer.status='Сломанный'
            global inf0
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
                'status': computer.status,
                'processor_model':computer.model_processors.model_processors,
                'motherboard_model':computer.model_motherboards.model_motherboards,
                'ram_model':computer.model_ram.model_ram,
                'count_slots':computer.quantity,
                'hard_disk_model':computer.model_harddrives.model_harddrives,
                'second_disk_model':computer.second_model_harddrives.model_harddrives,
                'power_supply_model':computer.model_powersupplies.model_powersupplies,
                'graphic_card_model':computer.model_graphicscards.model_graphicscards,
                'software_list1':software.all(),
                'software_list':[software.name for software in software.all()],
                'software_key':[software.licensekey for software in software.all()],
                'software_data':[software.installdate for software in software.all()],
                'software_count': range(software.count()),

            }
            
            print(software.count())
            print(inf0)
            return render(request, 'report_pc.html', inf0)
            # return render(request, 'report_pc.html', inf0)
        else:
            return render(request, 'report_pc.html', {'problem':'Неправильный серийный номер'})
    else:
        return render(request, 'report_pc.html',{'problem':'Неправильный серийный номер'})


@login_required   
def generate_pdf_printer(request):
    print(inf0)
    template_path = 'report_printer.html'  # Путь к вашему шаблону
    context = inf0  # Ваши данные для шаблона

    # Создаем объект HttpResponse с заголовком, указывающим на то, что мы отправляем PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report_printer_'+inf0.get("serial_number")+'.pdf"'

    # Получаем шаблон и рендерим его с данными
    template = get_template(template_path)
    html = template.render(context)

    # Создаем PDF файл
    pisa_status = pisa.CreatePDF(
       html, dest=response)

    # Если PDF создан успешно, то возвращаем его, иначе возвращаем ошибку
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required
def generate_pdf_pc(request):
    print(inf0)
    template_path = 'pc_pdf.html'  # Путь к вашему шаблону
    context = inf0  # Ваши данные для шаблона

    # Создаем объект HttpResponse с заголовком, указывающим на то, что мы отправляем PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report_pc_'+inf0.get("serial_number")+'.pdf"'

    # Получаем шаблон и рендерим его с данными
    template = get_template(template_path)
    html = template.render(context)

    # Создаем PDF файл
    pisa_status = pisa.CreatePDF(
       html, dest=response, encoding="UTF-8")

    # Если PDF создан успешно, то возвращаем его, иначе возвращаем ошибку
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required
def generate_pdf_office(request):
    print(employee_info)
    template_path = 'report_office.html'  # Путь к вашему шаблону
    context = {'employee_info': employee_info}  # Ваши данные для шаблона

    # Создаем объект HttpResponse с заголовком, указывающим на то, что мы отправляем PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report_office_'+office1+'.pdf"'

    # Получаем шаблон и рендерим его с данными
    template = get_template(template_path)
    html = template.render(context)

    # Создаем PDF файл
    pisa_status = pisa.CreatePDF(
       html, dest=response)

    # Если PDF создан успешно, то возвращаем его, иначе возвращаем ошибку
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required
def generate_pdf_department(request):
    print(employee_info)
    template_path = 'report_department.html'  # Путь к вашему шаблону
    context =  {'employee_info': employee_info}  # Ваши данные для шаблона

    # Создаем объект HttpResponse с заголовком, указывающим на то, что мы отправляем PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report_department_'+departmentid1+'.pdf"'

    # Получаем шаблон и рендерим его с данными
    template = get_template(template_path)
    html = template.render(context)

    # Создаем PDF файл
    pisa_status = pisa.CreatePDF(
       html, dest=response)

    # Если PDF создан успешно, то возвращаем его, иначе возвращаем ошибку
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required
def generate_pdf_broken_pcs(request):
    print(serial)
    template_path = 'report_broken_pcs.html'  # Путь к вашему шаблону
    context =  info  # Ваши данные для шаблона

    # Создаем объект HttpResponse с заголовком, указывающим на то, что мы отправляем PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report_incident_'+serial+'.pdf"'

    # Получаем шаблон и рендерим его с данными
    template = get_template(template_path)
    html = template.render(context)

    # Создаем PDF файл
    pisa_status = pisa.CreatePDF(
       html, dest=response)

    # Если PDF создан успешно, то возвращаем его, иначе возвращаем ошибку
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@login_required
def search_printer(request):
    print('3')
    if request.method == 'POST':
        serialnumber1 = request.POST["serial"]
        print(serialnumber1)

        printer = Printers.objects.filter(serialnumber=serialnumber1).prefetch_related(
            Prefetch('employeeid', queryset=Employees.objects.all())
        ).first()

        if printer:
            if printer.status:
                printer.status='Рабочий'
            else:
                printer.status='Сломанный'

            global inf0
            inf0= {
                'serial_number': printer.serialnumber,
                'inventory_number': printer.inventory_number,
                'model': printer.model,
                'employee_firstname':printer.employeeid.firstname,
                'employee_lastname':printer.employeeid.lastname,
                'department_name': printer.employeeid.departmentid,
                'corpus':printer.employeeid.corpus,
                'cabinet':printer.employeeid.office,
                'post':printer.employeeid.post,
                'phone':printer.employeeid.tel,
                'ip_address':printer.ip_adress,
                'date_of_entry':printer.datу_use,
                'status': printer.status,
            }
            
            print(inf0)
            return render(request, 'report_printer.html', inf0)
            # return render(request, 'report_pc.html', inf0)
        else:
            return render(request, 'report_printer.html', {'problem':'Неправильный серийный номер'})
    else:
        return render(request, 'report_printer.html',{'problem':'Неправильный серийный номер'})
    

@login_required
def report_pc(request):
    
    return render(request, 'report_pc.html')

@login_required
def report_printer(request):
    
    return render(request, 'report_printer.html')

@login_required
def report_department(request):
    # Логика для получения данных для отчета по отделу
    # ...
    return render(request, 'report_department.html')

@login_required
def search_department(request):
    if request.method == 'POST':
        global departmentid1
        departmentid1 = request.POST["serial"]
        print(departmentid1)

        try:

            employees = Employees.objects.filter(departmentid=departmentid1).prefetch_related(
                Prefetch('computers_set', queryset=Computers.objects.all()),
                Prefetch('monitors_set', queryset=Monitors.objects.all()),
                Prefetch('printers_set', queryset=Printers.objects.all())
            ).all()
            if employees:

                def status_to_text(status):
                    return "Рабочий" if status else "Сломанный"
                global employee_info
                employee_info = []
                for employee in employees:
                    computers = employee.computers_set.all()
                    monitors = employee.monitors_set.all()
                    printers = employee.printers_set.all()
                    employee_info.append({
                        'employee_firstname':employee.firstname,
                        'employee_lastname':employee.lastname,
                        'department_name': employee.departmentid,
                        'corpus':employee.corpus,
                        'cabinet':employee.office,
                        'post':employee.post,
                        'phone':employee.tel,
                        'computers': [{'serial_number': c.serialnumber, 'inventory_number': c.inventory_number, 'model': c.model, 'ip_address': c.ip_adress, 'status': status_to_text(c.status)} for c in computers],
                        'monitors': [{'serial_number': m.serialnumber, 'inventory_number': m.inventory_number,  'model': m.model, 'status': status_to_text(m.status)} for m in monitors],
                        'printers': [{'serial_number': p.serialnumber, 'inventory_number': p.inventory_number, 'model': p.model, 'ip_address': p.ip_adress, 'status': status_to_text(p.status)} for p in printers],
                })
                    
                print(employee_info)
                    
                
                return render(request, 'report_department.html',  {'employee_info': employee_info})
        except:
            return render(request, 'report_department.html', {'problem':'Неправильный номер отдела'})
        else:
            return render(request, 'report_department.html', {'problem':'Неправильный номер отдела'})
    else:
        return render(request, 'report_department.html',{'problem':'Неправильный номер отдела'})


@login_required
def report_office(request):
    # Логика для получения данных для отчета по кабинету
    # ...
    return render(request, 'report_office.html')

@login_required
def search_office(request):
    if request.method == 'POST':
        global office1
        office1 = request.POST["serial"]
        
        print(office1)

        try:

            employees = Employees.objects.filter(office=office1).prefetch_related(
                Prefetch('computers_set', queryset=Computers.objects.all()),
                Prefetch('monitors_set', queryset=Monitors.objects.all()),
                Prefetch('printers_set', queryset=Printers.objects.all())
            ).all()
            if employees:

                def status_to_text(status):
                    return "Рабочий" if status else "Сломанный"

                global employee_info

                employee_info = []
                for employee in employees:
                    computers = employee.computers_set.all()
                    monitors = employee.monitors_set.all()
                    printers = employee.printers_set.all()
                    employee_info.append({
                        'employee_firstname':employee.firstname,
                        'employee_lastname':employee.lastname,
                        'department_name': employee.departmentid,
                        'corpus':employee.corpus,
                        'cabinet':employee.office,
                        'post':employee.post,
                        'phone':employee.tel,
                        'computers': [{'serial_number': c.serialnumber, 'inventory_number': c.inventory_number, 'model': c.model, 'ip_address': c.ip_adress, 'status': status_to_text(c.status)} for c in computers],
                        'monitors': [{'serial_number': m.serialnumber, 'inventory_number': m.inventory_number,  'model': m.model, 'status': status_to_text(m.status)} for m in monitors],
                        'printers': [{'serial_number': p.serialnumber, 'inventory_number': p.inventory_number, 'model': p.model, 'ip_address': p.ip_adress, 'status': status_to_text(p.status)} for p in printers],
                })
                    
                print(employee_info)
                    
                
                return render(request, 'report_office.html',  {'employee_info': employee_info})
        except:
            return render(request, 'report_office.html', {'problem':'Неправильный номер кабинета'})
        else:
            return render(request, 'report_office.html', {'problem':'Неправильный номер кабинета'})
    else:
        return render(request, 'report_office.html',{'problem':'Неправильный номер кабинета'})
    return render(request, 'report_office.html')

@login_required
def report_broken_pcs(request):
    # Логика для получения данных для отчета по сломанным ПК
    # ...
    return render(request, 'report_broken_pcs.html')


@login_required
def search_broken_pcs(request):
    if request.method == 'POST':
        global serial
        serial = request.POST["serial"]
        print(serial)

        try:

            incident = Incidenthistory.objects.filter(serialnumber=serial).all()
            incidentt = Incidenthistory.objects.filter(serialnumber=serial).first()
            if incident and incidentt:
                global info
                info={
                    'serialnumber':incidentt.serialnumber,
                    'equipmenttype':incidentt.equipmenttype,
                    'inf':incident.all()
                    }

                    
                print(info)
                    
                
                return render(request, 'report_broken_pcs.html',  info)
        except:
            return render(request, 'report_broken_pcs.html', {'problem':'Неправильный серийный номер'})
        else:
            return render(request, 'report_broken_pcs.html', {'problem':'Неправильный серийный номер'})
    else:
        return render(request, 'report_broken_pcs.html',{'problem':'Неправильный серийный номер'})