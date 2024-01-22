from HelperClass.sqlhelper import MySQLHelper
from IparkRight.DAL import query

class LoginBL:
    def __init__(self):
        self.sqlhelper = MySQLHelper()

    def Checklogin(self,data):
        exequery = query.loginquary.format(data['username'],data['password'])
        runqry = self.sqlhelper
        rows = runqry.queryonerecord(exequery)
        return rows

    def dbgetdashboardcount(self,superid):
        exequery = query.getdashboadcountquary.format(superid)
        runqry = self.sqlhelper
        rows = runqry.queryonerecord(exequery)
        return rows

    def dbgetdashboardTenantsDetails(self,superid):
        exequery = query.getdashboardTenantsDetailsquary.format(superid)
        runqry = self.sqlhelper
        rows = runqry.queryall(exequery)
        return rows