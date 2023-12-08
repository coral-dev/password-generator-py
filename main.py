import random
import constants

print("Welcome to the password generator!")
letter_num = int(input("How many letters would you like in your password?"))
symbol_num = int(input("How many symbols would you like?"))
number_num = int(input("How many numbers would you like?"))
result = ''
password_list = []

for letter in range(0, letter_num):
    password_list += random.choice(constants.letters)
for letter in range(0, symbol_num):
    password_list += random.choice(constants.symbols)
for letter in range(0, number_num):
    password_list += random.choice(constants.numbers)

random.shuffle(password_list)

for char in password_list:
    result += char

print(f"Generated Password Is: {result}")
