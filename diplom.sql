CREATE DATABASE IF NOT EXISTS IT_Inventory;
USE IT_Inventory;

CREATE TABLE IF NOT EXISTS Departments (
    DepartmentID INT AUTO_INCREMENT,
    DepartmentName VARCHAR(100) NOT NULL,
    PRIMARY KEY (DepartmentID)
);

CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DepartmentID INT NOT NULL,
    Corpus INT NOT NULL,
    Office INT NOT NULL,
    Post VARCHAR(50) NOT NULL,
    Tel VARCHAR(18) NOT NULL,
    Adress VARCHAR(150) NOT NULL,
    Email VARCHAR(40) NOT NULL,
    PRIMARY KEY (EmployeeID),
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Processors (
    Model_processors VARCHAR(120) NOT NULL,
    Count_core INT NOT NULL,
    Clock_rate DECIMAL(2,1),
    PRIMARY KEY (Model_processors)
);

CREATE TABLE IF NOT EXISTS Motherboards (
	Model_motherboards VARCHAR(120) NOT NULL,
    Chipset VARCHAR(30) NOT NULL,
    Form_factor VARCHAR(20) NOT NULL,
    Socket VARCHAR(20) NOT NULL,
    Memory_type VARCHAR(20) NOT NULL,
    Count_slots INT NOT NULL,
    Max_memory INT NOT NULL,
    Rate_memory INT NOT NULL,
    Motherboard_power VARCHAR(20) NOT NULL,
    Connectors VARCHAR(450) NOT NULL,
    PRIMARY KEY (Model_motherboards)
);

CREATE TABLE IF NOT EXISTS RAMs (
    Model_ram VARCHAR(120) NOT NULL,
    Memory_type VARCHAR(20) NOT NULL,
    Rate_memory INT NOT NULL,
    PRIMARY KEY (Model_ram)
);

CREATE TABLE IF NOT EXISTS HardDrives (
    Model_HardDrives VARCHAR(120) NOT NULL,
    Disk_type VARCHAR(30) NOT NULL,
    Space_disk INT NOT NULL,
    Speed_disk INT NOT NULL,
    PRIMARY KEY (Model_HardDrives)
);

CREATE TABLE IF NOT EXISTS PowerSupplies (
    Model_PowerSupplies VARCHAR(120) NOT NULL,
	Form_factor VARCHAR(20) NOT NULL,
    Power_bp INT NOT NULL, 
    PRIMARY KEY (Model_PowerSupplies)
);

CREATE TABLE IF NOT EXISTS GraphicsCards (
    Model_GraphicsCards VARCHAR(120) NOT NULL,
    Video_memory INT NOT NULL, 
    Type_memory VARCHAR(30) NOT NULL,
    Connectors VARCHAR(450) NOT NULL,
    PRIMARY KEY (Model_GraphicsCards)
);


CREATE TABLE IF NOT EXISTS Computers (
    ComputerID INT AUTO_INCREMENT UNIQUE,
    SerialNumber VARCHAR(13) NOT NULL,
    Inventory_number INT  UNIQUE NOT NULL,
    Model VARCHAR(120) NOT NULL,
    EmployeeID INT NOT NULL,
    IP_adress VARCHAR(19),
    Datу_use DATE NOT NULL default(curdate()),
	Status BOOLEAN DEFAULT(TRUE),
    Model_processors VARCHAR(120) NOT NULL,
	Model_motherboards VARCHAR(120) NOT NULL,
    Model_ram VARCHAR(120) NOT NULL,
    Quantity INT NOT NULL,
    Model_HardDrives VARCHAR(120) NOT NULL,
    Second_Model_HardDrives VARCHAR(120) NOT NULL,
    Model_PowerSupplies VARCHAR(120) NOT NULL,
    Model_GraphicsCards VARCHAR(120) NOT NULL,
    PRIMARY KEY (SerialNumber),
    FOREIGN KEY (Model_processors) REFERENCES Processors(Model_processors) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (Model_motherboards) REFERENCES Motherboards(Model_motherboards) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (Model_ram) REFERENCES RAMs(Model_ram) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (Model_HardDrives) REFERENCES HardDrives(Model_HardDrives) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (Second_Model_HardDrives) REFERENCES HardDrives(Model_HardDrives) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (Model_PowerSupplies) REFERENCES PowerSupplies(Model_PowerSupplies) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (Model_GraphicsCards) REFERENCES GraphicsCards(Model_GraphicsCards) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Monitors (
    MonitorID INT AUTO_INCREMENT UNIQUE,
    Model VARCHAR(50),
    SerialNumber VARCHAR(13) NOT NULL,
    Inventory_number INT  UNIQUE NOT NULL,
    Status BOOLEAN DEFAULT(TRUE),
    EmployeeID INT NOT NULL,
    Datу_use DATE NOT NULL default(curdate()),
    Screen VARCHAR(200) NOT NULL,
    Connectors VARCHAR(450) NOT NULL,
    PRIMARY KEY (SerialNumber),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

CREATE TABLE IF NOT EXISTS Printers (
    PrinterID INT AUTO_INCREMENT UNIQUE,
    Model VARCHAR(120) NOT NULL,
    SerialNumber VARCHAR(50) NOT NULL,
    Inventory_number INT  UNIQUE NOT NULL,
    Status BOOLEAN DEFAULT(TRUE),
    EmployeeID INT NOT NULL,
    IP_adress VARCHAR(19),
	Datу_use DATE NOT NULL default(curdate()),
    Connectors VARCHAR(450) NOT NULL,
    PRIMARY KEY (SerialNumber),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

CREATE TABLE IF NOT EXISTS Software (
    SoftwareID INT AUTO_INCREMENT UNIQUE,
    Name VARCHAR(100) NOT NULL,
    Version VARCHAR(50) NOT NULL,
    LicenseKey VARCHAR(50) NOT NULL,
    PRIMARY KEY (Name)
);

CREATE TABLE IF NOT EXISTS ComputerSoftware (
    SerialNumber VARCHAR(13) NOT NULL,
    Name VARCHAR(100) NOT NULL,
    InstallDate DATE default(curdate()),
    PRIMARY KEY (SerialNumber, Name),
    FOREIGN KEY (SerialNumber) REFERENCES Computers(SerialNumber),
    FOREIGN KEY (Name) REFERENCES Software(Name)
);




CREATE TABLE IF NOT EXISTS IncidentHistory (
    IncidentID INT AUTO_INCREMENT,
    EquipmentType ENUM('Компьютер', 'Монитор', 'Принтер'), -- Добавляем ENUM для типа оборудования
    SerialNumber VARCHAR(13) NOT NULL, -- ID оборудования, с которым связано происшествие
    IncidentDate DATETIME default(current_time()), 
    Description TEXT,
    PRIMARY KEY (IncidentID)
);




