list1=[]
print(list1)
list2=list()
print(list2)
list3=[5,6,8]
print(list3)
input_str=input("Введіть рядок чисел  через пропуск:\n")
list4=input_str.split()
print(f'list4: {list4}')
# print(f'sum: {sum(list4)}') #TypeError
# метод включення -  скороченого синтаксису створення списку
list4_number=[int(number) for number in list4]
print(f'sum: {sum(list4_number)}') #TypeError
# OR
list4_number_v2=[]
for number in list4:
    list4_number_v2.append(int(number))
print(f'sum: {sum(list4_number_v2)}') #TypeError

import random
list5_random=[random.randint(1,10) for _ in range(10)]
print(f'{"*"*10}list5_random{"*"*10}')
print(list5_random)
list6_random=list5_random
list6_random.append(555)
print("list5_random:",list5_random)
print("list6_random:",list6_random)

list7_random=list5_random.copy()   # <=> list7_random=list5_random[:]
print("list5_random:",list5_random)
print("list7_random:",list7_random)
list7_random.append(444)
print("AFTER CHANGE:\nlist5_random:",list5_random)
print("list7_random:",list7_random)
list7_random.append([22,33])
list8_random=list7_random[:]
print("list7_random:",list7_random)
print("list8_random:",list8_random)
list8_random[0]=777
list8_random[-1][0]=222
print("AFTER CHANGED:\nlist7_random:",list7_random)
print("list8_random:",list8_random)

import copy
# глибоке копіювання
list9_random=copy.deepcopy(list8_random)
list9_random[-1][0]=22222
print("AFTER CHANGED:\nlist8_random:",list8_random)
print("list9_random:",list9_random)

import re 
# str1=input("Введіть речення:")
str1="Існує спосіб, вилучити елемент-зі списку з Урахуванням його індексу замість його значення:del оператор."
words=str1.split()
words_re=re.split(r"[\s+|,|.|:|-]",str1)
print(words)
print(words_re)
words_re=[word for word in words_re if len(word)>0]
print(id(words_re))
words_re.sort(key=str.lower,reverse=True)
# print(words_re)
print(id(words_re))
# print(sorted(words_re,key=str.lower))
# 

# tuple
info_user=("admin","Qwerty-1")
print(info_user.count("admin"))
info_user1=("guest",)
print(type(info_user1))
user1,password="tata","Qwerty-1"
print(user1, password)
user_admin,pw=info_user
print(user_admin, pw)
tuple1=tuple(words_re)
print(tuple1)
print("username:",info_user[0])
# info_user[0]="guest2"
print("username:",info_user[0])

students=["user1", "user2","user3"]
tuple_student=enumerate(students)
print(f"list=> {list(tuple_student)}")
tuple_student=enumerate(students,start=1)
print(f"tuple=>{tuple(tuple_student)}")
import string
for i in enumerate(string.punctuation):
    print(i)

tuple_country=(("Rivne", 1200,300000 ),("Kyiv",820,10000000))
for city in tuple_country:
    print(city)
    name_city, year,population=city
    print(f" City: {name_city}, year: {year}, population: {population}")

for  name_city, year,population in tuple_country:
    print(f" City: {name_city}, year: {year}, population: {population}")    

