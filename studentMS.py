#student management system 
class Students:
    def __init__(self,reg_no,name,age,grade):
        self.reg_no = reg_no
        self.name = name
        self.age = age
        self.grade = grade


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_students(self):
        reg_no = input("enter registration no. ")
        name = input("enter student name. ")
        age = input("enter age. ")
        grade = input('enter grade. ')
        student = Students(reg_no,name,age,grade)
        self.students.append(student)
        print('student successfull added.')

    def view_student(self):
        if not self.students:
            print("there is no students added")
        else:
            for student in self.students:
                print(student)

    def delete_student(self):
        reg_no = input("delete by regstration no. ")
        for student in self.students:
            if student.reg_no == reg_no:
                self.students.remove(student)
                print('students successfull removed')
        print("students not found")

    def search_student(self):
        reg_no = input('enter student regstration no. ')
        for student in self.students:
            if student.reg_no == reg_no:
                print(student)
        
        print("student not found")

def main():
    sms = StudentManagementSystem()
    while True:
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("|||||||||||||||| STUDENTS MENAGEMENT SYSTEM ||||||||||||||||")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        print("1. to add students.")
        print("2. to view students.")
        print("3. to delete students.")
        print("4. to search students.\n")
        print("--------------------------------------------------------------\n")

        print("use number to select what to do.")

        choice = input("enter choice. ")
        if choice == '1':
            sms.add_students()
        elif choice == '2':
            sms.view_student()
        elif choice == '3':
            sms.delete_student()
        elif choice == '4':
            sms.search_student()
        else:
            print("invalid input. try again.")

if __name__=="__main__":
    main()