
from daos.employee_roles_dao import EmployeeRolesDAO
from models.employee_roles_model import EmployeeRoles
from util.db_connection import connection


class EmployeeRoleIDImpl(EmployeeRolesDAO):
    def create_new_employee_role(self, employee_role_id,emp_object):
        sql = "INSERT INTO employeeroles VALUES(DEFAULT, %s, %s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (employee_role_id.employee_role_name, employee_role_id.employee_id))
        record = cursor.fetchone()
        # because this is insertion which is part of the DML, the data needs to be committed after it's added
        connection.commit()

        return EmployeeRoles(record[0], record[1], record[2])

    def get_employee_role_id(self, employee_role_id):
        sql = "SELECT * FROM employeeroles WHERE employee_id = %s"  # %s is a placeholder for string
        cursor = connection.cursor()
        cursor.execute(sql, [employee_role_id])

        record = cursor.fetchone()

        if record:
            return EmployeeRoles(record[0], record[1], record[2])
        else:
            return f"Employee Role with id: {employee_role_id} - Not Found"

    def all_employee_roles(self):
        # a sql statement that would equate to getting all the moives from our database
        sql = "SELECT * FROM employeeroles"
        # setting up an object called cursor , and assign connection object after importing it from util
        # This connection object has many methods like cursor()
        cursor = connection.cursor()
        # using this cursor object to execute sql statments and pass sql command to it
        cursor.execute(sql)
        # store those results in an object called records
        records = cursor.fetchall()

        # create a list for our movie list
        employee_role_list = []
        # iterating through that list
        for record in records:
            # create a new movie object and passing the values from the movie list by following the order
            # that is in the database movies
            roles = EmployeeRoles(record[0], record[1], record[2])
            # append the result to the movie_list we created and convert them to json()
            employee_role_list.append(roles.json())
        return employee_role_list

    def update_employee_role(self, change, employee_id):
        sql = "UPDATE employeeroles SET employee_role_name=%s WHERE employee_role_id=%s RETURNING * "

        cursor = connection.cursor()
        cursor.execute(sql, (change.employee_role_name, change.employee_role_id))
        connection.commit()

        record = cursor.fetchone()
        return EmployeeRoles(record[0], record[1], record[2])

    def delete_employee_role(self, employee_role_id):
        sql = "DELETE FROM employeeroles WHERE employee_role_id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_role_id])
        connection.commit()
