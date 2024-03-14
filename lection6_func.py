def myprint():
    """
    for print any info
    """
    # pass
    print("We learning Python lang")

def hi_print(name:str, age:int):
    """
    name -> name of user
    age -> age of user
    """
    # pass
    print(f"Hi, {name}. You have {age} years old.")

print(type(myprint))
myprint()
func_print=myprint
func_print()
print(myprint.__doc__)
print(type(func_print))

hi_print("Oleg",25)
hi_print(age=25,name="Oleg")
print(hi_print("Ihor",38))

# def suma(a:int=0,b:int=0)->int:
#     """
#     a:int => operand 1,b:int => operand 2
#     return a+b
#     """
#     return a+b

def suma(a=0,b=0):
    """
    a:int => operand 1,b:int => operand 2
    return a+b
    """
    return a+b
print(suma(2,3))
print(suma(b=2,a=3))
print(suma(2))

def get_sum(*nums):
    s = 0
    for a in nums:
        s += a
    return s

print(get_sum(1, 2, 5, 6, 7))
print(get_sum(*[1, 2, 5, 6, 7]))
# sum([1,2,4,5])

def get_sum1(func,*nums):
    s = 0
    for a in nums:
        s += a
    return func(s)

def x_2(x):
    return x**2

print(get_sum1(x_2, 1, 2, 3, 4))
print(get_sum1(lambda x:x**3, 1, 2, 3, 4))
x_3=lambda x:x**3
print(get_sum1(x_3, 1, 2, 3, 4))


# Визначення функції:
def func2(*args, **kwargs):
    print(args)
    print(kwargs)
# Виклик функції:
func2(1, 2, 3, 4, a=1, b=2, c=3)

dict_books={"Shevcenko":"Katerina", "Franko":"Kamenayr"}
func2(*[1,2,3],**dict_books)
func2(1,2,3,4,Shevcenko="Katerina",Franko="Kamenayr")


def func3(list1=[]):
    s=0
    for n in list1:
        if n%2==0:
            s+=n
    return s

print(func3([3,4,5,6]))

name="Tetyana"
def func4(list1=[]):
    global name
    s=0
    name="Ihor"
    for n in list1:
        if n%2==0:
            s+=n
    return s, name

print(func4([3,4,5,6]))
print(name)