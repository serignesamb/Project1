from flask import jsonify, json

from daos.employee_dao import EmployeeDAO
from exceptions.resource_not_found import ResourceNotFound
from models.employee_model import Employee
from util.db_connection import connection


class EmployeeDAOImpl(EmployeeDAO):
    def create_new_employee(self, employee):
        sql = "INSERT INTO employees VALUES(DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [employee.employee_first_name, employee.employee_last_name,
                             employee.employee_phone_number,
                             employee.employee_email, employee.employee_address,
                             employee.employee_username, employee.employee_password, employee.employee_role])

        # because this is insertion which is part of the DML, the data needs to be committed after it's added
        connection.commit()
        record = cursor.fetchone()

        return Employee(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                        record[7], record[8]).json()

    def get_employee_id(self, employee_id):
        sql = "SELECT * FROM employees WHERE employee_id = %s"  # %s is a placeholder for string
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])

        record = cursor.fetchone()

        if record:
            return Employee(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                            record[7], record[8])
        else:
            raise ResourceNotFound(f"Employee with id: {employee_id} - Not Found")

    def all_employees(self):
        # a sql statement that would equate to getting all the employees from our database
        sql = "SELECT * FROM employees"
        # setting up an object called cursor , and assign connection object after importing it from util
        # This connection object has many methods like cursor()
        cursor = connection.cursor()
        # using this cursor object to execute sql statements and pass sql command to it
        cursor.execute(sql)
        # store those results in an object called records
        records = cursor.fetchall()

        # create a list for our movie list
        employee_list = []
        # iterating through that list
        for record in records:
            # create a new employee object and passing the values from the employee list by following the order
            # that is in the database employees
            employee = Employee(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                record[7], record[8])
            # append the result to the employees_list we created and convert them to json()
            employee_list.append(employee.json())
        return employee_list

    def update_employee(self, change):
        sql = "UPDATE employees SET employee_first_name=%s, employee_last_name=%s, employee_phone_number=%s," \
              "employee_email=%s, employee_address=%s,employee_username=%s, employee_password=%s ,employee_role=%s" \
              "WHERE employee_id=%s " \
              "RETURNING * "

        cursor = connection.cursor()
        # Keep in mind employee_id has to be added in the last column otherwise you will get "tuple index out of
        # range" error
        cursor.execute(sql, (change.employee_first_name, change.employee_last_name, change.employee_phone_number,
                             change.employee_email, change.employee_address,
                             change.employee_username, change.employee_password,
                             change.employee_role, change.employee_id))
        connection.commit()

        record = cursor.fetchone()
        return Employee(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                        record[7], record[8])

    def delete_employee(self, employee_id):
        sql = "DELETE FROM employees WHERE employee_id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        connection.commit()

    def get_user(self, username, password):
        sql = "SELECT * FROM employees WHERE employee_username=%s AND employee_password=%s "

        cursor = connection.cursor()
        cursor.execute(sql, [username, password])

        connection.commit()

        record = cursor.fetchone()

        if record:
            return Employee(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                            record[7], record[8])
