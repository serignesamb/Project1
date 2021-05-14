class CoursesList:
    def __init__(self, course_id=0, course_name="", employee_id=0):
        self.course_id = course_id
        self.course_name = course_name
        self.employee_id = employee_id


    def json(self):
        return {
            'courseId': self.course_id,
            'courseName': self.course_name,
            'employeeId': self.employee_id
        }

    @staticmethod
    def json_parse(json):
        course_list = CoursesList()
        course_list.course_id = json["courseId"] if "courseId" in json else 0
        course_list.course_name = json["courseName"] if "courseName" in json else None
        course_list.employee_id = json["employeeId"] if "employeeId" in json else 0
        return course_list
