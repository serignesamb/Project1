from abc import abstractmethod, ABC


class EmployeeDAO(ABC):

    @abstractmethod
    def create_new_employee(self, employee):
        pass

    @abstractmethod
    def get_employee_id(self, employee_id):
        pass

    @abstractmethod
    def all_employees(self):
        pass

    @abstractmethod
    def update_employee(self, change):
        pass

    @abstractmethod
    def delete_employee(self, employee_id):
        pass
