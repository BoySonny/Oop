from teacher import Teacher
from student import Student
from grade import Grade
from load import Load

print()
print('Student')
student1 = Student('0-1234','Kambang', 'Sonny', 'Balah', 'Student', '3', 'BSCS', 'A')
print(student1.getName())
print(student1.getYrCrseSec())
print(student1)

print()
print('Teacher')
teacher1 = Teacher('21-2351', 'Kambang', 'Sonny', 'Balah', 'Teaccher', 'CED', 'Instructor')
print(teacher1.getDepartment())
print(teacher1.getName())
print(teacher1)

print()
print('Grade')
grade1 = Grade(99, 78, 85, 90)
grade1.id = '1312'
grade1.last_name = 'Kambang'
grade1.first_name = 'Sonny'
grade1.middle_name = 'Balah'
grade1.course = 'BSCS'
grade1.year = 2
grade1.section = 'A'
print(grade1.getName())
print(grade1.getYrCrseSec())
print(grade1.getAverage())


print()
print('Load')
load_1 = Load('English', 'Math', 'Science')
load_1.id = '1234'
load_1.last_name = 'Kanmbang'
load_1.first_name = 'Sonny'
load_1.middle_name = 'Balah'
load_1.department = 'Ced'
load_1.position = 'Instructor'
print(load_1.getName())
print(load_1.getDepartment())
print(load_1.getPosition())
print(load_1.getLoad())




