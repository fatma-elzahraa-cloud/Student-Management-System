class Student:
    def __init__(self, student_id, name, age, department, grades=None, attendance=None):
        self.student_id = str(student_id)
        self.name = name
        self.age = age
        self.department = department
        self.grades = grades if grades is not None else {}
        self.attendance = attendance if attendance is not None else {}

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "grades": self.grades,
            "attendance": self.attendance
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            student_id=data["student_id"],
            name=data["name"],
            age=data["age"],
            department=data["department"],
            grades=data.get("grades", {}),
            attendance=data.get("attendance", {})
        )
