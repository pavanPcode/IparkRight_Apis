
from datetime import date,datetime
import calendar
from HelperClass.sqlhelper import MySQLHelper
from IparkRight.DAL import query
from HelperClass.Models import ResponseModel


class TenentsBL:
    def __init__(self):
        self.sqlhelper = MySQLHelper()

    def dbgetTenents(self,superid):

        exequery = query.getTenentsQuary.format(superid)
        runqry = self.sqlhelper
        rows = runqry.queryall(exequery)
        return rows

    def dbcreateTenents(self,data):
        exequery = query.createTenentsQuary.format(data['superid'],data['name'],data['code'],data['alloted2wheelers'],data['alloted4wheelers'],data['phoneno'])
        runqry = self.sqlhelper
        rows = runqry.update(exequery)
        if rows == 1:
            return  ResponseModel(message=None, result_data=[], status=True)
        return ResponseModel(message='Try Again,Something went Wrong', result_data=[], status=True)

    def dbUpdateTenents(self,data):
        exequery = query.updateTenentsQuary.format(data['superid'],data['name'],data['code'],data['alloted2wheelers'],data['alloted4wheelers'],data['phoneno'],data["id"])
        runqry = self.sqlhelper
        rows = runqry.update(exequery)
        if rows == 1:
            return  ResponseModel(message=None, result_data=[], status=True)
        return ResponseModel(message='Try Again,Something went Wrong', result_data=[], status=True)

    def dbdeleteTenents(self,data):
        exequery = query.deleteTenentsQuary.format(data["id"])
        runqry = self.sqlhelper
        rows = runqry.update(exequery)
        if rows == 1:
            return  ResponseModel(message=None, result_data=[], status=True)
        return ResponseModel(message='Try Again,Something went Wrong', result_data=[], status=True)