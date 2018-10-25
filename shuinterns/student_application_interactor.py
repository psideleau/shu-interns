from shu_models import Student
from shu_models import Company
class StudentApplicationInteractor:
    def __init__(self, student_repository, company_repository):
        self.student_repository = student_repository
        self.company_repository = company_repository
    
    def find_companies(self, studentID):
        student = self.student_repository.find_student(studentID)
        companies = self.company_repository.find_companies()
        return [c for c in companies if student.gpa >= c.avgGpa ]


