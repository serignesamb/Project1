from daos.course_list_dao import CoursesListDAO
from exceptions.resource_not_found import ResourceNotFound
from models.course_list_model import CoursesList
from models.employee_model import Employee
from models.reimbursment_model import ReimbursementForm
from util.db_connection import connection


class CoursesListDAOImpl(CoursesListDAO):
    def create_new_course(self, course_list, id):
        sql = "INSERT INTO courseslist VALUES(DEFAULT, %s, %s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [course_list.course_name, course_list.employee_id])
        record = cursor.fetchone()

        # because this is insertion which is part of the DML, the data needs to be committed after it's added
        connection.commit()

        return CoursesList(record[0], record[1], record[2])

    def get_course_id(self, course_id):
        sql = "SELECT * FROM courseslist WHERE employee_id= %s"  # %s is a placeholder for string
        cursor = connection.cursor()
        cursor.execute(sql, [course_id])

        records = cursor.fetchall()

        course_list = []
        # iterating through that list
        for record in records:
            # create a new movie object and passing the values from the course list by following the order
            # that is in the database couselist
            courses = CoursesList(record[0], record[1], record[2])
            # append the result to the movie_list we created and convert them to json()
            course_list.append(courses.json())
        return course_list


    def get_course_name(self, course_id):
        sql = "SELECT course_name FROM courseslist WHERE course_id= %s"  # %s is a placeholder for string
        cursor = connection.cursor()
        cursor.execute(sql, [course_id])

        records = cursor.fetchone()
        return records

    def all_courses(self):
        # a sql statement that would equate to getting all the courses from our database
        sql = "SELECT * FROM courseslist"
        # setting up an object called cursor , and assign connection object after importing it from util
        # This connection object has many methods like cursor()
        cursor = connection.cursor()
        # using this cursor object to execute sql statments and pass sql command to it
        cursor.execute(sql)
        # store those results in an object called records
        records = cursor.fetchall()

        # create a list for our movie list
        course_list = []
        # iterating through that list
        for record in records:
            # create a new movie object and passing the values from the movie list by following the order
            # that is in the database course
            courses = CoursesList(record[0], record[1], record[2])
            # append the result to the course_list we created and convert them to json()
            course_list.append(courses.json())
        return course_list

    def update_course(self, change):
        sql = "UPDATE courseslist SET course_name=%s, employee_id=%s RETURNING * "

        cursor = connection.cursor()
        cursor.execute(sql, (change.course_name, change.employee_id))
        connection.commit()

        record = cursor.fetchone()
        return CoursesList(record[0], record[1], record[2])

    def delete_course(self, course_id):
        sql = "DELETE FROM courseslist WHERE course_id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [course_id])
        connection.commit()
