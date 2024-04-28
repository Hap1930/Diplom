

CREATE TABLE `Computers` (
  `History_id` INT AUTO_INCREMENT,
  `Type_command` ENUM('Удаление', 'Изменение'),
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
  PRIMARY KEY (`History_id`),
  
) ;

CREATE TABLE `Monitors` (
  `History_id` INT AUTO_INCREMENT,
  `Type_command` ENUM('Удаление', 'Изменение'),
  `Model` varchar(50) NOT NULL,
  `SerialNumber` varchar(13) NOT NULL,
  `Inventory_number` varchar(10) NOT NULL,
  `Status` tinyint(1) NOT NULL,
  `Datу_use` date NOT NULL,
  `Screen` varchar(200) NOT NULL,
  `Connectors` varchar(450) NOT NULL,
  `EmployeeID` int NOT NULL,
  PRIMARY KEY (`History_id`),
  
) ;
CREATE TABLE `Printers` (
  `History_id` INT AUTO_INCREMENT,
  `Type_command` ENUM('Удаление', 'Изменение'),
  `Model` varchar(120) NOT NULL,
  `SerialNumber` varchar(13) NOT NULL,
  `Inventory_number` varchar(10) NOT NULL,
  `Status` tinyint(1) NOT NULL,
  `IP_adress` varchar(19) DEFAULT NULL,
  `Datу_use` date NOT NULL,
  `Connectors` varchar(450) NOT NULL,
  `EmployeeID` int NOT NULL,
  PRIMARY KEY (`History_id`),
  
) ;
