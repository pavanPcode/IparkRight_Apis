from flask import Flask, jsonify,json,request,Blueprint
from IparkRight.BL import dbreports
from HelperClass.Models import ResponseModel

appReports = Blueprint('appReports',__name__, url_prefix='/IparkApis/Reports')


@appReports.route("/VehicleRegister")
def VehicleRegister():
    try:
        filters = request.args
        rcbl = dbreports.ReportsBL()
        retrows = rcbl.dbVehicleRegister(filters)
        return jsonify(retrows)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)

@appReports.route("/OverstayVehicle")
def OverstayVehicle():
    try:
        rcbl = dbreports.ReportsBL()
        retrows = rcbl.dbOverstayVehicle()
        return jsonify(retrows)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)

@appReports.route("/SlotAllotment")
def SlotAllotment():
    try:
        rcbl = dbreports.ReportsBL()
        retrows = rcbl.dbSlotAllotment()
        return jsonify(retrows)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)

@appReports.route("/VehicleINandOUt")
def VehicleINandOUt():
    try:
        rcbl = dbreports.ReportsBL()
        retrows = rcbl.dbVehicleINandOUt()
        return jsonify(retrows)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)

@appReports.route("/TagInventoryReport")
def TagInventoryReport():
    try:
        rcbl = dbreports.ReportsBL()
        retrows = rcbl.dbTagInventoryReport()
        return jsonify(retrows)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)