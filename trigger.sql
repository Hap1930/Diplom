DELIMITER //
CREATE TRIGGER computer_Trigger_update
AFTER UPDATE ON djangoo.Computers FOR EACH ROW
BEGIN
INSERT INTO  `djangoo`.`History_Computers` (`Type_command`, `ComputerID`, `SerialNumber`, `Inventory_number`, `Model`, `EmployeeID`, `IP_adress`, `Datу_use`, `Status`, `Model_processors`, `Model_motherboards`, `Model_ram`, `Quantity`, `Model_HardDrives`, `Second_Model_HardDrives`, `Model_PowerSupplies`) 
VALUES ('Изменение', old.ComputerID, old.SerialNumber, old.Inventory_number, old.Model , old.EmployeeID , old.IP_adress, old.Datу_use, old.Status, old.Model_processors , old.Model_ram, old.Quantity, old.Model_HardDrives, old.Second_Model_HardDrives, old.Model_PowerSupplies);
END; //
DELIMITER ;

DELIMITER //
CREATE TRIGGER computer_Trigger_delete
AFTER DELETE ON djangoo.Computers FOR EACH ROW
BEGIN
INSERT INTO  `djangoo`.`History_Computers` (`Type_command`, `ComputerID`, `SerialNumber`, `Inventory_number`, `Model`, `EmployeeID`, `IP_adress`, `Datу_use`, `Status`, `Model_processors`, `Model_motherboards`, `Model_ram`, `Quantity`, `Model_HardDrives`, `Second_Model_HardDrives`, `Model_PowerSupplies`) 
VALUES ('Удаление', old.ComputerID, old.SerialNumber, old.Inventory_number, old.Model , old.EmployeeID , old.IP_adress, old.Datу_use, old.Status, old.Model_processors , old.Model_ram, old.Quantity, old.Model_HardDrives, old.Second_Model_HardDrives, old.Model_PowerSupplies);

END; //
DELIMITER ;

DELIMITER //
CREATE TRIGGER printer_Trigger_update
AFTER UPDATE ON djangoo.Printers FOR EACH ROW
BEGIN
INSERT INTO `djangoo`.`History_Printers` (`Type_command`, `PrinterID`, `Model`, `SerialNumber`, `Inventory_number`, `Status`, `EmployeeID`, `IP_adress`, `Datу_use`)
 VALUES ('Изменение', old.PrinterID, old.Model, old.SerialNumber, old.Inventory_number, old.Status, old.EmployeeID, old.IP_adress, old.Datу_use);
​END; //
DELIMITER ;

DELIMITER //
CREATE TRIGGER printer_Trigger_delete
AFTER DELETE ON djangoo.Printers FOR EACH ROW
BEGIN
INSERT INTO `djangoo`.`History_Printers` (`Type_command`, `PrinterID`, `Model`, `SerialNumber`, `Inventory_number`, `Status`, `EmployeeID`, `IP_adress`, `Datу_use`)
 VALUES ('Удаление', old.PrinterID, old.Model, old.SerialNumber, old.Inventory_number, old.Status, old.EmployeeID, old.IP_adress, old.Datу_use);
​END; //
DELIMITER ;

DELIMITER //
CREATE TRIGGER monitor_Trigger_update
AFTER UPDATE ON djangoo.Monitors FOR EACH ROW
BEGIN
INSERT INTO `djangoo`.`History_Monitors` (`Type_command`, `MonitorID`, `Model`, `SerialNumber`, `Inventory_number`, `Status`, `EmployeeID`, `Datу_use`, `Screen`) 
VALUES ('Изменение', old.MonitorID, old.Model, old.SerialNumber, old.Inventory_number, old.Status, old.EmployeeID, old.Datу_use, old.Screen);
END; //
DELIMITER ;

DELIMITER //
CREATE TRIGGER monitor_Trigger_delete
AFTER DELETE ON djangoo.Monitors FOR EACH ROW
BEGIN
INSERT INTO `djangoo`.`History_Monitors` (`Type_command`, `MonitorID`, `Model`, `SerialNumber`, `Inventory_number`, `Status`, `EmployeeID`, `Datу_use`, `Screen`) 
VALUES ('Удаление', old.MonitorID, old.Model, old.SerialNumber, old.Inventory_number, old.Status, old.EmployeeID, old.Datу_use, old.Screen);
END; //
DELIMITER ;
