
class ReimbursementForm:
    def __init__(self, tuition_id=0, event_location="", event_type="", description="",
                 work_justification="", grade_format="", event_cost=0,employee_id=0,
                 islate=True, approval_status=""):
        # supervisor_approval_status=False, head_approval_status= False, benco_approval_status= False
        self.tuition_id = tuition_id
        self.event_location = event_location
        self.event_type = event_type
        self.description = description
        self.work_justification = work_justification
        self.grade_format = grade_format
        self.event_cost = event_cost
        self.employee_id = employee_id
        self.islate = islate
        self.approval_status = approval_status
        # self.supervisor_approval_status = supervisor_approval_status
        # self.head_approval_status = head_approval_status
        # self.benco_approval_status = benco_approval_status


    def json(self):
        return {
            'tuitionId': self.tuition_id,
            'eventLocation': self.event_location,
            'eventType': self.event_type,
            'description': self.description,
            'workJustification': self.work_justification,
            'gradeFormat': self.grade_format,
            'eventCost': self.event_cost,
            'islate': self.islate,
            'approvalStatus': self.approval_status,
            'employeeId': self.employee_id
        }

    @staticmethod
    def json_parse(json):
        reimbursement = ReimbursementForm()
        reimbursement.tuition_id = json["tuitionId"] if "tuitionId" in json else 0
        reimbursement.event_location = json["eventLocation"] if "eventLocation" in json else None
        reimbursement.event_type = json["eventType"] if "eventType" in json else None
        reimbursement.description = json["description"] if "description" in json else None
        reimbursement.work_justification = json["workJustification"] if "workJustification" in json else None
        reimbursement.grade_format = json["gradeFormat"] if "gradeFormat" in json else None
        reimbursement.event_cost = json["eventCost"] if "eventCost" in json else None
        reimbursement.employee_id = json["employeeId"] if "employeeId" in json else 0
        reimbursement.isLate = json["islate"] if "islate" in json else None
        reimbursement.approval_status = json["approvalStatus"] if "approvalStatus" in json else "Pending"
        return reimbursement

 # Without this the function is going to return an object as a result in Postman
    def __repr__(self):
        return str(self.json())
