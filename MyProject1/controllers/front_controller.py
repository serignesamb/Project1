from controllers import employee_controller, courseslist_controller, reimbursement_controller, employee_role_controller, login_controller

def route(app):
    # Calls all other other controller
    employee_controller.route(app)
    courseslist_controller.route(app)
    reimbursement_controller.route(app)
    employee_role_controller.route(app)
    login_controller.route(app)

