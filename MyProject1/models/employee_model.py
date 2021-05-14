
class Employee:
    def __init__(self, employee_id=0, employee_first_name=" ", employee_last_name="", employee_phone_number="",
                 employee_email="", employee_address="",employee_username="", employee_password="", employee_role=""):
        self.employee_id = employee_id
        self.employee_first_name = employee_first_name
        self.employee_last_name = employee_last_name
        self.employee_phone_number = employee_phone_number
        self.employee_email = employee_email
        self.employee_address = employee_address
        self.employee_username = employee_username
        self.employee_password = employee_password
        self.employee_role = employee_role

    def json(self):
        return {
            'employee_id': self.employee_id,
            'first_name': self.employee_first_name,
            'last_name': self.employee_last_name,
            'phone_number': self.employee_phone_number,
            'email_address': self.employee_email,
            'address': self.employee_address,
            'username': self.employee_username,
            'password': self.employee_password,
            'role': self.employee_role
        }

    @staticmethod
    def json_parse(json):
        employee = Employee()
        # commenting the code below allows you to not bother putting the employee_id when creating a new employee in Postman
        employee.employee_id = json["employee_id"] if "employee_id" in json else 0
        employee.employee_first_name = json["first_name"]
        employee.employee_last_name = json["last_name"]
        employee.employee_phone_number = json["phone_number"]
        employee.employee_email = json["email_address"]
        employee.employee_address = json["address"]
        employee.employee_username = json["username"]
        employee.employee_password = json["password"]
        employee.employee_role = json["role"] if "role" in json else "Regular"
        return employee

    # Without this the function is going to return an object as a result in Postman
    def __repr__(self):
        return str(self.json())