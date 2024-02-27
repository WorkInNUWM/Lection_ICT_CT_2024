#str
# print("Python is lang. \n\t\tIt created by \a 'Guido'\n\vIn Python for insert new row using \\n")
print("*="*20)
user_name="tata_sh"
print(user_name)
print(f"symbol by index 2 is {user_name[2]}")
# user_name[2]="T" #TypeError 'str' object does not support item assignment
print(f"symbol by index 2 is {user_name[2]}")
new_user_name=user_name[:2]+user_name[2].upper()+user_name[3:]
print(new_user_name)
print(f"last symbol {new_user_name[-1]}")
last_index=len(new_user_name)-1
print(f"last symbol {new_user_name[last_index]}")
print(f"revers str => {new_user_name[::-1]}")

for symbol in "Python":
    print(symbol)

import string
# print(string.punctuation)
# for symbol in string.ascii_letters:
#     print(f"{symbol} ({ord(symbol)})",end=" ")
# print()
# for i in range(256):
#     result_text=f"{i} ({chr(i)})"
#     print(result_text,end=" ")
# print()
a=34.6
b=45.89
text_for_value=f"{a}*{b}={a*b:^10.2f}"
print(text_for_value)
text_for_value2="{0}*{1}={2:y^-15_.2f}".format(a,b,a*b)
print(text_for_value2)
text_for_value3="%5.2f*%f=%.2f"%(a,b,a*b)
print(text_for_value3)

punctuation=string.punctuation
print(punctuation)
str1="переводить перший - символ; рядка. у! верхній регістр, а всі інші - в нижній;"

print(f'len={len(str1)}')
count_p=0
for b in str1:
    if b in punctuation:
        count_p=count_p+1 # count_p+=1
        print(f'{count_p} => {b}')

print(f'count punctuation in str => {count_p}')

count_p=0
for b in str1:
    if punctuation.find(b)!=-1:
        count_p=count_p+1 # count_p+=1
        print(f'{count_p} => {b}')

print(f'count punctuation in str => {count_p}')

# порахувати кількість слів в речені, розділених пропусками
# перед цим за потреби замінити інші знаки пунктуації пропуском
str_new=""
for b in str1:
    if b in punctuation:
        str_new+=" "
    else:
        str_new+=b

  
print(f'new str=> {str_new}')
words=str_new.split()
print(f'count words={len(words)}')
print(words)

str2="  retro   ".strip()
print(str2)
str2=str2.center(11,'*')
print(str2)


