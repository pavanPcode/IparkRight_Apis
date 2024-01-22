from flask import Flask, jsonify,json,request,Blueprint,send_file
from IparkRight.BL import dbResidents
from HelperClass.Models import ResponseModel
import pandas as pd

appResidents = Blueprint('appResidents',__name__, url_prefix='/IparkApis/Residents')


@appResidents.route("/getResidetslist")
def getResidetslist():
    try:
        superid = request.args.get('superid')
        rcbl = dbResidents.ResidentBL()
        retrows = rcbl.dbgetResidetslist(superid)
        return jsonify(retrows)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)

@appResidents.route("/getresidentListbyTenantid")
def getresidentListbyTenantid():
    try:
        tenantid = request.args.get('tenantid')
        rcbl = dbResidents.ResidentBL()
        retrows = rcbl.dbgetresidentListbyTenantid(tenantid)
        return jsonify(retrows)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)

@appResidents.route("/getResidetsdetails")
def getResidetsdetails():
    try:
        residentid = request.args.get('residentid')
        rcbl = dbResidents.ResidentBL()
        retrows = rcbl.dbgetResidetsdetails(residentid)
        return jsonify(retrows)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)

@appResidents.route("/createresidents",methods = ["POST"])
def createresidents():
    try:
        inputdata = request.json
        rcbl = dbResidents.ResidentBL()
        retrows = rcbl.dbcreateresidents(inputdata)
        return jsonify(retrows.__dict__)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)

@appResidents.route("/deleteresidents",methods = ["POST"])
def deleteresidents():
    try:
        inputdata = request.json
        rcbl = dbResidents.ResidentBL()
        retrows = rcbl.dbdeleteresidents(inputdata)
        return jsonify(retrows.__dict__)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)

@appResidents.route("/updateresidents",methods = ["POST"])
def updateresidents():
    try:
        inputdata = request.json
        rcbl = dbResidents.ResidentBL()
        retrows = rcbl.dbupdateresidents(inputdata)
        return jsonify(retrows.__dict__)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)


@appResidents.route('/download_excel', methods=['GET'])
def download_excel():
    # Create a simple DataFrame for demonstration
    data = {'Name' :[], 'Mobile' : [], 'FlatNo' : [], 'BlockNo' : [] , 'Alloted2W':[], 'Alloted4W' :[]
            }
    df = pd.DataFrame(data)

    # Create an Excel file (xlsx format)
    excel_file_path = 'ResidentsBulkCreate.xlsx'
    df.to_excel(excel_file_path, index=False)

    # Return the file for download
    return send_file(excel_file_path, as_attachment=True)



@appResidents.route('/upload_residentsExcel', methods=['POST'])
def upload_excel():
    try:
        file = request.files['file']
        superid = request.form.get('superid')
        tenantid = request.form.get('tenantid')

        if file == None or superid == None or tenantid == None:
            response = ResponseModel(message="Error: File or superid or tenantid not provided", result_data=[], status=False)
            return jsonify(response.__dict__), 400

        rcbl = dbResidents.ResidentBL()
        retrows = rcbl.dbcreateBulkResidents(file,superid,tenantid)
        return jsonify(retrows.__dict__)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

