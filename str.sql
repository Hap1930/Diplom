
CREATE TABLE `ComputerSoftware` (
  `SerialNumber` varchar(13) NOT NULL,
  `InstallDate` date NOT NULL,
  `LicenseKey` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`SerialNumber`),
  UNIQUE KEY `ComputerSoftware_SerialNumber_name_30ef75ed_uniq` (`SerialNumber`,`name`),
  KEY `ComputerSoftware_name_de7e98fa_fk_Software_Name` (`name`),
  CONSTRAINT `ComputerSoftware_name_de7e98fa_fk_Software_Name` FOREIGN KEY (`name`) REFERENCES `Software` (`Name`),
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
  `Graphicscards_id` int NOT NULL,
  `harddrives_id` int NOT NULL,
  `Second_harddrives_id` int DEFAULT NULL,
  `Motherboards_id` int NOT NULL,
  `powersupplies_id` int NOT NULL,
  `processors_id` int NOT NULL,
  `ram_id` int NOT NULL,
  PRIMARY KEY (`SerialNumber`),
  UNIQUE KEY `Inventory_number` (`Inventory_number`),
  KEY `Computers_EmployeeID_7bd1a392_fk_Employees_EmployeeID` (`EmployeeID`),
  KEY `Computers_Graphicscards_id_218a684d_fk_GraphicsC` (`Graphicscards_id`),
  KEY `Computers_harddrives_id_bc1c3b4e_fk_HardDrives_harddrives_id` (`harddrives_id`),
  KEY `Computers_Second_harddrives_id_5b1f44b1_fk_HardDrive` (`Second_harddrives_id`),
  KEY `Computers_Motherboards_id_25285230_fk_Motherboa` (`Motherboards_id`),
  KEY `Computers_powersupplies_id_e1421486_fk_PowerSupp` (`powersupplies_id`),
  KEY `Computers_processors_id_f762a378_fk_Processors_processors_id` (`processors_id`),
  KEY `Computers_ram_id_c42d03f0_fk_RAMs_ram_id` (`ram_id`),
  CONSTRAINT `Computers_EmployeeID_7bd1a392_fk_Employees_EmployeeID` FOREIGN KEY (`EmployeeID`) REFERENCES `Employees` (`EmployeeID`),
  CONSTRAINT `Computers_Graphicscards_id_218a684d_fk_GraphicsC` FOREIGN KEY (`Graphicscards_id`) REFERENCES `GraphicsCards` (`Graphicscards_id`),
  CONSTRAINT `Computers_harddrives_id_bc1c3b4e_fk_HardDrives_harddrives_id` FOREIGN KEY (`harddrives_id`) REFERENCES `HardDrives` (`harddrives_id`),
  CONSTRAINT `Computers_Motherboards_id_25285230_fk_Motherboa` FOREIGN KEY (`Motherboards_id`) REFERENCES `Motherboards` (`Motherboards_id`),
  CONSTRAINT `Computers_powersupplies_id_e1421486_fk_PowerSupp` FOREIGN KEY (`powersupplies_id`) REFERENCES `PowerSupplies` (`powersupplies_id`),
  CONSTRAINT `Computers_processors_id_f762a378_fk_Processors_processors_id` FOREIGN KEY (`processors_id`) REFERENCES `Processors` (`processors_id`),
  CONSTRAINT `Computers_ram_id_c42d03f0_fk_RAMs_ram_id` FOREIGN KEY (`ram_id`) REFERENCES `RAMs` (`ram_id`),
  CONSTRAINT `Computers_Second_harddrives_id_5b1f44b1_fk_HardDrive` FOREIGN KEY (`Second_harddrives_id`) REFERENCES `HardDrives` (`harddrives_id`)
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
  `Graphicscards_id` int NOT NULL AUTO_INCREMENT,
  `Model_GraphicsCards` varchar(120) NOT NULL,
  `Video_memory` int NOT NULL,
  `Type_memory` varchar(30) NOT NULL,
  `Connectors` varchar(450) NOT NULL,
  PRIMARY KEY (`Graphicscards_id`),
  UNIQUE KEY `Model_GraphicsCards` (`Model_GraphicsCards`)
) ;


CREATE TABLE `HardDrives` (
  `harddrives_id` int NOT NULL AUTO_INCREMENT,
  `Model_HardDrives` varchar(120) NOT NULL,
  `Disk_type` varchar(30) NOT NULL,
  `Space_disk` int NOT NULL,
  `Speed_disk` int NOT NULL,
  PRIMARY KEY (`harddrives_id`),
  UNIQUE KEY `Model_HardDrives` (`Model_HardDrives`)
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
  UNIQUE KEY `Inventory_number` (`Inventory_number`),
  KEY `Monitors_EmployeeID_7c56875d_fk_Employees_EmployeeID` (`EmployeeID`),
  CONSTRAINT `Monitors_EmployeeID_7c56875d_fk_Employees_EmployeeID` FOREIGN KEY (`EmployeeID`) REFERENCES `Employees` (`EmployeeID`)
) ;

CREATE TABLE `Motherboards` (
  `Motherboards_id` int NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`Motherboards_id`),
  UNIQUE KEY `Model_motherboards` (`Model_motherboards`)
) ;


CREATE TABLE `PowerSupplies` (
  `powersupplies_id` int NOT NULL AUTO_INCREMENT,
  `Model_PowerSupplies` varchar(120) NOT NULL,
  `Form_factor` varchar(20) NOT NULL,
  `Power_bp` int NOT NULL,
  PRIMARY KEY (`powersupplies_id`),
  UNIQUE KEY `Model_PowerSupplies` (`Model_PowerSupplies`)
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
);


CREATE TABLE `Processors` (
  `processors_id` int NOT NULL AUTO_INCREMENT,
  `Model_processors` varchar(120) NOT NULL,
  `Count_core` int NOT NULL,
  `Clock_rate` decimal(2,1) DEFAULT NULL,
  PRIMARY KEY (`processors_id`),
  UNIQUE KEY `Model_processors` (`Model_processors`)
) ;


CREATE TABLE `RAMs` (
  `ram_id` int NOT NULL AUTO_INCREMENT,
  `Model_ram` varchar(120) NOT NULL,
  `Memory_type` varchar(20) NOT NULL,
  `Rate_memory` int NOT NULL,
  PRIMARY KEY (`ram_id`),
  UNIQUE KEY `Model_ram` (`Model_ram`)
) ;


CREATE TABLE `Software` (
  `Name` varchar(100) NOT NULL,
  `Version` varchar(50) NOT NULL,
  PRIMARY KEY (`Name`)
) ;

