from flask import request, jsonify
from models.employee_roles_model import EmployeeRoles
from services.employee_roles_service import EmployeeRolesService
from services.employee_service import EmployeeService


def route(app):
    @app.route("/employees/<employee_id>/role", methods=["POST"])
    def assign_employee_role(employee_id):
        emp_object = EmployeeRoles.json_parse(request.json)
        emp_new_role = EmployeeRolesService.create_new_employee_role(emp_object, employee_id)
        return jsonify(str(emp_new_role)), 201  # Resource Created

    @app.route("/roles/<employee_id>", methods=['GET'])
    def get_employee_role_by_id(employee_id):
        employee_role = EmployeeRolesService.get_employee_role_by_id(employee_id)
        return jsonify(str(employee_role)), 200  # ok

    @app.route("/roles/employee_role/<employee_role_id>", methods=['PUT'])
    def update_employee_role_by_empid(employee_id):
        employee_role_obj = EmployeeRoles.json_parse(request.json)
        employee_role_obj.employee_id = int(employee_id)
        employee_role = EmployeeRolesService.update_employee_role(employee_role_obj, employee_id)
        return jsonify(str(employee_role)), 200

    @app.route("/employeeroles", methods=['GET'])
    def get_all_employee_roles():
        return jsonify(EmployeeRolesService.all_employees_roles()), 200

    @app.route("/login/<username>/<password>/<role>", methods=["GET"])
    def login(username, password, role):
        employee_login = EmployeeService.login(username, password, role)
        if employee_login:
            return jsonify(employee_login)
        else:
            return ("Employee Not Found"), 404