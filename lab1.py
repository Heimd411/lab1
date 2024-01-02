import datetime

#Ask for name and greet person
#first = input('Enter your name:\n')
first = "John"
print(f'Hello {first}')

#Ask for last name
#last = input('What is your last name?:\n')
last = "Doe"
print(f'Nice to meet you {first} {last}')

#Multiply two numbers
number1 = int(input('Enter a number:\n'))
number2 = int(input('And another number:\n'))
print(f'Multiplying the two numbers equals {number1*number2}\n')

#Divide two numbers
print(f'If we divide both numbers we get {number1/number2}\n')

#Age from dob
yearborn = 1977
print(f'If you were born in {yearborn} then you are {datetime.datetime.today().year - yearborn} years old.\n')

#Add moms to price
price = 55
print(f'{55*1.25}')
