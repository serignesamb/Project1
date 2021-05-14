from flask import jsonify

from exceptions.resource_not_found import ResourceNotFound
from services.employee_service import EmployeeService

def route(app):
    @app.route("/login/<username>/<password>", methods=["GET"])
    def employee_login(username, password):
        logininfo = EmployeeService.login(username, password)
        if logininfo:
            return jsonify(logininfo.json()), 200

