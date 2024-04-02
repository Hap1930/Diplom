DELIMITER //
CREATE TRIGGER computer_Trigger_update
AFTER UPDATE ON django.Computers FOR EACH ROW
BEGIN
INSERT INTO  `HISTORY`.`History_Computers` (`Type_command`, `SerialNumber`, `Inventory_number`, `Model`, `IP_adress`, `Datу_use`, `Status`, `Quantity`, `EmployeeID`, `Graphicscards_id`, `harddrives_id`, `Second_harddrives_id`, `Motherboards_id`, `powersupplies_id`, `processors_id`, `ram_id`) 
VALUES ('Изменение', old.SerialNumber, old.Inventory_number, old.Model ,  old.IP_adress, old.Datу_use, old.Status, old.Quantity, old.EmployeeID, old.Graphicscards_id, old.harddrives_id, old.Second_harddrives_id, old.Motherboards_id,  old.powersupplies_id, old.processors_id, old.ram_id);
END; //
DELIMITER ;

DELIMITER //
CREATE TRIGGER computer_Trigger_delete
AFTER DELETE ON django.Computers FOR EACH ROW
BEGIN
INSERT INTO  `HISTORY`.`History_Computers` (`Type_command`, `SerialNumber`, `Inventory_number`, `Model`, `IP_adress`, `Datу_use`, `Status`, `Quantity`, `EmployeeID`, `Graphicscards_id`, `harddrives_id`, `Second_harddrives_id`, `Motherboards_id`, `powersupplies_id`, `processors_id`, `ram_id`) 
VALUES ('Удаление', old.SerialNumber, old.Inventory_number, old.Model ,  old.IP_adress, old.Datу_use, old.Status, old.Quantity, old.EmployeeID, old.Graphicscards_id, old.harddrives_id, old.Second_harddrives_id, old.Motherboards_id,  old.powersupplies_id, old.processors_id, old.ram_id);

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
