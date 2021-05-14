class EmployeeRoles:
    def __init__(self, employee_role_id=0, employee_role_name="", employee_id=0):
        self.employee_role_id = employee_role_id
        self.employee_role_name = employee_role_name
        self.employee_id = employee_id

    def json(self):
        return {
            'employee_role_id': self.employee_role_id,
            'employee_role_name': self.employee_role_name,
            'employee_id': self.employee_id
        }

    @staticmethod
    def json_parse(json):
        emp_role_id = EmployeeRoles()
        emp_role_id.employee_role_id = json["employee_role_id"]
        emp_role_id.employee_role_name = json["employee_role_name"]
        emp_role_id.employee_id = json["employee_id"]
        return emp_role_id

    # Without this the function is going to return an object as a result in Postman
    def __repr__(self):
        return str(self.json())