DELIMITER //
CREATE TRIGGER computer_Trigger_update
AFTER UPDATE ON django.Computers FOR EACH ROW
BEGIN
INSERT INTO  `HISTORY`.`History_Computers` (`Type_command`, `SerialNumber`, `Inventory_number`, `Model`, `IP_adress`, `Datу_use`, `Status`, `Quantity`, `EmployeeID`, `Model_GraphicsCards`, `Model_HardDrives`, `Second_Model_HardDrives`, `Model_motherboards`, `Model_PowerSupplies`, `Model_processors`, `Model_ram`) 
VALUES ('Изменение', old.SerialNumber, old.Inventory_number, old.Model ,  old.IP_adress, old.Datу_use, old.Status, old.Quantity, old.EmployeeID, old.Model_GraphicsCards, old.Model_HardDrives, old.Second_Model_HardDrives, old.Model_motherboards,  old.Model_PowerSupplies, old.Model_processors, old.Model_ram);
END; //
DELIMITER ;

DELIMITER //
CREATE TRIGGER computer_Trigger_delete
AFTER DELETE ON django.Computers FOR EACH ROW
BEGIN
INSERT INTO  `HISTORY`.`History_Computers` (`Type_command`, `SerialNumber`, `Inventory_number`, `Model`, `IP_adress`, `Datу_use`, `Status`, `Quantity`, `EmployeeID`, `Model_GraphicsCards`, `Model_HardDrives`, `Second_Model_HardDrives`, `Model_motherboards`, `Model_PowerSupplies`, `Model_processors`, `Model_ram`) 
VALUES ('Удаление', old.SerialNumber, old.Inventory_number, old.Model ,  old.IP_adress, old.Datу_use, old.Status, old.Quantity, old.EmployeeID, old.Model_GraphicsCards, old.Model_HardDrives, old.Second_Model_HardDrives, old.Model_motherboards,  old.Model_PowerSupplies, old.Model_processors, old.Model_ram);

END; //
DELIMITER ;

DELIMITER //
CREATE TRIGGER printer_Trigger_update
AFTER UPDATE ON django.Printers FOR EACH ROW
BEGIN
INSERT INTO `HISTORY`.`History_Printers` (`Type_command`, `Model`, `SerialNumber`, `Inventory_number`, `Status`, `EmployeeID`, `IP_adress`, `Datу_use`, `Connectors`)
VALUES ('Изменение', old.Model, old.SerialNumber, old.Inventory_number, old.Status, old.EmployeeID, old.IP_adress, old.Datу_use, old.Connectors);
​END; //
DELIMITER ;

DELIMITER //
CREATE TRIGGER printer_Trigger_delete
AFTER DELETE ON django.Printers FOR EACH ROW
BEGIN
INSERT INTO `HISTORY`.`History_Printers` (`Type_command`, `Model`, `SerialNumber`, `Inventory_number`, `Status`, `EmployeeID`, `IP_adress`, `Datу_use`, `Connectors`)
VALUES ('Удаление', old.Model, old.SerialNumber, old.Inventory_number, old.Status, old.EmployeeID, old.IP_adress, old.Datу_use, old.Connectors);
​END; //
DELIMITER ;

DELIMITER //
CREATE TRIGGER monitor_Trigger_update
AFTER UPDATE ON django.Monitors FOR EACH ROW
BEGIN
INSERT INTO `HISTORY`.`History_Monitors` (`Type_command`, `Model`, `SerialNumber`, `Inventory_number`, `Status`, `Datу_use`, `Screen`, `Connectors`, `EmployeeID`) 
VALUES ('Изменение',old.Model, old.SerialNumber, old.Inventory_number, old.Status,  old.Datу_use, old.Screen, old.Connectors, old.EmployeeID);
END; //
DELIMITER ;

DELIMITER //
CREATE TRIGGER monitor_Trigger_delete
AFTER DELETE ON django.Monitors FOR EACH ROW
BEGIN
INSERT INTO `HISTORY`.`History_Monitors` (`Type_command`, `Model`, `SerialNumber`, `Inventory_number`, `Status`, `Datу_use`, `Screen`, `Connectors`, `EmployeeID`) 
VALUES ('Удаление',old.Model, old.SerialNumber, old.Inventory_number, old.Status,  old.Datу_use, old.Screen, old.Connectors, old.EmployeeID);
END; //
DELIMITER ;
