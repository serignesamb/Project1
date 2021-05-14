from datetime import datetime, time

from daos.reimbursement_dao import ReimbursementDAO
from exceptions.resource_not_found import ResourceNotFound
from models.employee_model import Employee
from models.reimbursment_model import ReimbursementForm
from util.db_connection import connection


class ReimbursementDAOImpl(ReimbursementDAO):
    def create_new_reimbursement_form(self, reimbursement):
        sql = "INSERT INTO reimbursementform VALUES(DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s,%s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement.event_location, reimbursement.event_type, reimbursement.description,
                             reimbursement.work_justification, reimbursement.grade_format, reimbursement.event_cost,
                             reimbursement.employee_id, reimbursement.islate,reimbursement.approval_status])

        # because this is insertion which is part of the DML, the data needs to be committed after it's added
        connection.commit()
        record = cursor.fetchone()
        return ReimbursementForm(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                                 record[7], record[8], record[9]).json()

    def get_reimbursement_form_id(self, reimbursement_id):
        sql = "SELECT * FROM reimbursementform WHERE employee_id = %s"  # %s is a placeholder for string
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement_id])
        record = cursor.fetchone()

        connection.commit()

        if record:
            reimbursement = ReimbursementForm(record[0], record[1], record[2], record[3], record[4], record[5],
                                              record[6], record[7], record[8], record[9])
            # append the result to the movie_list we created and convert them to json()
            return reimbursement
        else:
            raise ResourceNotFound(f"The employee id tuition does not exist")


    # def get_employee_id(self, employee_id):
    #     sql = "SELECT * FROM employees WHERE employee_id = %s"  # %s is a placeholder for string
    #     cursor = connection.cursor()
    #     cursor.execute(sql, [employee_id])
    #
    #     record = cursor.fetchone()
    #
    #     if record:
    #         return Employee(record[0], record[1], record[2], record[3], record[4], record[5], record[6],
    #                         record[7], record[8])
    #     else:
    #         raise ResourceNotFound(f"Employee with id: {employee_id} - Not Found")

    def all_reimbursements(self):
        # a sql statement that would equate to getting all the moives from our database
        sql = "SELECT * FROM reimbursementform"
        # setting up an object called cursor , and assign connection object after importing it from util
        # This connection object has many methods like cursor()
        cursor = connection.cursor()
        # using this cursor object to execute sql statments and pass sql command to it
        cursor.execute(sql)
        # store those results in an object called records
        records = cursor.fetchall()

        # create a list for our movie list
        reimbursement_list = []
        # iterating through that list
        for record in records:
            # create a new movie object and passing the values from the movie list by following the order
            # that is in the database movies
            reimbursement = ReimbursementForm(record[0], record[1], record[2], record[3], record[4], record[5],
                                              record[6],
                                              record[7], record[8], record[9])
            # append the result to the movie_list we created and convert them to json()
            reimbursement_list.append(reimbursement.json())
        return reimbursement_list

    def update_reimbursement_form(self, change, emp_id):
        sql = "UPDATE reimbursementform SET approval_status=%s WHERE employee_id=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [change.approval_status, change.employee_id])

        record = cursor.fetchone()
        connection.commit()

        return ReimbursementForm(record[0], record[1]).json()


    def delete_reimbursement_form(self, reimbursement_id):
        sql = "DELETE FROM reimbursementform WHERE tuition_id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement_id])
        connection.commit()
