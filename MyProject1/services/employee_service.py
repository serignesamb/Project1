from daos.employee_dao_impl import EmployeeDAOImpl


class EmployeeService:
    employee_dao = EmployeeDAOImpl()

    @classmethod
    def create_new_employee(cls, employee):
        return cls.employee_dao.create_new_employee(employee), 201

    @classmethod
    def all_employees(cls):
        return cls.employee_dao.all_employees()

    @classmethod
    def get_employee_by_id(cls, employee_id):
        return cls.employee_dao.get_employee_id(employee_id)

    @classmethod
    def update_employee(cls, employee):
        return cls.employee_dao.update_employee(employee)

    @classmethod
    def delete_employee(cls, employee_id):
        return cls.employee_dao.delete_employee(employee_id)

    @classmethod
    def login(cls, username, password):
        return cls.employee_dao.get_user(username, password)
