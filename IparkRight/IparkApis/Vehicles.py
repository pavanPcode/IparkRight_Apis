from flask import Flask, jsonify,json,request,Blueprint
from IparkRight.BL import dbVehicles
from HelperClass.Models import ResponseModel

appVehicle = Blueprint('appVehicle',__name__, url_prefix='/IparkApis/Vehicles')


@appVehicle.route("/getVehicleTypes")
def getVehicleTypes():
    try:
        rcbl = dbVehicles.VehiclesBL()
        retrows = rcbl.dbgetVehicleTypes()
        return jsonify(retrows)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)

@appVehicle.route("/checkResidentMobile")
def checkResidentMobile():
    try:
        Mobile = request.args.get('mobile')
        rcbl = dbVehicles.VehiclesBL()
        retrows = rcbl.dbcheckResidentNumber(Mobile)
        return jsonify(retrows)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)

@appVehicle.route("/getVehiclesByResident")
def getVehiclesByResident():
    try:
        residentid = request.args.get('residentid')
        rcbl = dbVehicles.VehiclesBL()
        retrows = rcbl.dbgetVehiclesByResident(residentid)
        return jsonify(retrows)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)


@appVehicle.route("/registerVehicle",methods = ["POST"])
def registerVehicle():
    try:
        form_data = request.form
        uploaded_file = request.files['vehicleimage']
        rcbl = dbVehicles.VehiclesBL()
        retrows = rcbl.dbcreateVehicle(form_data,uploaded_file)
        return jsonify(retrows.__dict__)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)

@appVehicle.route("/UpdateVehicle",methods = ["POST"])
def UpdateVehicle():
    try:
        form_data = request.form
        uploaded_file = request.files['vehicleimage']
        rcbl = dbVehicles.VehiclesBL()
        retrows = rcbl.dbUpdateVehicle(form_data,uploaded_file)
        return jsonify(retrows.__dict__)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)

@appVehicle.route("/deleteVehicle",methods = ["POST"])
def deleteVehicle():
    try:
        inputdata = request.json
        rcbl = dbVehicles.VehiclesBL()
        retrows = rcbl.dbdeleteVehicle(inputdata)
        return jsonify(retrows.__dict__)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)