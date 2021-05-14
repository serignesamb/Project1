from daos.employee_roles_dao_impl import EmployeeRoleIDImpl
from daos.reimbursement_dao_impl import ReimbursementDAOImpl
from services.reimbursment_service import ReimbursementService


class EmployeeRolesService:
    employee_role_dao = EmployeeRoleIDImpl()

    @classmethod
    def create_new_employee_role(cls, employee_role_id, emp_object):
        return cls.employee_role_dao.create_new_employee_role(employee_role_id, emp_object), 201

    @classmethod
    def all_employees_roles(cls):
        return cls.employee_role_dao.all_employee_roles()

    @classmethod
    def get_employee_role_by_id(cls, employee_role_id):
        return cls.employee_role_dao.get_employee_role_id(employee_role_id)

    @classmethod
    def update_employee_role(cls, employee_role_obj, emp_id):
        return cls.employee_role_dao.update_employee_role(employee_role_obj, emp_id)

    @classmethod
    def delete_employee_role(cls, employee_role_id):
        return cls.employee_role_dao.delete_employee_role(employee_role_id)

    @classmethod
    def approval_process(cls, employee_role_id):
        pass

