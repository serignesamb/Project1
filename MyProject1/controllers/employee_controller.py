from flask import Flask, jsonify, request
from exceptions.resource_not_found import ResourceNotFound
from models.employee_model import Employee
from services.employee_service import EmployeeService


def route(app):
    @app.route("/employees", methods=["POST"])
    def create_new_employee():
        employee = Employee.json_parse(request.json)
        employees = EmployeeService.create_new_employee(employee)
        return jsonify(employees), 201  # Resource Created

    @app.route("/employees/<employee_id>", methods=['GET'])
    def get_employee_by_id(employee_id):
        try:
            employee = EmployeeService.get_employee_by_id(int(employee_id))
            return jsonify(employee.json()), 200  # ok
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employees", methods=['GET'])
    def get_all_employees():
        return jsonify(EmployeeService.all_employees()), 200

    # Update account with id 3 for client 10
    @app.route("/employees/<employee_id>", methods=["PUT"])
    def update_employee_with_employee_id(employee_id):
        employee = Employee.json_parse(request.json)
        employee.employee_id = int(employee_id)
        employee = EmployeeService.update_employee(employee)
        return jsonify(employee.json()), 500


    @app.route("/employees/<employee_id>", methods=['DELETE'])
    def delete_employee_by_id(employee_id):
        try:
            if EmployeeService.get_employee_by_id(int(employee_id)):
                EmployeeService.delete_employee(employee_id)
                return '', 204

        except ResourceNotFound as m:
            return "Employee does not exist", 404

