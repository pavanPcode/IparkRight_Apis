
from HelperClass.sqlhelper import MySQLHelper
from IparkRight.DAL import query
from HelperClass.Models import ResponseModel
import pandas as pd

class ResidentBL:
    def __init__(self):
        self.sqlhelper = MySQLHelper()

    def dbgetResidetslist(self,superid):
        exequery = query.getresidentListquary.format(superid)
        runqry = self.sqlhelper
        rows = runqry.queryall(exequery)
        return rows

    def dbgetresidentListbyTenantid(self,tenantid):
        exequery = query.getresidentListbyTenantidquary.format(tenantid)
        runqry = self.sqlhelper
        rows = runqry.queryall(exequery)
        return rows

    def dbgetResidetsdetails(self,id):
        exequery = query.getresidentdetailsbyidquary.format(id)
        runqry = self.sqlhelper
        rows = runqry.queryonerecord(exequery)
        return rows

    def dbcreateresidents(self,data):

        try:
            alloted2w = int(data.get('alloted2w', 1))
        except ValueError:
            alloted2w = 1

        try:
            alloted4w = int(data.get('alloted4w', 1))
        except ValueError:
            alloted4w = 1


        print(data)
        exequery = query.createResidentQuary.format(data['superid'],data['name'],data['mobile'],data['flatno'],data['blockno'],alloted2w,alloted4w,data['tenantid'])
        runqry = self.sqlhelper
        print(exequery)
        rows = runqry.update(exequery)
        if rows == 1:
            return  ResponseModel(message=None, result_data=[], status=True)
        return ResponseModel(message='Try Again,Something went Wrong', result_data=[], status=True)

    def dbupdateresidents(self,data):
        try:
            alloted2w = int(data.get('alloted2w', 1))
        except ValueError:
            alloted2w = 1

        try:
            alloted4w = int(data.get('alloted4w', 1))
        except ValueError:
            alloted4w = 1

        exequery = query.updateResidentQuary.format(data['superid'],data['name'],data['mobile'],data['flatno'],data['blockno'],alloted2w,alloted4w,data['residentid'],data['tenantid'])
        runqry = self.sqlhelper
        print(exequery)
        rows = runqry.update(exequery)
        if rows == 1:
            return  ResponseModel(message=None, result_data=[], status=True)
        return ResponseModel(message='Try Again,Something went Wrong', result_data=[], status=True)

    def dbdeleteresidents(self,data):
        exequery = query.deleteResidentQuary.format(data['residentid'])
        runqry = self.sqlhelper
        rows = runqry.update(exequery)
        if rows == 1:
            return  ResponseModel(message=None, result_data=[], status=True)
        return ResponseModel(message='Try Again,Something went Wrong', result_data=[], status=True)


    def dbcreateBulkResidents(self, file,superid,tenantid):
        try:
            if file and file.filename.endswith('.xlsx'):
                # Read Excel file into a DataFrame
                df = pd.read_excel(file)

                data_list = []
                for _, row in df.iterrows():
                    print(row)

                    try:
                        print(row.get('Alloted2W'))
                        alloted_2w_value = int(row.get('Alloted2W', 1))
                    except ValueError:
                        alloted_2w_value = 1

                    try:
                        print(row.get('Alloted4W'))
                        alloted_4w_value = int(row.get('Alloted4W', 1))
                    except ValueError:
                        alloted_4w_value = 1

                    data_list.append((superid, row['Name'], row['Mobile'], row['FlatNo'], row['BlockNo'],
                                      alloted_2w_value,alloted_4w_value,tenantid))

                exequery = query.createBulkResidentQuary
                runqry = self.sqlhelper
                print(data_list)
                rows = runqry.update_bulk(exequery,data_list)
                print(rows)
                if rows == 1:
                    return ResponseModel(message=None, result_data=[], status=True)
                return ResponseModel(message= f'Try Again,Something went Wrong : {rows}', result_data=[], status=True)
            else:
                return ResponseModel(message="Invalid file format. Please upload a valid Excel file.",result_data=[],status=False )

        except Exception as e:
            print(f"Error: {e}")
            return ResponseModel(message="An error occurred during bulk insertion.",result_data=[],status=False)
