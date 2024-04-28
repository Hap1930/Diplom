


CREATE TABLE `ComputerSoftware` (
  `SerialNumber` varchar(13) NOT NULL,
  `InstallDate` date DEFAULT NULL,
  `LicenseKey` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  PRIMARY KEY (`SerialNumber`),
  UNIQUE KEY `ComputerSoftware_SerialNumber_Name_3ea14377_uniq` (`SerialNumber`,`Name`),
  KEY `ComputerSoftware_Name_5859780d_fk_Software_Name` (`Name`),
  CONSTRAINT `ComputerSoftware_Name_5859780d_fk_Software_Name` FOREIGN KEY (`Name`) REFERENCES `Software` (`Name`),
  CONSTRAINT `ComputerSoftware_SerialNumber_b542f044_fk_Computers_SerialNumber` FOREIGN KEY (`SerialNumber`) REFERENCES `Computers` (`SerialNumber`)
) ;



CREATE TABLE `Computers` (
  `SerialNumber` varchar(13) NOT NULL,
  `Inventory_number` varchar(10) NOT NULL,
  `Model` varchar(120) NOT NULL,
  `IP_adress` varchar(19) DEFAULT NULL,
  `Datу_use` date NOT NULL,
  `Status` tinyint(1) NOT NULL,
  `Quantity` int NOT NULL,
  `EmployeeID` int NOT NULL,
  `Model_GraphicsCards` varchar(120) NOT NULL,
  `Model_HardDrives` varchar(120) NOT NULL,
  `Second_Model_HardDrives` varchar(120) NOT NULL,
  `Model_motherboards` varchar(120) NOT NULL,
  `Model_PowerSupplies` varchar(120) NOT NULL,
  `Model_processors` varchar(120) NOT NULL,
  `Model_ram` varchar(120) NOT NULL,
  PRIMARY KEY (`SerialNumber`),
  UNIQUE KEY `Inventory_number` (`Inventory_number`),
  KEY `Computers_EmployeeID_7bd1a392_fk_Employees_EmployeeID` (`EmployeeID`),
  KEY `Computers_Model_GraphicsCards_b2c235aa_fk_GraphicsC` (`Model_GraphicsCards`),
  KEY `Computers_Model_HardDrives_2208efff_fk_HardDrive` (`Model_HardDrives`),
  KEY `Computers_Second_Model_HardDri_caee9421_fk_HardDrive` (`Second_Model_HardDrives`),
  KEY `Computers_Model_motherboards_120c7c97_fk_Motherboa` (`Model_motherboards`),
  KEY `Computers_Model_PowerSupplies_42a1b886_fk_PowerSupp` (`Model_PowerSupplies`),
  KEY `Computers_Model_processors_d5e500d0_fk_Processor` (`Model_processors`),
  KEY `Computers_Model_ram_d85d6420_fk_RAMs_Model_ram` (`Model_ram`),
  CONSTRAINT `Computers_EmployeeID_7bd1a392_fk_Employees_EmployeeID` FOREIGN KEY (`EmployeeID`) REFERENCES `Employees` (`EmployeeID`),
  CONSTRAINT `Computers_Model_GraphicsCards_b2c235aa_fk_GraphicsC` FOREIGN KEY (`Model_GraphicsCards`) REFERENCES `GraphicsCards` (`Model_GraphicsCards`),
  CONSTRAINT `Computers_Model_HardDrives_2208efff_fk_HardDrive` FOREIGN KEY (`Model_HardDrives`) REFERENCES `HardDrives` (`Model_HardDrives`),
  CONSTRAINT `Computers_Model_motherboards_120c7c97_fk_Motherboa` FOREIGN KEY (`Model_motherboards`) REFERENCES `Motherboards` (`Model_motherboards`),
  CONSTRAINT `Computers_Model_PowerSupplies_42a1b886_fk_PowerSupp` FOREIGN KEY (`Model_PowerSupplies`) REFERENCES `PowerSupplies` (`Model_PowerSupplies`),
  CONSTRAINT `Computers_Model_processors_d5e500d0_fk_Processor` FOREIGN KEY (`Model_processors`) REFERENCES `Processors` (`Model_processors`),
  CONSTRAINT `Computers_Model_ram_d85d6420_fk_RAMs_Model_ram` FOREIGN KEY (`Model_ram`) REFERENCES `RAMs` (`Model_ram`),
  CONSTRAINT `Computers_Second_Model_HardDri_caee9421_fk_HardDrive` FOREIGN KEY (`Second_Model_HardDrives`) REFERENCES `HardDrives` (`Model_HardDrives`)
) ;


CREATE TABLE `Departments` (
  `DepartmentID` int NOT NULL,
  `DepartmentName` varchar(100) NOT NULL,
  PRIMARY KEY (`DepartmentID`)
) ;


