from HelperClass.sqlhelper import MySQLHelper
from IparkRight.DAL import query
from HelperClass.Models import ResponseModel

class VehiclesBL:
    def __init__(self):
        self.sqlhelper = MySQLHelper()


    def dbcheckResidentNumber(self,Mobile):
        clean_number = ''.join(c for c in str(Mobile) if c.isdigit())
        # Check if the cleaned number has exactly 10 digits
        if len(clean_number) == 10:

            exequery = query.checkResidentNoQuary.format(Mobile)

            runqry = self.sqlhelper
            rows = runqry.queryonerecord(exequery)
            return rows
        return ResponseModel(message='Enter Valid Mobile Number', result_data=[], status=True)

    def dbgetVehiclesByResident(self,residentid):
        exequery = query.getVehiclesByResidentQuary.format(residentid)
        runqry = self.sqlhelper
        rows = runqry.queryall(exequery)
        return rows

    def dbgetVehicleTypes(self):
        exequery = query.getVehicleTypesQuary
        runqry = self.sqlhelper
        rows = runqry.queryall(exequery)
        return rows

    def dbcreateVehicle(self,form_data,uploaded_file):
        print(form_data,uploaded_file)

        checkslots = query.checkVehSlotesquary.format(form_data.get('residentid'),form_data.get('vehicletype'))
        runcheckqry = self.sqlhelper
        checkrows = runcheckqry.queryonerecord(checkslots)

        if checkrows['Status'] == False:
            return ResponseModel(message='Try Again,Something went Wrong', result_data=[], status=True)

        elif  int(checkrows['ResultData']['comparison_result']) == 0:
            return ResponseModel(message='Your parking Slot limit Reached', result_data=[], status=True)

        exequery = query.registerVehicleQuary.format(form_data.get('residentid'),form_data.get('tagno'),form_data.get('vehicletype'),form_data.get('registrationnumber'),form_data.get('vehicleimage'))
        runqry = self.sqlhelper
        rows = runqry.update(exequery)
        if rows == 1:
            return ResponseModel(message=None, result_data=[], status=True)
        return ResponseModel(message='Try Again,Something went Wrong', result_data=[], status=True)

    def dbUpdateVehicle(self,form_data,uploaded_file):
        exequery = query.UpdateVehicleQuary.format(form_data.get('residentid'),form_data.get('tagno'),form_data.get('vehicletype'),form_data.get('registrationnumber'),form_data.get('vehicleimage'),form_data.get('vehicleid'))
        runqry = self.sqlhelper
        rows = runqry.update(exequery)

        if rows == 1:
            return ResponseModel(message=None, result_data=[], status=True)
        return ResponseModel(message='Try Again,Something went Wrong', result_data=[], status=True)

    def dbdeleteVehicle(self,data):
        exequery = query.deleteVehicleQuary.format(data['vehicleid'])
        runqry = self.sqlhelper
        rows = runqry.update(exequery)
        if rows == 1:
            return ResponseModel(message=None, result_data=[], status=True)
        return ResponseModel(message='Try Again,Something went Wrong', result_data=[], status=True)


