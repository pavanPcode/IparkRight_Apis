getTenentsQuary = """SELECT id,superid,name,code,Alloted2Wheelers,Alloted4Wheelers,DATE_FORMAT(CREATEDON, '%Y-%m-%d %h:%i %p') Registrationdate,phoneno 
FROM tenant where isactive = 1 and superid = {0};"""

createTenentsQuary  = """INSERT INTO tenant (superid, name, code, Alloted2Wheelers, Alloted4Wheelers, CREATEDON, phoneno, isactive)
VALUES ({0}, '{1}', '{2}', {3}, {4}, (UTC_TIMESTAMP() + INTERVAL 330 MINUTE), '{5}', 1);"""

updateTenentsQuary  = """UPDATE tenant SET name = '{1}',code = '{2}',Alloted2Wheelers = {3},Alloted4Wheelers = {4},
    updatedOn = (UTC_TIMESTAMP() + INTERVAL 330 MINUTE),  phoneno = '{5}',superid = {0} 
    WHERE id = {6};
"""

deleteTenentsQuary  = """update tenant set isactive = 0 where id = {0}"""


############################checkResident Number ExistOR Not

checkResidentNoQuary = """ select id Residentid, SuperId,Mobile,name,flatno,blockno,alloted4w,alloted2w from resident where Mobile = '{0}' """

getVehiclesByResidentQuary = """SELECT Id vehicleid, ResidentId, TagNo, VehicleType, RegistrationNumber, VehicleImage
FROM Vehicles WHERE ResidentId = {0} and isactive = 1"""

getVehiclesBysuperidQuary = """SELECT v.Id vehicleid, v.ResidentId, v.TagNo, v.VehicleType, v.RegistrationNumber, v.VehicleImage,r.superid
,
r.name residentname,r.mobile resmobile,t.name tenantname
FROM Vehicles v 
inner join resident r on r.id = v.ResidentId
WHERE  v.isactive = 1 and r.superid = {0}"""

registerVehicleQuary = """INSERT INTO Vehicles (ResidentId, TagNo, VehicleType, RegistrationNumber, VehicleImage)
VALUES ({0}, '{1}', '{2}', '{3}', '{4}'); """

UpdateVehicleQuary = """UPDATE Vehicles SET ResidentId = {0},TagNo = '{1}',     VehicleType = '{2}',     RegistrationNumber = '{3}',     VehicleImage = '{4}'
WHERE id = {5};
"""

deleteVehicleQuary = """UPDATE Vehicles SET  isactive = 0 WHERE id = {0};
"""


loginquary = """SELECT Us.Id AS UserId, RL.Id AS RoleId,US.Name AS UserName,RL.Name AS RoleName,US.IsActive AS UserActive,RL.IsActive AS RoleActive, US.SuperId
FROM Users Us
INNER JOIN  Roles RL ON Us.RoleId = RL.Id
where US.IsActive = 1 and RL.IsActive = 1 and Us.password = '{1}' and Us.Name = '{0}';"""


########################################################Resident############################

createResidentQuary = """INSERT INTO  `resident`
(`SuperId`,`Name`,`Mobile`,`FlatNo`,`BlockNo`,`Alloted2W`,`Alloted4W`,`IsActive`,`CreatedOn`,`tenantid`)
VALUES({0},'{1}','{2}','{3}','{4}','{5}','{6}',1,DATE_ADD(UTC_TIMESTAMP(), INTERVAL '5:30' HOUR_MINUTE),{7});"""

createBulkResidentQuary = """INSERT INTO `resident`
            (`SuperId`,`Name`,`Mobile`,`FlatNo`,`BlockNo`,`Alloted2W`,`Alloted4W`,`IsActive`,`CreatedOn`,`tenantid`)
            VALUES(%s, %s, %s, %s, %s, %s , %s ,1, DATE_ADD(UTC_TIMESTAMP(), INTERVAL '5:30' HOUR_MINUTE), %s)
        """

