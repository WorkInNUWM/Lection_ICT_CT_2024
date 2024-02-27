"""
for змінна in послідовність:
    commands_1
else:
    command_2
for(i=11; i<100; ){`
commands
i+=2
}
"""
for i in range(5):#(0,1,2,3,4)
    print(i)
    print("Hello, Python")

for _ in range(5):#(0,1,2,3,4)
    print("Hello, Python")

# range(start=0, stop, step=1)
print(list(range(3,15,2)))

for i in range(11,100,2):#(11,13,...,99)
    if i%3==0 and i%5==0:
        continue
    if i%3==0:
        print(i)
    # print("Hello, Python")

# for b in "Python":
#     print(b)


# #==========================================================
# # 1
# subjects = {
#     'science': {
#         'physics': ['nuclear physics', 'optics', 'thermodynamics'],
#         'computer science': {},
#         'biology': {}
#     },
#     'humanities': {},
#     'public': {}
# }

# print("Keys of subjects['science']: ", subjects['science'].keys())
# print("Values of subjects['science']['physics']: ", subjects['science']['physics'])
# # 2
# morse = {
#     'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
#     'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
#     'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
#     'Y': '-.--', 'Z': '--..',
#     '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
#     '7': '--...', '8': '---..', '9': '----.'
# }

# def text_to_morse(text):
#     morse_code = ''
#     for char in text:
#         if char.upper() in morse:
#             morse_code += morse[char.upper()] + ' '  
#         elif char == ' ': 
#             morse_code += '/ '
#         else:
#             morse_code += char  
#     return morse_code

# name = "Korniychuk"

# print("Прізвище у коді Морзе: ", text_to_morse(name))
# # 3
# def count_word_occurrences(sentence):
#     words = sentence.split()
#     word_count = {}
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     return word_count

# sentence = "the quick brown fox jumps over the lazy dog"
# print(count_word_occurrences(sentence))
# # 4
# def has_common_element(list1, list2):
#     for item in list2:
#         if item in list1:
#             return True
#     return False

# def get_input_list():
#     input_str = input("Введіть список через пробіл: ")
#     return input_str.split()

# list1 = get_input_list()
# list2 = get_input_list()

# print(has_common_element(list1, list2))
# # 5
# import math

# sqrt_func = lambda x: round(math.sqrt(x), 2)

# num = int(input())
# print(sqrt_func(num))
# # 6
# import math

# cube_func = lambda x: round(x ** (1/3), 2)

# num = int(input())
# print(cube_func(num))
# 7
result_set = set()

for num in range(1, 101):
    if num % 5 == 2 or num % 5 == 4:
        if num % 7 == 3:
            if num % 3 != 1:
                result_set.add(num)

print("Множина чисел, що задовольняють умови:", result_set)
# 8
def number_to_words(number):
    units_words = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens_words = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens_words = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if 1 <= number < 20:
        if number < 10:
            return units_words[number]
        else:
            return teens_words[number - 10]
    
    elif 20 <= number < 100:
        return tens_words[number // 10] + (" " + number_to_words(number % 10) if number % 10 != 0 else "")
    
    elif 100 <= number < 1000:
        return units_words[number // 100] + " hundred" + ((" and " + number_to_words(number % 100)) if number % 100 != 0 else "")
    
    elif number == 1000:
        return "one thousand"

def count_letters(word):
    word = word.replace(" ", "")
    return len(word)

def main():
    number = int(input("Введіть ціле число від 1 до 1000: "))
    if 1 <= number <= 1000:
        words = number_to_words(number)
        print(words)
        print(f"{count_letters(words)} букви знадобиться для запису англійською мовою числа {number}")

main()

