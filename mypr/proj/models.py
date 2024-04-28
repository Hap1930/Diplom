
from django.db import models

class SledDate(models.Model):
    date = models.DateField()


class Departments(models.Model):
    departmentid = models.IntegerField(db_column='DepartmentID', primary_key=True, blank=True)  # Field name made lowercase.
    departmentname = models.CharField(db_column='DepartmentName', max_length=100)  # Field name made lowercase.


    def __str__(self):
        return f'{self.departmentid} {self.departmentname}'
    

    class Meta:
        managed = True
        db_table = 'Departments'

class Motherboards(models.Model):
    motherboards_id = models.AutoField(db_column='Motherboards_id',  primary_key=True, blank=True)
    model_motherboards = models.CharField(db_column='Model_motherboards', unique=True, max_length=120)  # Field name made lowercase.
    chipset = models.CharField(db_column='Chipset', max_length=30)  # Field name made lowercase.
    form_factor = models.CharField(db_column='Form_factor', max_length=20)  # Field name made lowercase.
    socket = models.CharField(db_column='Socket', max_length=20)  # Field name made lowercase.
    memory_type = models.CharField(db_column='Memory_type', max_length=20)  # Field name made lowercase.
    count_slots = models.IntegerField(db_column='Count_slots')  # Field name made lowercase.
    max_memory = models.IntegerField(db_column='Max_memory')  # Field name made lowercase.
    rate_memory = models.IntegerField(db_column='Rate_memory')  # Field name made lowercase.
    motherboard_power = models.CharField(db_column='Motherboard_power', max_length=20)  # Field name made lowercase.
    connectors = models.CharField(db_column='Connectors', max_length=450)  # Field name made lowercase.

    def __str__(self):
        return f'{self.model_motherboards}'

    class Meta:
        managed = True
        db_table = 'Motherboards'


class Graphicscards(models.Model):
    graphicscards_id = models.AutoField(db_column='Graphicscards_id',  primary_key=True, blank=True)
    model_graphicscards = models.CharField(db_column='Model_GraphicsCards', unique=True, max_length=120)  # Field name made lowercase.
    video_memory = models.IntegerField(db_column='Video_memory')  # Field name made lowercase.
    type_memory = models.CharField(db_column='Type_memory', max_length=30)  # Field name made lowercase.
    connectors = models.CharField(db_column='Connectors', max_length=450)  # Field name made lowercase.


    def __str__(self):
        return f'{self.model_graphicscards}'
    
    class Meta:
        managed = True
        db_table = 'GraphicsCards'


class Processors(models.Model):
    processors_id = models.AutoField(db_column='processors_id',  primary_key=True, blank=True)
    model_processors = models.CharField(db_column='Model_processors', unique=True, max_length=120)  # Field name made lowercase.
    count_core = models.IntegerField(db_column='Count_core')  # Field name made lowercase.
    clock_rate = models.DecimalField(db_column='Clock_rate', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.



    def __str__(self):
        return f'{self.model_processors}'

    class Meta:
        managed = True
        db_table = 'Processors'


class Rams(models.Model):
    ram_id = models.AutoField(db_column='ram_id',  primary_key=True, blank=True)
    model_ram = models.CharField(db_column='Model_ram', unique=True, max_length=120)  # Field name made lowercase.
    memory_type = models.CharField(db_column='Memory_type', max_length=20)  # Field name made lowercase.
    rate_memory = models.IntegerField(db_column='Rate_memory')  # Field name made lowercase.

    def __str__(self):
        return f'{self.model_ram}'

    class Meta:
        managed = True
        db_table = 'RAMs'


class Software(models.Model):
    # softwareid = models.AutoField(db_column='SoftwareID',  primary_key=True, blank=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=100)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=50)  # Field name made lowercase.
    

    def __str__(self):
        return f'{self.name}'

    class Meta:
        managed = True
        db_table = 'Software'



class Powersupplies(models.Model):
    powersupplies_id = models.AutoField(db_column='powersupplies_id',  primary_key=True, blank=True)
    model_powersupplies = models.CharField(db_column='Model_PowerSupplies', unique=True, max_length=120)  # Field name made lowercase.
    form_factor = models.CharField(db_column='Form_factor', max_length=20)  # Field name made lowercase.
    power_bp = models.IntegerField(db_column='Power_bp')  # Field name made lowercase.

    def __str__(self):
        return f'{self.model_powersupplies}'

    class Meta:
        managed = True
        db_table = 'PowerSupplies'


class Employees(models.Model):
    employeeid = models.AutoField(db_column='EmployeeID', primary_key=True, blank=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50)  # Field name made lowercase.
    departmentid = models.ForeignKey(Departments,  on_delete=models.CASCADE, db_column='DepartmentID')  # Field name made lowercase.
    corpus = models.IntegerField(db_column='Corpus')  # Field name made lowercase.
    office = models.IntegerField(db_column='Office')  # Field name made lowercase.
    post = models.CharField(db_column='Post', max_length=50)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=18)  # Field name made lowercase.
    adress = models.CharField(db_column='Adress', max_length=150)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=40)  # Field name made lowercase.

    def __str__(self):
        return f'{self.employeeid} {self.firstname} {self.lastname}'
    
    class Meta:
        managed = True
        db_table = 'Employees'

class Harddrives(models.Model):
    harddrives_id = models.AutoField(db_column='harddrives_id',  primary_key=True, blank=True)
    model_harddrives = models.CharField(db_column='Model_HardDrives', unique=True, max_length=120)  # Field name made lowercase.
    disk_type = models.CharField(db_column='Disk_type', max_length=30)  # Field name made lowercase.
    space_disk = models.IntegerField(db_column='Space_disk')  # Field name made lowercase.
    speed_disk = models.IntegerField(db_column='Speed_disk')  # Field name made lowercase.

    def __str__(self):
        return f'{self.model_harddrives}'

    class Meta:
        managed = True
        db_table = 'HardDrives'