updateResidentQuary = """UPDATE  `resident`
SET  `SuperId` = {0} , `Name` = '{1}' , `Mobile` = '{2}' , `FlatNo` =  '{3}', `BlockNo` =  '{4}', `Alloted2W` =  '{5}', 
`Alloted4W` = '{6}' , `UpdatedOn` = DATE_ADD(UTC_TIMESTAMP(), INTERVAL '5:30' HOUR_MINUTE),`tenantid` = {8}   WHERE `Id` = {7} ;"""

getresidentListquary = """SELECT r.`Id` residentid, r.`SuperId`,r. `Name`, r.`Mobile`, r.`FlatNo`,r.`BlockNo`, r.`Alloted2W`, r.`Alloted4W`,  r.`CreatedOn`,r.`tenantid`,
DATE_FORMAT(r.`CreatedOn`, '%a, %d %b %Y') AS CreatedOndate,t.name tenantname
FROM  `resident` as r
left join tenant t on t.id = r.tenantid
WHERE r.`SuperId` = {0} and r.`IsActive` = 1;
"""

getresidentListbyTenantidquary = """SELECT r.`Id` residentid, r.`SuperId`,r. `Name`, r.`Mobile`, r.`FlatNo`,r.`BlockNo`, r.`Alloted2W`, r.`Alloted4W`,  r.`CreatedOn`,r.`tenantid`,
DATE_FORMAT(r.`CreatedOn`, '%a, %d %b %Y') AS CreatedOndate,t.name tenantname
FROM  `resident` as r
left join tenant t on t.id = r.tenantid
WHERE r.`Tenantid` = {0} and r.`IsActive` = 1;"""

getresidentdetailsbyidquary = """SELECT r.`Id` residentid, r.`SuperId`,r. `Name`, r.`Mobile`, r.`FlatNo`,r.`BlockNo`, r.`Alloted2W`, r.`Alloted4W`,  r.`CreatedOn`,r.`tenantid`,
DATE_FORMAT(r.`CreatedOn`, '%a, %d %b %Y') AS CreatedOndate,t.name tenantname
FROM  `resident` as r
left join tenant t on t.id = r.tenantid
WHERE r.`Id` = {0};
"""

deleteResidentQuary = """UPDATE  `resident`
SET  `IsActive` = 0    WHERE `Id` = {0} ;"""

########################################################################################################################

getVehicleTypesQuary = """select Name,NoOfWheels from vehicletypes where isactive = 1"""

checkVehSlotesquary = """SELECT
    (SELECT Alloted2W FROM resident WHERE id = {0}) >=
    (SELECT COUNT(*) FROM Vehicles WHERE residentid = {0} AND VehicleType = '{1}' AND isactive = 1) AS comparison_result;"""

getdashboadcountquary = """select count(t.id) tenantscount, sum(alloted2wheelers) + sum(alloted4wheelers) totalslots,sum(alloted2wheelers) twowheelers,sum(alloted4wheelers) fourwheelers
from tenant t where t.superid = {0}"""

getdashboardTenantsDetailsquary = """SELECT
  t.id AS tenantid,
  t.Superid,
  t.name,
  t.phoneno,
  alloted2wheelers - COALESCE((SELECT count(alloted2w) FROM resident WHERE tenantid = t.id), 0) AS AvailableTwoWheelers,

  alloted4wheelers - COALESCE((SELECT count(alloted4w) FROM resident WHERE tenantid = t.id), 0) AS AvailableFourWheelers,
  COALESCE((SELECT count(alloted2w) FROM resident WHERE tenantid = t.id), 0) AS OccupiedTwoWheelers,
  COALESCE((SELECT count(alloted4w) FROM resident WHERE tenantid = t.id), 0) AS OccupiedFourWheels
FROM
  tenant t
WHERE
  t.superid = {0}"""
