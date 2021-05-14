from abc import abstractmethod, ABC


class CoursesListDAO(ABC):

    @abstractmethod
    def create_new_course(self, course_list):
        pass

    @abstractmethod
    def get_course_id(self, course_id):
        pass

    @abstractmethod
    def all_courses(self):
        pass

    @abstractmethod
    def update_course(self, change):
        pass

    @abstractmethod
    def delete_course(self, course_id):
        pass
