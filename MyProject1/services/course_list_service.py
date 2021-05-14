from daos.course_list_dao_impl import CoursesListDAOImpl


class CoursesListService:
    course_list_dao = CoursesListDAOImpl()

    @classmethod
    def create_new_course(cls, course_list, id):
        return cls.course_list_dao.create_new_course(course_list, id), 201

    @classmethod
    def all_courses(cls):
        return cls.course_list_dao.all_courses()


    @classmethod
    def get_course_id(cls, course_id):
        return cls.course_list_dao.get_course_id(course_id)

    @classmethod
    def get_course_name(cls, course_id):
        return cls.course_list_dao.get_course_name(course_id)

    @classmethod
    def update_course(cls, course):

        return cls.course_list_dao.update_course(course)

    @classmethod
    def delete_course(cls, course_id):
        return cls.course_list_dao.delete_course(course_id)
