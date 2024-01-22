from HelperClass.sqlhelper import MySQLHelper
from IparkRight.DAL import reportsquerys

class ReportsBL:
    def __init__(self):
        self.sqlhelper = MySQLHelper()

    def dbVehicleRegister(self,filters):
        if filters.get('tenantid') == '':
            tenantid = 't.id'
        elif filters.get('tenantid') is not None :
            tenantid = filters.get('tenantid')
        else:
            tenantid = 't.id'

        if filters.get('vehicletype') == '':
            vehicletype = 'vt.NoOfWheels'
        elif filters.get('vehicletype') is not None :
            vehicletype = filters.get('vehicletype')
        else:
            vehicletype = 'vt.NoOfWheels'

        if filters.get('residentid') == '':
            residentid = 'r.id'
        elif filters.get('residentid') is not None :
            residentid = filters.get('residentid')
        else:
            residentid = 'r.id'


        exequery = reportsquerys.VehicleRegisterQuary.format(tenantid,vehicletype,residentid)
        print(exequery)
        runqry = self.sqlhelper
        rows = runqry.queryall(exequery)
        return rows

    def dbOverstayVehicle(self):
        exequery = reportsquerys.OverstayVehicleQuary
        runqry = self.sqlhelper
        rows = runqry.queryall(exequery)
        return rows

    def dbSlotAllotment(self):
        exequery = reportsquerys.SlotAllotmentQuary
        runqry = self.sqlhelper
        rows = runqry.queryall(exequery)
        return rows

    def dbVehicleINandOUt(self):
        exequery = reportsquerys.VehicleINandOUtquary
        runqry = self.sqlhelper
        rows = runqry.queryall(exequery)
        return rows

    def dbTagInventoryReport(self):
        exequery = reportsquerys.TagInventoryReportquary
        runqry = self.sqlhelper
        rows = runqry.queryall(exequery)
        return rows