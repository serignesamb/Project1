from flask import request, jsonify, json
from psycopg2.extensions import JSON

from exceptions.resource_not_found import ResourceNotFound
from models.reimbursment_model import ReimbursementForm
from services.course_list_service import CoursesListService
from services.employee_service import EmployeeService
from services.reimbursment_service import ReimbursementService

def route(app):
    @app.route("/reimbursements", methods=["POST"])

    def create_new_reimbursement():
        try:
            reimbursement = ReimbursementForm.json_parse(request.json)
            # employee_service = EmployeeService.get_employee_by_id(employee_id)
            # course_service = CoursesListService.get_course_id(course_id)
            reimbursement_service = ReimbursementService.create_new_reimbursement(reimbursement)
            return jsonify(reimbursement_service), 201  # Resource Created
        except ResourceNotFound:
            return f"Employee ID Does not exist", 404

    @app.route("/reimbursements", methods=['GET'])
    def get_all_reimbursements():
        return jsonify(ReimbursementService.all_reimbursements()), 200


    # @app.route("/reimbursements/<employee_id>", methods=['GET'])
    # def get_reimbursement_by_empid(employee_id):
    #     record = []
    #     for firstElement in ReimbursementService.get_reimbursement_by_id(employee_id):
    #         record = firstElement
    #     return jsonify(record), 200

    @app.route("/reimbursements/<employee_id>", methods=['GET'])
    def get_reimbursement_by_empid(employee_id):
        try:
            employee = ReimbursementService.get_reimbursement_by_id(int(employee_id))
            return jsonify(employee.json()), 200  # ok
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/reimbursement/<employee_id>", methods=['PUT'])
    def update_reimbursement_by_empid(employee_id):
        reimbursement_req = ReimbursementForm.json_parse(request.json)
        # reimbursement_req.employee_id = int(employee_id)
        reimbursement = ReimbursementService.update_reimbursement(reimbursement_req, employee_id)
        return jsonify(reimbursement), 200

    # @app.route("/roles/<employee_id>", methods=["PUT"])
    # def approval_role(employee_id):
    #     reimbursement_service = ReimbursementService.approval_process(int(employee_id))
    #     return f"Employee with ID {employee_id} is approved {reimbursement_service}", 200















