# a=True
# b=False
# print(type(True))
# print(a>b)
# print(a!=b)
# # and  or  not
# a=5
# b=7

# #if/elif/else
# if a>b: #logic expretions
#     print(a,">",b)
# else:
#     print(a,"<",b)


# if a>b: #logic expretions
#     print(a,">",b)
# else:
#     if a==b:
#         print(a,"==",b)
#     else:
#         print(a,"<",b)

# if a>b: #logic expretions
#     print(a,">",b)
# elif a==b:
#     print(a,"==",b)
# else:
#     print(a,"<",b)

# #logic_value =>  predicate

# str1="Python"   #True
# str2=""         #False
# number1=23      #True
# number2=0       #False
# if str1: #
#     print("it is true") #true
# else:
#     print("it is false")

# """
# switch => match
# ==================
# match term:
#     case pattern-1:
#         action-1
#     case pattern-2:
#         action-2
#     case pattern-3:
#         action-3
#     ...
#     case _:
#         action-default
# """

# lang=input("What program lang you want to learn?")
# match lang:
#     case "Python": #  if lang=="Python": print("You can become a Data Siencit. You create server api, webapp.. ")
#         print("You can become a Data Siencit. You create server api, webapp.. ")
#     case "JavaScript":
#         print("You can become a web developer")
#     case "Java":
#         print("You can become a mobile app developer")
#     case _:
#         print("I don't now....")
    
# # if lang=="Python":
# #     print("You can become a Data Siencit. You create server api, webapp.. ")
# # elif ..
        
# n1=6
# n2=7
# my_min=n1 if n1<n2 else n2
# print("min=",my_min,sep="", end=";")
# print("max=",n1 if n1>n2 else n2,sep="")
# print(f'suma: {n1:&^10d}+{n2}={n1+n2}')
# print(f'multiply: {n1}*{n2}={n1*n2}')
# c=3456789
# c=int(input("Input number: "))
# print(f'{c:_d}')
# print(f'{c:,d}')

# # in
# if "y" in "Python":
#     print("True")
# else:
#     print("False")

# #==================================================    
# """
# for змінна in послідовність:
#     команди 1
# else:               #відслідковує чи не було виконано  оператор break
#     команди 2
# ###########################################
# range(start, end, step) => [start,end)
# #########################################

# while logic_value: 
#     команди 1
# else:               #відслідковує чи не було виконано  оператор break
#     команди 2
# """


# # порахувати суму чисел з діапазон1 [0,10]
# suma=0
# for number in range(11):  #range(0,11,1)  
#     print(number)
#     suma+=number

# print(f'suma={suma}')

# suma=0
# i=0
# while i<=10:
#     print(number)
#     suma+=number
#     i+=1
# print(suma)


#Вивести на екран "Python" n-разів
n=3
for _ in range(n):
    print("Python")

#порахувати суму чисел від 1 до n, крім тих, що діляться на 3 і 5
# continue, break
suma=0
n=18
for i in range(n): # [0,1,2,...,17, None]
    # if not(i%3==0 and i%5==0):
    #     suma+=i
    if i%3==0 and i%5==0:
        print(f'Number %3 and %5 {i}')
        continue
    suma+=i
    print(i)
    # other operations
else: # цикл виконався повністю
    print(f'suma = {suma}')


for i in range(n):
    # if not(i%3==0 and i%5==0):
    #     suma+=i
    if i==7:
        print(f'Number {i} break cicle')
        break
    suma+=i
    print(i)
    # other operations
else: # цикл виконався повністю
    print("Cicle correctly..")
    print(f'suma = {suma}')

print(f'suma after cicle operator for = {suma}')


suma=0
i=1
while i<=10:
    if i==3 or i==7:
        # print(i)
        i+=1
        continue
    print(i,end="; ")
    suma+=i
    i+=1
print(f"\nsuma={suma}")

for i in range(1,10):
    for j in range(1,10):
        print(f'{i}*{j}={i*j}',end="    ")
    print()
    