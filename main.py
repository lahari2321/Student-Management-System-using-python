class Student:
    student_dictionary={}
    school_name="XYZ"
    def __init__(self):
        self.roll_no=input("\tEnter roll_no: ")
        self.Student_name=input("\tEnter Student Name: ")
        self.phone_number=input("\tEnter Phone Number: ")
        self.Address=input("\tEnter Address: ")
        student_class=input("\tEnter Student Class Ex[1 2 3 4 5 6 7 8 9 10]: ")

        if student_class in StudentClass.classes:
            StudentClass.classes[student_class].studentList.append(self)
        else:
            new_class=StudentClass(student_class)
            new_class.studentList.append(self)
            StudentClass.classes[student_class] = new_class
        self.student_class=StudentClass.classes[student_class]
        print("\n Students Added Successfully\n")
        self.getstudent()
    def getstudent(self):
        print("\tStudent roll_no:",self.roll_no)
        print("\tStudent Name:",self.Student_name)
        print("\tStudent Phone Number:",self.phone_number)
        print("\tStudent Address:",self.Address)
        print("\tStudent Class :",self.student_class.name)
        print("\tSchool Name: ",Student.school_name)
    def updatestudent(self):
        print("\n\t Select options to update student details\n:")
        print("\t\t1.To change Student Name:")
        print("\t\t2.To change Student phone number:")
        print("\t\t3.To change Student Address:")
        print("\t\t4.To change Student Class:")
        option=input("\t\tEnter any above option: ")
        print()
        if option in ["1","2","3","4"]:
            if option=="1":
                self.Student_name=input("\n\tEnter Student Name: ")
                print("\t\t Student Name Changed Successfully")
            elif option=="2":
                self.phone_number=input("\n\tEnter Student phone number: ")
                print("\t\t Student Phone Number Changed Successfully")
            elif option=="3":
                self.Address=input("\n\tEnter Student Address: ")
                print("\t\t Student Address Changed Successfully")
            else:
                new_class=input("\t\tEnter Student New Class Name:")
                self.student_class.studentList.remove(self)
                try:
                     self.student_class=StudentClass.classes[new_class]
                     self.student_class.studentList.append(self)
                except:
                    addclass = StudentClass(new_class)
                    self.student_class = addclass  # set to the StudentClass instance
                    addclass.studentList.append(self)
                    print("\t\t Student Class Changed Successfully")

            self.getstudent()
        else:
            print("\n\tYou Choosen Wrong Option")
    @classmethod
    def updateschoolname(cls,new_school_name):
        cls.school_name=new_school_name

    @classmethod
    def gettotalstudentscount(cls):
        return len(cls.student_dictionary)
class StudentClass:
    classes={}
    def __init__(self,name):
        self.name=name
        StudentClass.classes[name]=self
        self.studentList=[]
def main():
        print("---WELCOME TO ",Student.school_name ,"SCHOOL---\n")
        print("\t1) To Get Student Details")
        print("\t2) To Add New Student ")
        print("\t3) To Remove Details")
        print("\t4) To Update Student Details")
        print("\t5) To Update School Name")
        print("\t6) To Get Number of Students in School")
        print("\t7) To Get All Student Details")
        print("\t8) To Get Class Student Details")
        option=int(input("Enter your option: "))
        if option==1:
           roll_no=input("\n\tEnter roll_no of the Student: ")
           try:
               Student.student_dictionary[roll_no].getstudent()
           except:
                 print("\n\tYOU ARE ENTERED WRONG ROLL NO")
        elif option==2:
            new_student=Student()
            Student.student_dictionary[new_student.roll_no]=new_student
        elif option==3:
            roll_no=input("\n\tEnter roll_no of the Student: ")
            try:
                 student=Student.student_dictionary.pop(roll_no)
                 student.student_class.studentList.remove(student)
                 print("\t\t",roll_no,"Student Removed Successfully")
            except:
                print("\n\tNO STUDENT FOUND")
        elif option==4:
          roll_no=input("\tEnter roll_no of the Student: ")
          print()
          try:
            student=Student.student_dictionary[roll_no].updatestudent()
          except:
             print("\n\tYOU ARE ENTERED WRONG ROLL NO")
        elif option==5:
            new_school_name=input("\t\nEnter The New School Name: ")
            Student.updateschoolname(new_school_name)
            print("\n\tSchool Name Changed Successfully")
        elif option==6:
              print("\n\tTotal Number of Students in School",Student.gettotalstudentscount())
        elif option==7:
            if Student.student_dictionary:
                print("\n\tTotal Number of Students in School", Student.gettotalstudentscount())
                print("\nTotal Stdents List With Details\n")
                for sNo,student  in enumerate(Student.student_dictionary.values()):
                     print('Student -',sNo+1)
                     student.getstudent()
                     print()
            else:
                print("\n\tNo Student Found")

        elif option==8:
            try:
               students=StudentClass.classes[input("enter class name: ")]
               print("\nstudents of class:",students.name)
               print("Total number of students in class",students.name,":",len(students.studentList)
)
               print()
               for sNo,student in enumerate(students.studentList):
                    print("Student -",sNo+1)
                    student.getstudent()
                    print()
            except:
              print("\n\tYOU ENTERED WRONG CLASS (OR) No Student Found")
if __name__=='__main__':
         option="yes"
         while option=="yes":
            main()
            option=input("\n\tDo You Want To Continue? (Yes/No): ")
            print()