name = input("What is your name? : ")
print('Hi ' + name + '!')
colour = input("What is your favourite colour? : ")
print(name + ' likes the colour ' + colour.lower() + '.')
birth_year = input("What is your birth year? : ")
age = 2023 - int(birth_year)
print(name + ' likes the colour ' + colour.lower() + ' and is ' + str(age) + ' years old.')
print('\'birth_year\' has data type', type(birth_year), 'and \'age\' has data type', type(age))
