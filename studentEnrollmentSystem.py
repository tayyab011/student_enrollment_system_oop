class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)


class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.__is_enrolled == False:
            self.__is_enrolled = True
            print(f"Student {self.__student_id} enrolled successfully")
        else:
            print("Student is already enrolled")

    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print("Student dropped successfully")
        else:
            print("Student doesn't enrolled yet")

    def view_student_info(self):
        print(f"Student ID: {self.__student_id} | Name: {self.__name} | Department: {self.__department} | Enrolled: {self.__is_enrolled}")

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def get_is_enrolled(self):
        return self.__is_enrolled


s1 = Student(101, 'Md Monir', 'cse', False)
s2 = Student(102, 'Md Asad', 'bba', False)
s3 = Student(103, 'Md Latif', 'law', False)


while True:
    print("--------------")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")
    print("---------------")

    option = int(input("Enter your option: "))

    if option == 1:
        for i in StudentDatabase.student_list:
            i.view_student_info()

    elif option == 2:
        student_id = int(input("Enter Student ID: "))
        found = False

        for student in StudentDatabase.student_list:
            if student_id == student.get_student_id():
                Student.enroll_student(student)     
                found = True
                break

        if found == False:
            print("Invalid user")

    elif option == 3:
        student_id = int(input("Enter Student ID: "))
        found = False

        for student in StudentDatabase.student_list:
            if student_id == student.get_student_id():
                Student.drop_student(student)       
                found = True
                break

        if found == False:
            print("Invalid user")

    elif option == 4:
        break

    else:
        print("Invalid option number")