from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)




@app.route('/')
def ServiceHealth():
    return jsonify('IparkRight Service Is Up')
from IparkRight.IparkApis import Tenents,Vehicles,login,Reports,Residents
app.register_blueprint(Tenents.appOrganization)
app.register_blueprint(Vehicles.appVehicle)
app.register_blueprint(login.appLogin)
app.register_blueprint(Reports.appReports)
app.register_blueprint(Residents.appResidents)



if __name__ == "__main__":
    app.run()
