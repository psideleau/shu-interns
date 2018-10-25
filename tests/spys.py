class StudentRepositorySpy:
    def __init__(self, student=None):
        self.student = student

    def find_student(self,studentID):
        self.studentID = studentID
        return self.student;

class CompanyRepositorySpy:
    def __init__(self, companies=None):
        self.companies = companies
    def find_companies(self):
        print(self.companies)
        return self.companies
