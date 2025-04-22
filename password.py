import string
import random
letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','(',')','*']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols=int(input("how many symbols would you like in your password?\n"))
nr_numbers=int(input("How many numbers would you like in your password?\n"))

password_list=[]
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))
for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)

password=''
for char in password_list:
    password += char
print(password)