from typing import NamedTuple
class Student(NamedTuple):
    id: str = None
    gpa: float = 0

class Company(NamedTuple):
    id: int = 0
    avgGpa: float = 0


