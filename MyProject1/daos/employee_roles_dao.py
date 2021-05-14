from abc import abstractmethod, ABC


class EmployeeRolesDAO(ABC):

    @abstractmethod
    def create_new_employee_role(self, employee_role):
        pass

    @abstractmethod
    def get_employee_role_id(self, employee_role_id):
        pass

    @abstractmethod
    def all_employee_roles(self):
        pass

    @abstractmethod
    def update_employee_role(self, change):
        pass

    @abstractmethod
    def delete_employee_role(self, employee_role_id):
        pass
