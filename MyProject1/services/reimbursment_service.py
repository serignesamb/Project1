from flask import jsonify

from daos.employee_roles_dao_impl import EmployeeRoleIDImpl
from daos.reimbursement_dao_impl import ReimbursementDAOImpl
from models.reimbursment_model import ReimbursementForm
from services.employee_service import EmployeeService


class      ReimbursementService:

    reimbursement_dao = ReimbursementDAOImpl()

    @classmethod
    def create_new_reimbursement(cls, reimbursement):
        return cls.reimbursement_dao.create_new_reimbursement_form(reimbursement), 201

    @classmethod
    def all_reimbursements(cls):
        return cls.reimbursement_dao.all_reimbursements()

    @classmethod
    def get_reimbursement_by_id(cls, reimbursement_id):
        return cls.reimbursement_dao.get_reimbursement_form_id(reimbursement_id)

    @classmethod
    def update_reimbursement(cls, reimbursement, employee_id):
        return cls.reimbursement_dao.update_reimbursement_form(reimbursement, employee_id)

    @classmethod
    def delete_reimbursement(cls, reimbursement_id):
        return cls.reimbursement_dao.delete_reimbursement_form(reimbursement_id)

    @classmethod
    def approval_process(cls, employee_id):
        employee_role_name = []
        employee = EmployeeService.get_employee_by_id(int(employee_id))
        if employee:
            reimbursement = ReimbursementService.get_reimbursement_by_id(employee_id)
            if reimbursement.islate:
                employee_roles = EmployeeRoleIDImpl.all_employee_roles(employee_id)
                for emp_role in employee_roles:

                    # Checks if an employee id is in the list
                    if employee_id in list(emp_role.values()):
                        print("yes")
                        # prints out the key & value of the employee role based on the employee id passed
                        employee_role_name = list(emp_role.keys())[1], list(emp_role.values())[1]
                        if 'Head' in employee_role_name:
                            reimbursement.approval_status = "Approved"
                            reimburse = ReimbursementService.update_reimbursement(reimbursement, employee_id)
                            print("reimburse:", reimburse)
                            return jsonify(str(reimburse)), 200

                print(employee_role_name)















                # print("employee role", employee_role)
                # supervisor_role = employee_role[1]
                # print("supervisor", supervisor_role)
                # dep_head_role = employee_role[1]
                # print("department head", dep_head_role)
                # benco_role = employee_role[2]
                # print("benco", benco_role)
                #
                # if employee_role_name:
                #     reimbursement.approval_status = "Approved"
                #     reimburse = ReimbursementService.update_reimbursement(reimbursement, employee_id)
                #     print("reimburse:" , reimburse)
                #     return jsonify(str(reimburse)), 200







