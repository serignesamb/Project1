from abc import abstractmethod, ABC


class ReimbursementDAO(ABC):
    @abstractmethod
    def create_new_reimbursement_form(self, reimbursement):
        pass

    @abstractmethod
    def get_reimbursement_form_id(self, reimbursement_id):
        pass

    @abstractmethod
    def all_reimbursements(self):
        pass

    @abstractmethod
    def update_reimbursement_form(self, change):
        pass

    @abstractmethod
    def delete_reimbursement_form(self, reimbursement_id):
        pass
