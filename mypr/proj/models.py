# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Computersoftware(models.Model):
    serialnumber = models.OneToOneField('Computers', models.DO_NOTHING, db_column='SerialNumber', primary_key=True)  # Field name made lowercase. The composite primary key (SerialNumber, Name) found, that is not supported. The first column is selected.
    name = models.ForeignKey('Software', models.DO_NOTHING, db_column='Name')  # Field name made lowercase.
    installdate = models.DateField(db_column='InstallDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ComputerSoftware'
        unique_together = (('serialnumber', 'name'),)


class Computers(models.Model):
    computerid = models.IntegerField(db_column='ComputerID', unique=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', primary_key=True, max_length=13)  # Field name made lowercase.
    inventory_number = models.IntegerField(db_column='Inventory_number', unique=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=120)  # Field name made lowercase.
    employeeid = models.ForeignKey('Employees', models.DO_NOTHING, db_column='EmployeeID')  # Field name made lowercase.
    ip_adress = models.CharField(db_column='IP_adress', max_length=19, blank=True, null=True)  # Field name made lowercase.
    datу_use = models.DateField(db_column='Datу_use')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    model_processors = models.ForeignKey('Processors', models.DO_NOTHING, db_column='Model_processors')  # Field name made lowercase.
    model_motherboards = models.ForeignKey('Motherboards', models.DO_NOTHING, db_column='Model_motherboards')  # Field name made lowercase.
    model_ram = models.ForeignKey('Rams', models.DO_NOTHING, db_column='Model_ram')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    model_harddrives = models.ForeignKey('Harddrives', models.DO_NOTHING, db_column='Model_HardDrives')  # Field name made lowercase.
    second_model_harddrives = models.ForeignKey('Harddrives', models.DO_NOTHING, db_column='Second_Model_HardDrives', related_name='computers_second_model_harddrives_set')  # Field name made lowercase.
    model_powersupplies = models.ForeignKey('Powersupplies', models.DO_NOTHING, db_column='Model_PowerSupplies')  # Field name made lowercase.
    model_graphicscards = models.ForeignKey('Graphicscards', models.DO_NOTHING, db_column='Model_GraphicsCards')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Computers'


class Departments(models.Model):
    departmentid = models.AutoField(db_column='DepartmentID', primary_key=True)  # Field name made lowercase.
    departmentname = models.CharField(db_column='DepartmentName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Departments'


class Employees(models.Model):
    employeeid = models.AutoField(db_column='EmployeeID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50)  # Field name made lowercase.
    departmentid = models.ForeignKey(Departments, models.DO_NOTHING, db_column='DepartmentID')  # Field name made lowercase.
    corpus = models.IntegerField(db_column='Corpus')  # Field name made lowercase.
    office = models.IntegerField(db_column='Office')  # Field name made lowercase.
    post = models.CharField(db_column='Post', max_length=50)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=18)  # Field name made lowercase.
    adress = models.CharField(db_column='Adress', max_length=150)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Employees'


class Graphicscards(models.Model):
    model_graphicscards = models.CharField(db_column='Model_GraphicsCards', primary_key=True, max_length=120)  # Field name made lowercase.
    video_memory = models.IntegerField(db_column='Video_memory')  # Field name made lowercase.
    type_memory = models.CharField(db_column='Type_memory', max_length=30)  # Field name made lowercase.
    connectors = models.CharField(db_column='Connectors', max_length=450)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'GraphicsCards'


class Harddrives(models.Model):
    model_harddrives = models.CharField(db_column='Model_HardDrives', primary_key=True, max_length=120)  # Field name made lowercase.
    disk_type = models.CharField(db_column='Disk_type', max_length=30)  # Field name made lowercase.
    space_disk = models.IntegerField(db_column='Space_disk')  # Field name made lowercase.
    speed_disk = models.IntegerField(db_column='Speed_disk')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'HardDrives'


class Incidenthistory(models.Model):
    incidentid = models.AutoField(db_column='IncidentID', primary_key=True)  # Field name made lowercase.
    equipmenttype = models.CharField(db_column='EquipmentType', max_length=9, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=13)  # Field name made lowercase.
    incidentdate = models.DateTimeField(db_column='IncidentDate', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'IncidentHistory'


class Monitors(models.Model):
    monitorid = models.IntegerField(db_column='MonitorID', unique=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=50, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', primary_key=True, max_length=13)  # Field name made lowercase.
    inventory_number = models.IntegerField(db_column='Inventory_number', unique=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    employeeid = models.ForeignKey(Employees, models.DO_NOTHING, db_column='EmployeeID')  # Field name made lowercase.
    datу_use = models.DateField(db_column='Datу_use')  # Field name made lowercase.
    screen = models.CharField(db_column='Screen', max_length=200)  # Field name made lowercase.
    connectors = models.CharField(db_column='Connectors', max_length=450)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Monitors'


class Motherboards(models.Model):
    model_motherboards = models.CharField(db_column='Model_motherboards', primary_key=True, max_length=120)  # Field name made lowercase.
    chipset = models.CharField(db_column='Chipset', max_length=30)  # Field name made lowercase.
    form_factor = models.CharField(db_column='Form_factor', max_length=20)  # Field name made lowercase.
    socket = models.CharField(db_column='Socket', max_length=20)  # Field name made lowercase.
    memory_type = models.CharField(db_column='Memory_type', max_length=20)  # Field name made lowercase.
    count_slots = models.IntegerField(db_column='Count_slots')  # Field name made lowercase.
    max_memory = models.IntegerField(db_column='Max_memory')  # Field name made lowercase.
    rate_memory = models.IntegerField(db_column='Rate_memory')  # Field name made lowercase.
    motherboard_power = models.CharField(db_column='Motherboard_power', max_length=20)  # Field name made lowercase.
    connectors = models.CharField(db_column='Connectors', max_length=450)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Motherboards'


class Powersupplies(models.Model):
    model_powersupplies = models.CharField(db_column='Model_PowerSupplies', primary_key=True, max_length=120)  # Field name made lowercase.
    form_factor = models.CharField(db_column='Form_factor', max_length=20)  # Field name made lowercase.
    power_bp = models.IntegerField(db_column='Power_bp')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PowerSupplies'


class Printers(models.Model):
    printerid = models.IntegerField(db_column='PrinterID', unique=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=120)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', primary_key=True, max_length=50)  # Field name made lowercase.
    inventory_number = models.IntegerField(db_column='Inventory_number', unique=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    employeeid = models.ForeignKey(Employees, models.DO_NOTHING, db_column='EmployeeID')  # Field name made lowercase.
    ip_adress = models.CharField(db_column='IP_adress', max_length=19, blank=True, null=True)  # Field name made lowercase.
    datу_use = models.DateField(db_column='Datу_use')  # Field name made lowercase.
    connectors = models.CharField(db_column='Connectors', max_length=450)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Printers'


class Processors(models.Model):
    model_processors = models.CharField(db_column='Model_processors', primary_key=True, max_length=120)  # Field name made lowercase.
    count_core = models.IntegerField(db_column='Count_core')  # Field name made lowercase.
    clock_rate = models.DecimalField(db_column='Clock_rate', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Processors'


class Rams(models.Model):
    model_ram = models.CharField(db_column='Model_ram', primary_key=True, max_length=120)  # Field name made lowercase.
    memory_type = models.CharField(db_column='Memory_type', max_length=20)  # Field name made lowercase.
    rate_memory = models.IntegerField(db_column='Rate_memory')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'RAMs'


class Software(models.Model):
    softwareid = models.IntegerField(db_column='SoftwareID', unique=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=100)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=50)  # Field name made lowercase.
    licensekey = models.CharField(db_column='LicenseKey', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Software'