class Incidenthistory(models.Model):
    
    AUTHOR_CHOICES = [
       ('Компьютер', 'Компьютер'),
       ('Монитор', 'Монитор'),
       ('Принтер', 'Принтер'),
   ]
    incidentid = models.AutoField(db_column='IncidentID', primary_key=True, blank=True)  # Field name made lowercase.
    equipmenttype = models.CharField(db_column='EquipmentType', max_length=10, choices=AUTHOR_CHOICES)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=13)  # Field name made lowercase.
    incidentdate = models.DateTimeField(db_column='IncidentDate', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.


    def __str__(self):
        return f'{self.serialnumber} {self.incidentdate}'

    class Meta:
        managed = True
        db_table = 'IncidentHistory'



class Computers(models.Model):
    # computerid = models.IntegerField(db_column='ComputerID', unique=True,  blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', primary_key=True, max_length=13)  # Field name made lowercase.
    inventory_number = models.CharField(db_column='Inventory_number', max_length=10, unique=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=120)  # Field name made lowercase.
    employeeid = models.ForeignKey(Employees, on_delete=models.CASCADE, db_column='EmployeeID', related_name='computers_set')  # Field name made lowercase.
    ip_adress = models.CharField(db_column='IP_adress', max_length=19, blank=True, null=True)  # Field name made lowercase.
    datу_use = models.DateField(db_column='Datу_use')  # Field name made lowercase.
    status = models.BooleanField(db_column='Status',  default = True)  # Field name made lowercase.
    model_processors = models.ForeignKey(Processors, on_delete=models.CASCADE, db_column='processors_id')  # Field name made lowercase.
    model_motherboards = models.ForeignKey(Motherboards,  on_delete=models.CASCADE, db_column='Motherboards_id')  # Field name made lowercase.
    model_ram = models.ForeignKey(Rams,  models.CASCADE, db_column='ram_id')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    model_harddrives = models.ForeignKey(Harddrives, on_delete=models.CASCADE, db_column='harddrives_id')  # Field name made lowercase.
    second_model_harddrives = models.ForeignKey(Harddrives, on_delete=models.CASCADE, blank=True, null=True, db_column='Second_harddrives_id', related_name='computers_second_model_harddrives_set')  # Field name made lowercase.
    model_powersupplies = models.ForeignKey(Powersupplies, on_delete=models.CASCADE,  db_column='powersupplies_id')  # Field name made lowercase.
    model_graphicscards = models.ForeignKey(Graphicscards, on_delete=models.CASCADE, db_column='Graphicscards_id')  # Field name made lowercase.

    def __str__(self):
        return f'{self.serialnumber}'

    class Meta:
        managed = True
        db_table = 'Computers'

class Computersoftware(models.Model):
    serialnumber = models.ForeignKey(Computers, on_delete=models.CASCADE, db_column='SerialNumber',  max_length=13)  # Field name made lowercase. The composite primary key (SerialNumber, Name) found, that is not supported. The first column is selected.
    name = models.ForeignKey(Software, on_delete=models.CASCADE, db_column='name')  # Field name made lowercase.
    installdate = models.DateField(db_column='InstallDate')  # Field name made lowercase.
    licensekey = models.CharField(db_column='LicenseKey', max_length=50)  # Field name made lowercase.
    
    def __str__(self):
        return f'{self.serialnumber} {self.name}'

    class Meta:
        managed = True
        db_table = 'ComputerSoftware'
        unique_together = (('serialnumber', 'name'),)


class Monitors(models.Model):
    # monitorid = models.IntegerField(db_column='MonitorID', unique=True, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=50)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', primary_key=True, max_length=13)  # Field name made lowercase.
    inventory_number = models.CharField(db_column='Inventory_number',max_length=10, unique = True)  # Field name made lowercase.
    status = models.BooleanField(db_column='Status', default = True)  # Field name made lowercase.
    employeeid = models.ForeignKey(Employees, on_delete=models.CASCADE, db_column='EmployeeID', related_name='monitors_set')  # Field name made lowercase.
    datу_use = models.DateField(db_column='Datу_use')  # Field name made lowercase.
    screen = models.CharField(db_column='Screen', max_length=200)  # Field name made lowercase.
    connectors = models.CharField(db_column='Connectors', max_length=450)  # Field name made lowercase.

    def __str__(self):
        return f'{self.serialnumber}'
    

    class Meta:
        managed = True
        db_table = 'Monitors'




class Printers(models.Model):
    # printerid = models.IntegerField(db_column='PrinterID', unique=True,  blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=120)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', primary_key=True, max_length=13)  # Field name made lowercase.
    inventory_number = models.CharField(db_column='Inventory_number',  max_length=10, unique=True)  # Field name made lowercase.
    status = models.BooleanField(db_column='Status', default = True)  # Field name made lowercase.
    employeeid = models.ForeignKey(Employees, on_delete=models.CASCADE, db_column='EmployeeID', related_name='printers_set')  # Field name made lowercase.
    ip_adress = models.CharField(db_column='IP_adress', max_length=19, blank=True, null=True)  # Field name made lowercase.
    datу_use = models.DateField(db_column='Datу_use')  # Field name made lowercase.
    connectors = models.CharField(db_column='Connectors', max_length=450)  # Field name made lowercase.

    def __str__(self):
        return f'{self.serialnumber}'

    class Meta:
        managed = True
        db_table = 'Printers'


