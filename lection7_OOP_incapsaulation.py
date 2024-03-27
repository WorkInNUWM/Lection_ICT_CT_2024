#Принципи ООП: Інкапсуляція, Наслідування, Поліморфізм.
# Інкапсуляція - приховування атрибутів класу
class Student():
    """
    Model of Students...
    """
    count_student=0 # змінна класу
    def __init__(self,name="Noname",age=1):
        # self.name=name  #attr, field, property
        # self._name=name  #protected
        self.__name=name  #private
        self.__age=age
        self.__seteaty=100
        Student.count_student+=1
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_seteaty(self):
        return self.__seteaty

    def do_work_lab(self,number_lab): #method
        if self.issetiaty():
            print(f"I worked lab{number_lab} of Python...")
            self.__seteaty-=15
        else:
            print("Nead to eat...")
            print(f"I will work lab{number_lab} of Python...")

    
    def eat(self):
        print("I a little eat...")
        self.__seteaty+=20
    
    def issetiaty(self):
        if self.__seteaty<=30:
            return False
        else:
            return True
        
    def __str__(self):
        return f"Student (name: {self.__name}, age: {self.__age})"



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
# print(st1.__name)
print(st1.get_name())
# print(st1.age)
print(st1.get_age())
# print(st1.seteaty)
print(st1.get_seteaty())
st1.do_work_lab(3)
st1.do_work_lab(4)
st1.do_work_lab(5)
st1.do_work_lab(6)
st1.do_work_lab(7)
st1.do_work_lab(8)
st1.do_work_lab(8)
st1.eat()
st1.do_work_lab(8)
print(st1.get_seteaty())
# realisation incsapsulation
# print(st1._name)
# st1._name="Oksana"
# print(st1._name)
# print(st1.__name) #error


