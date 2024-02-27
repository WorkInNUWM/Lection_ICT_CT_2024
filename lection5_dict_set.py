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

import random
list_number=[random.randint(1,11) for _ in range(20)]
print(list_number)
print(set(list_number))