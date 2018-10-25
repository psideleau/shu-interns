import pytest
from shu_models import *
from student_application_interactor import *
from spys import *
import collections

TestFixture = collections.namedtuple('TestFixture', 'student_repo company_repo uat')

@pytest.fixture
def fixture():
    student=StudentRepositorySpy()
    company=CompanyRepositorySpy()
    return TestFixture(student_repo=student, company_repo=company, uat=StudentApplicationInteractor(student, company))


def test_should_get_eligible_companies(fixture):
    fixture.student_repo.student = Student(id="324545", gpa=3.7)
    fixture.company_repo.companies = [Company(id=12378, avgGpa=4.0),Company(id=1234, avgGpa=3),Company(id=12378, avgGpa=4.0),Company(avgGpa=3.71)]

    companies = fixture.uat.find_companies("324545")

    assert fixture.student_repo.studentID == "324545"
    assert len(companies) == 1
    assert companies[0].id == 1234 
        
def test_student_gpa_does_not_qualify(fixture):
    fixture.student_repo.student = student = Student(id="324545", gpa=2.0)
    fixture.company_repo.companies = [Company(id=12378, avgGpa=4.0),Company(id=1234, avgGpa=3),Company(id=12378, avgGpa=4.0),Company(avgGpa=3.71)]

    companies = fixture.uat.find_companies("324545")

    assert len(companies) == 0
    assert fixture.student_repo.studentID == "324545"


