# male/female  = > ч/ж
# НАСЛІДУВАННЯ:  ЛЮДИНА=> ПРАЦІВНИК, ЛЮДИНА => СТУДЕНТ
class Human:
    numberHuman=0

    def __init__(self, name,age, gender="male"):
        self.name=name
        self.age=age
        self.gender=gender
        Human.numberHuman+=1
    
    def print_info_class(self):
        print("Class Human")
    
    
    def __str__(self) -> str:
        return f"Human: {self.name}, {self.age} years, {self.gender}"

#клас працівника
class Employee(Human):
    
    def __init__(self, name, age, gender="male",work=None,salary=0.0):
        super().__init__(name, age, gender)
        # Aбо
        # Human.__init__(self,name, age, gender)
        self.work=work
        self.salary=salary

    def __str__(self) -> str:
        text_info_human=super().__str__()
        info_employee=f"\nPlace work: {self.work}. Salary: {self.salary} грн."
        return text_info_human+info_employee

#клас працівника
class Student(Human):
   
    def __init__(self, name, age, gender="male",marks=[],educational_institution="коледж"):
        # super().__init__(name, age, gender)
        # Aбо
        Human.__init__(self,name, age, gender)
        self.marks=marks
        self.educational_institution=educational_institution
    
    def print_info_class(self):
        print("Class Student")
    
    def __str__(self) -> str:
        text_info_human=super().__str__()
        info_student=f"\nPlace learning: {self.educational_institution}"
        return text_info_human+info_student

#працюючий студент
class StudentEmployee(Student, Employee):

    def __init__(self, name, age, gender="male", marks=[], educational_institution="коледж", work="",salary=0):
        Student.__init__(self,name, age, gender, marks, educational_institution)
        Employee.__init__(self,name, age, gender,work, salary)

   

human_Denis=Human("Denis",19,"male")
print(f"Created {Human.numberHuman}")
print(human_Denis)
employee_Kostuyk=Employee("Ivan",18,"male","FPV creater",5000)
print(f"Created {Human.numberHuman}")
print(employee_Kostuyk)
employee_Nemkov=Employee("Oleksandr",19,"male","FPV-creater",8000)
print(f"Created {Human.numberHuman}")
print(employee_Nemkov)
student_Sloboda=Student("Denis",18, "male",[4,4,4],"MTHK")
print(student_Sloboda)
# student_Sloboda.print_info_class()
student_Kostuyk=StudentEmployee("Vlad",18,"male",[4,4,4],"NUWM","Qsevenics",6000)
print(student_Kostuyk)