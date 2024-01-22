import configparser
import mysql.connector
from .Models import ResponseModel

class MySQLHelper():
    CONFIG_PATH = '/dbConfig.ini'

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('dbConfig.ini')
        dbname = 'iparkRight'
        dbinfo = {
            'host': config.get(dbname, 'host'),
            'user': config.get(dbname, 'user'),
            'password': config.get(dbname, 'password'),
            'database': config.get(dbname, 'database')
        }
        self.connstr = dbinfo
        self.dbconn = None

    def dbconnect(self):
        self.dbconn = mysql.connector.connect(
            host=self.connstr['host'],
            user=self.connstr['user'],
            password=self.connstr['password'],
            database=self.connstr['database']
        )
        return self.dbconn.cursor()

    def dbclose(self):
        if self.dbconn:
            self.dbconn.close()

    def queryall(self, sqlqry):
        cursor = self.dbconnect()
        cursor.execute(sqlqry)
        result = self.getdictobjInList(cursor)
        self.dbclose()
        return result

    def queryonerecord(self, sqlqry):
        cursor = self.dbconnect()
        cursor.execute(sqlqry)
        result = self.getdictobjInOneRecord(cursor)
        self.dbclose()
        return result

    def update(self, sqlqry):
        cursor = self.dbconnect()
        cursor.execute(sqlqry)
        self.dbconn.commit()
        self.dbclose()
        return 1

    def update_bulk(self, sqlqry, data_list):
        cursor = self.dbconnect()
        try:
            cursor.executemany(sqlqry, data_list)
            affected_rows = cursor.rowcount  # Get the number of affected rows

            self.dbconn.commit()
            return {"status" : True , "count" : affected_rows}

        except Exception as e:
            self.dbconn.rollback()
            return f"Error: {e}"
        finally:
            self.dbclose()

    def rows(self):
        cursor = self.dbconnect()
        return cursor.rowcount

    def execstoredproc(self, query):
        try:
            cursor = self.dbconnect()
            cursor.execute(query)
            result = self.getdictobj(cursor)
            self.dbclose()
            return result
        except Exception as e:
            print(e)
            return []



    def getdictobjInList(self, cursor):
        columns = [column[0].lower() for column in cursor.description]
        rows = cursor.fetchall()
        if rows:
            if len(rows) == 1 or len(rows) > 1:
                row_dict = [dict(zip(columns, row)) for row in rows]
                response = ResponseModel(message=None, result_data=row_dict, status=True)
            else:
                row_dict = []
                response = ResponseModel(message='No Record Found', result_data=row_dict, status=False)
        else:
            row_dict = []
            response = ResponseModel(message='No Record Found', result_data=row_dict, status=False)

        return response.__dict__

    def getdictobjInOneRecord(self, cursor):
        columns = [column[0].lower() for column in cursor.description]
        rows = cursor.fetchall()
        if rows:
            if len(rows) == 1:
                row_dict = dict(zip(columns, rows[0]))
                response = ResponseModel(message=None, result_data=row_dict, status=True)
            else:
                row_dict = []
                response = ResponseModel(message='No Record Found', result_data=row_dict, status=False)
        else:
            row_dict = []
            response = ResponseModel(message='No Record Found', result_data=row_dict, status=False)

        return response.__dict__

    # def getdictobj(self, cursor):
    #     columns = [column[0].lower() for column in cursor.description]
    #     rows = cursor.fetchall()
    #     if rows:
    #         if len(rows) == 1:
    #             row_dict = dict(zip(columns, rows[0]))
    #             response = ResponseModel(message=None, result_data=row_dict, status=True)
    #         elif len(rows) > 1:
    #             row_dict = [dict(zip(columns, row)) for row in rows]
    #             response = ResponseModel(message=None, result_data=row_dict, status=True)
    #         else:
    #             row_dict = []
    #             response = ResponseModel(message='No Record Found', result_data=row_dict, status=False)
    #     else:
    #         row_dict = []
    #         response = ResponseModel(message='No Record Found', result_data=row_dict, status=False)
    #
    #     return response.__dict__