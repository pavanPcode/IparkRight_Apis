from flask import Flask, jsonify,json,request,Blueprint
from IparkRight.BL import dbTenents
from HelperClass.Models import ResponseModel

appOrganization = Blueprint('appOrganization',__name__, url_prefix='/IparkApis/Tenants')


@appOrganization.route("/getTenantslist")
def getTenantslist():
    try:
        superid = request.args.get('superid')
        if superid == None:
            response = ResponseModel(message='provide superid parameter', result_data=[], status=False)
            return jsonify(response.__dict__)
        rcbl = dbTenents.TenentsBL()
        retrows = rcbl.dbgetTenents(superid)
        return jsonify(retrows)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)

@appOrganization.route("/createTenants",methods = ["POST"])
def createTenants():
    try:
        inputdata = request.json
        rcbl = dbTenents.TenentsBL()
        retrows = rcbl.dbcreateTenents(inputdata)
        return jsonify(retrows.__dict__)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)

@appOrganization.route("/updateTenants",methods = ["POST"])
def updateTenants():
    try:
        inputdata = request.json
        rcbl = dbTenents.TenentsBL()
        retrows = rcbl.dbUpdateTenents(inputdata)
        return jsonify(retrows.__dict__)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)

@appOrganization.route("/deleteTenants",methods = ["POST"])
def deleteTenants():
    try:
        inputdata = request.json
        rcbl = dbTenents.TenentsBL()
        retrows = rcbl.dbdeleteTenents(inputdata)
        return jsonify(retrows.__dict__)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)