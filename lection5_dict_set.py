# dict
# key: value
# 345
# my_library={}
my_library=dict()
books={
    "Shevchenko": ["Kobzar","Katerina"],
    "Franko":["Kamenyari","Zahar Berkut"]
}

print(books)
print(books["Franko"])
print("Kobzar" in books["Shevchenko"])
print("Shevchenko books: ",books.get("Shevchenko","Input any author"))
print("keys: ",list(books.keys()))
print("items: ",list(books.items()))
print("*"*30)
for key,value in books.items(): # (key, value)
    # print(books[author])
    # pass
    print(key, value)

for book in books.items(): #кортеж (key, value)
    # print(books[author])
    # pass
    print(book)
    print(book[0],":",book[1])

print(f"{books.values()} => {list(books.values())} ")    

dict_new=dict([(i,i**3) for i in range(1,11)])
print(dict_new)

my_library["Lesya Ukrainka"]=["Lisova Pisnya"]
print(my_library)
my_library["Franko"]=books["Franko"]
# my_library["Franko"]="Franko history"
print(my_library)
my_library["Lesya Ukrainka"].append("Lis Mikita")
print(my_library)
my_library.update({"Simonenko":["Lebedi materinstva"]})

for book in iter(books):
    print(book)

print(books.setdefault("Kurt","Error!"))
print(books.setdefault("Franko","Error!"))
print(my_library)





# set-unmutable
set1=set("Python is script lang")
print(set1)

set2=set(books)
for author in books:
    print(author)
print(set2)

for book in books.items():
    print(book)
set3=set(books.keys())
# set3=set(books.values()) # if value is structure =>  error 
# set3=set(books.items()) # error
print(set3)
print(list(books.items()))
print(list(books.values())) 
print(list(books.keys()))

import random
list_number1=[random.randint(1,11) for _ in range(20)]
print(f'list_number1={list_number1}')
set_number1=set(list_number1)
print(f'set_number1={set_number1}')

list_number2=[random.randint(1,11) for _ in range(20)]
print(f'list_number2={list_number2}')
set_number2=set(list_number2)
print(f'set_number2={set_number2}')

print(len(set_number1))
print(set_number1.isdisjoint(set_number2)) 
print(set_number1==set_number2) 
print(set_number1.issubset(set_number2)) #   <=>  "<=" 
print(set_number1.issuperset(set_number2)) #   <=>  ">=" 
print(set_number1.union(set_number2)) #   <=>  " |"  
print(set_number1 | set_number2) #   <=>  " |" 
print(set_number1.intersection(set_number2)) #   <=>  " &"  