CREATE TABLE `Employees` (
  `EmployeeID` int NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(50) NOT NULL,
  `LastName` varchar(50) NOT NULL,
  `Corpus` int NOT NULL,
  `Office` int NOT NULL,
  `Post` varchar(50) NOT NULL,
  `Tel` varchar(18) NOT NULL,
  `Adress` varchar(150) NOT NULL,
  `Email` varchar(40) NOT NULL,
  `DepartmentID` int NOT NULL,
  PRIMARY KEY (`EmployeeID`),
  KEY `Employees_DepartmentID_aaaf5d9a_fk_Departments_DepartmentID` (`DepartmentID`),
  CONSTRAINT `Employees_DepartmentID_aaaf5d9a_fk_Departments_DepartmentID` FOREIGN KEY (`DepartmentID`) REFERENCES `Departments` (`DepartmentID`)
) ;

CREATE TABLE `GraphicsCards` (
  `Model_GraphicsCards` varchar(120) NOT NULL,
  `Video_memory` int NOT NULL,
  `Type_memory` varchar(30) NOT NULL,
  `Connectors` varchar(450) NOT NULL,
  PRIMARY KEY (`Model_GraphicsCards`)
) ;


CREATE TABLE `HardDrives` (
  `Model_HardDrives` varchar(120) NOT NULL,
  `Disk_type` varchar(30) NOT NULL,
  `Space_disk` int NOT NULL,
  `Speed_disk` int NOT NULL,
  PRIMARY KEY (`Model_HardDrives`)
) ;


CREATE TABLE `IncidentHistory` (
  `IncidentID` int NOT NULL AUTO_INCREMENT,
  `EquipmentType` varchar(10) NOT NULL,
  `SerialNumber` varchar(13) NOT NULL,
  `IncidentDate` datetime(6) DEFAULT NULL,
  `Description` longtext,
  PRIMARY KEY (`IncidentID`)
) ;


CREATE TABLE `Monitors` (
  `Model` varchar(50) NOT NULL,
  `SerialNumber` varchar(13) NOT NULL,
  `Inventory_number` varchar(10) NOT NULL,
  `Status` tinyint(1) NOT NULL,
  `Datу_use` date NOT NULL,
  `Screen` varchar(200) NOT NULL,
  `Connectors` varchar(450) NOT NULL,
  `EmployeeID` int NOT NULL,
  PRIMARY KEY (`SerialNumber`),
  UNIQUE KEY `Monitors_Inventory_number_0b852671_uniq` (`Inventory_number`),
  KEY `Monitors_EmployeeID_7c56875d_fk_Employees_EmployeeID` (`EmployeeID`),
  CONSTRAINT `Monitors_EmployeeID_7c56875d_fk_Employees_EmployeeID` FOREIGN KEY (`EmployeeID`) REFERENCES `Employees` (`EmployeeID`)
) ;


CREATE TABLE `Motherboards` (
  `Model_motherboards` varchar(120) NOT NULL,
  `Chipset` varchar(30) NOT NULL,
  `Form_factor` varchar(20) NOT NULL,
  `Socket` varchar(20) NOT NULL,
  `Memory_type` varchar(20) NOT NULL,
  `Count_slots` int NOT NULL,
  `Max_memory` int NOT NULL,
  `Rate_memory` int NOT NULL,
  `Motherboard_power` varchar(20) NOT NULL,
  `Connectors` varchar(450) NOT NULL,
  PRIMARY KEY (`Model_motherboards`)
) ;


CREATE TABLE `PowerSupplies` (
  `Model_PowerSupplies` varchar(120) NOT NULL,
  `Form_factor` varchar(20) NOT NULL,
  `Power_bp` int NOT NULL,
  PRIMARY KEY (`Model_PowerSupplies`)
) ;


CREATE TABLE `Printers` (
  `Model` varchar(120) NOT NULL,
  `SerialNumber` varchar(13) NOT NULL,
  `Inventory_number` varchar(10) NOT NULL,
  `Status` tinyint(1) NOT NULL,
  `IP_adress` varchar(19) DEFAULT NULL,
  `Datу_use` date NOT NULL,
  `Connectors` varchar(450) NOT NULL,
  `EmployeeID` int NOT NULL,
  PRIMARY KEY (`SerialNumber`),
  UNIQUE KEY `Inventory_number` (`Inventory_number`),
  KEY `Printers_EmployeeID_ea4865b2_fk_Employees_EmployeeID` (`EmployeeID`),
  CONSTRAINT `Printers_EmployeeID_ea4865b2_fk_Employees_EmployeeID` FOREIGN KEY (`EmployeeID`) REFERENCES `Employees` (`EmployeeID`)
) ;


CREATE TABLE `Processors` (
  `Model_processors` varchar(120) NOT NULL,
  `Count_core` int NOT NULL,
  `Clock_rate` decimal(2,1) DEFAULT NULL,
  PRIMARY KEY (`Model_processors`)
) ;


CREATE TABLE `RAMs` (
  `Model_ram` varchar(120) NOT NULL,
  `Memory_type` varchar(20) NOT NULL,
  `Rate_memory` int NOT NULL,
  PRIMARY KEY (`Model_ram`)
) ;


CREATE TABLE `Software` (
  `Name` varchar(100) NOT NULL,
  `Version` varchar(50) NOT NULL,
  PRIMARY KEY (`Name`)
);

