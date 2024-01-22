from flask import Flask, jsonify,json,request,Blueprint
from IparkRight.BL import dblogin
from HelperClass.Models import ResponseModel
import requests

appLogin = Blueprint('appLogin',__name__, url_prefix='/IparkApis/login')


@appLogin.route("/signIn",methods = ['POST'])
def logincheck():
    try:
        inputdata = request.json
        rcbl = dblogin.LoginBL()
        retrows = rcbl.Checklogin(inputdata)
        return jsonify(retrows)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)

@appLogin.route("/getdashboardcount")
def getdashboardcount():
    try:
        superid = request.args.get('superid')
        rcbl = dblogin.LoginBL()
        retrows = rcbl.dbgetdashboardcount(superid)
        return jsonify(retrows)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)

@appLogin.route("/getdashboardTenantsDetails")
def getdashboardTenantsDetails():
    try:
        superid = request.args.get('superid')
        rcbl = dblogin.LoginBL()
        retrows = rcbl.dbgetdashboardTenantsDetails(superid)
        return jsonify(retrows)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)


@appLogin.route("/SendOTP",methods = ['POST'])
def SendOTP():
    try:
        inputdata = request.json

        url = "http://182.18.163.39/v3/api.php"
        params = {
            "username": "Perennial",
            "apikey": "94561054cafdaf42a806",
            "senderid": "PERNAl",
            "mobile": inputdata['mobile'],
            "message": f"Dear {inputdata['name']} Your login OTP is {inputdata['otp']}.IparkRight PERENNIAL CODE"
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            result = eval(response.text)
            if 'campid' in result:
                response = ResponseModel(message='succ', result_data=result, status=True)
                return jsonify(response.__dict__)
            else:
                response = ResponseModel(message=result.get('Error'), result_data=[], status=False)
                return jsonify(response.__dict__)
        else:
            response = ResponseModel(message='Something went wrong,please try again', result_data=[], status=False)
            return jsonify(response.__dict__)
    except Exception as e:
        response = ResponseModel(message=str(e), result_data=[], status=False)
        return jsonify(response.__dict__)