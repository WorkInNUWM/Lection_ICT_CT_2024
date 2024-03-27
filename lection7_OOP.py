# number=7
# print(number.bit_count())
# print(type(number))

class Student():
    """
    Model of Students...
    """
    count_student=0 # змінна класу
    def __init__(self,name="Noname",age=1):
        self.name=name  #attr, field, property
        self.age=age
        self.seteaty=100
        Student.count_student+=1
    
    def do_work_lab(self,number_lab): #method
        if self.issetiaty():
            print(f"I worked lab{number_lab} of Python...")
            self.seteaty-=15
        else:
            print("Nead to eat...")
            print(f"I will work lab{number_lab} of Python...")

    
    def eat(self):
        print("I a little eat...")
        self.seteaty+=20
    
    def issetiaty(self):
        if self.seteaty<=30:
            return False
        else:
            return True
        
    def __str__(self):
        return f"Student (name: {self.name}, age: {self.age})"



# st1=Student()
# st2=Student()

# # print(st1.name)
# # print(st2.name)
# # Student.name="Olga"
# # print(Student.name)
# print(st1.name)
# print(st2.name)
# st1.name="Olga"
# print(st1.name)
# print(st2.name)
st1=Student("Olga",22)
st2=Student("Dmitro",21) 
 
print(f"Count object students: {Student.count_student}")  
print(st1)   
print(st2)   
# симуляція життя студента
print(st1.name)
print(st1.age)
print(st1.seteaty)
st1.do_work_lab(3)
print(st1.seteaty)
st1.do_work_lab(4)
print(st1.seteaty)
st1.do_work_lab(5)
print(st1.seteaty)
st1.do_work_lab(6)
print(st1.seteaty)
st1.do_work_lab(7)
print(st1.seteaty)
st1.do_work_lab(8)
print(st1.seteaty)
st1.eat()
st1.do_work_lab(8)
print(st1.seteaty)





