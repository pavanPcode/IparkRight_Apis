VehicleRegisterQuary = """select t.name TenantName,t.id tenantid,r.name residentname,r.mobile residentmobile,r.id ResidentId,v.RegistrationNumber,vt.name VehicleTypename,v.VehicleType
from vehicles v
inner join resident r on r.id = v.ResidentId
inner join tenant t on t.id = r.tenantid 
inner join vehicletypes vt on vt.NoOfWheels = v.Vehicletype
where v.IsActive = 1 and t.id = {0} and r.id = {2} and vt.NoOfWheels = {1}"""

OverstayVehicleQuary = """ SELECT
    tnt.Name AS Tenant,
    Reg.MemberName,
    Reg.VehicleNumber,
    vt.Name AS VehicleType,
    vt.ModelName AS VehicleModel,
    DATE_FORMAT(sw.DateOfTransaction, '%d/%m/%Y') AS Date,
    TIME_FORMAT(sw.InTime, '%H:%i') AS InTime,
    TIME_FORMAT(sw.OutTime, '%H:%i') AS OutTime
FROM
    iparkright.Tenant tnt
INNER JOIN
    iparkright.Registrations Reg ON Reg.TenantId = tnt.Id
INNER JOIN
    iparkright.VehicleTypes vt ON vt.Id = Reg.VehicleTypeId
INNER JOIN
    iparkright.SwipeTransactions sw ON sw.CardId = Reg.CardId AND sw.OutTime IS NULL
WHERE
    tnt.Name = tnt.Name;
"""

SlotAllotmentQuary = """SELECT
    tnt.Name AS Organization,
    tnt.Code AS OrgCode,
    tnt.Alloted2Wheelers AS `2WAlloted`,
    tnt.Alloted4Wheelers AS `4WAlloted`
FROM
    iparkright.Tenant tnt
INNER JOIN
    iparkright.Tenant reg ON reg.Id = tnt.Id;
"""

VehicleINandOUtquary = """SELECT
    tnt.Name AS TenantName,
    reg.VehicleNumber,
    reg.MemberName,
    vt.Name AS VehicleType,
    vt.ModelName AS VehicleModel,
    DATE_FORMAT(sw.DateOfTransaction, '%Y-%m-%d') AS Date,
    TIME_FORMAT(sw.InTime, '%H:%i') AS InTime,
    TIME_FORMAT(sw.OutTime, '%H:%i') AS OutTime
FROM
    iparkright.Tenant tnt
INNER JOIN
    iparkright.Registrations reg ON reg.TenantId = tnt.Id
INNER JOIN
    iparkright.VehicleTypes vt ON vt.Id = reg.VehicleTypeId
INNER JOIN
    iparkright.SwipeTransactions sw ON sw.CardId = reg.CardId;
"""

TagInventoryReportquary = """SELECT
    REG.TagId AS `Card No`,
    CASE
        WHEN REG.Allocated = 1 THEN 'Allocated'
        ELSE 'Not Allocated'
    END AS `Is Allocated`,
    CONCAT(DATE_FORMAT(REG.CreatedOn, '%d/%m/%Y'), TIME_FORMAT(REG.CreatedOn, '%H:%i')) AS `Date Of Transaction`,
    CASE
        WHEN REG.IsTwoWheeler = 1 THEN '2 Wheeler'
        ELSE '4 Wheeler'
    END AS `Vehicle Type`
FROM
    iparkright.CardInventorytags REG; """