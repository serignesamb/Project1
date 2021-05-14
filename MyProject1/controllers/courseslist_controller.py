from flask import Flask, jsonify, request
from exceptions.resource_not_found import ResourceNotFound
from models.course_list_model import CoursesList
from services.course_list_service import CoursesListService
from services.employee_service import EmployeeService


def route(app):
    @app.route("/addcourse/<id>", methods=['POST'])
    def create_new_course(id):
        try:
            course = CoursesList.json_parse(request.json)
            CoursesListService.create_new_course(course, id)
            return jsonify(course.json()), 201
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/getcourses", methods=['GET'])
    def get_all_courses():
        return jsonify(CoursesListService.all_courses()), 200

    @app.route("/viewcourses/<emp_id>", methods=["GET"])
    def view_courses(emp_id):
        try:
            courses = CoursesListService.get_course_id(int(emp_id))
            return jsonify(courses)
        except ValueError:
            return "Course ID does not exist"

    @app.route("/courses/<course_id>", methods=["GET"])
    def get_course_name(course_id):
        try:
            course_name = CoursesListService.get_course_name(int(course_id))
            return jsonify(f"Course Name:  {course_name}")
        except ValueError:
            return "Course ID does not exist"

    @app.route("/employees/<employee_id>/courses", methods=['GET'])
    def get_courses_with_employee_id(employee_id):
        try:
            if EmployeeService.get_employee_by_id(employee_id):
                course = CoursesListService.get_course_id(int(employee_id))
                return jsonify(course), 200
        except ValueError as ve:
            return "This is not a valid id", 400
        except ResourceNotFound as r:
            return "The passed Employee ID or Course ID is missing", 404

    @app.route("/courses/<course_id>", methods=["DELETE"])
    def delete_course(course_id):
        CoursesListService.delete_course(int(course_id))
        return ("Course is Deleted!"), 204
