"""
Variable is a name that refers to store the value in memory.
In Python creating a variable is simple just write the variable name and assign the value to it.

Variable names are case-sensitive.
variable type is dynamic type that means type of variable will be-decide based on value assign to it.
You can re-assign the same variable.
variable name should be small letter.
1. a variable name must start with a letter or the underscore character
2. a variable name can not start with a number
3. a variable name can only contain alph-numeric character and underscore (A-Z ,a-z,0-9 and _)
4. a variable names are case-sensitive
5. Most important - variable name cannot be any of the python keywords.
"""


x = 20 # variable x assigned to int type
y = 30

print(x)
print(y)

print(type(x)) # To check the type of variable
print(type(y))

x = "Ankiit" #re-assign the same variable with different type - Variable re-assignment
print(x)
print(type(x))

name = 'Ankiit'
age = 35


print(name , age)
print('My name is', name, " and my age is ",age)

weight = float(95)
print(weight)

address = str('Maisuria')
print(address)

a = b = c = 100 #assign multiple variables with same value - assign same value
print(a, b, c)
# you can not do like this
#a,b,c = 100
a, b, c = 100, 200, 300    #assign multiple variables with different values at a time - Multiple assignments
print(a, b, c)

#f-string
lastname = 'Maisuria'
phone_num = 2509517193
print('Last Name is', lastname , 'and my phone number is', phone_num)
print(f'My last name is {lastname} and my phone number is {phone_num}') #example of f-String

fullname = name +" "+ lastname
details = fullname+" "+str(age)
print(fullname)
print(details)

#Getting user input

city = input('Enter your city:')
print(city)
country_code = input('Enter your country code :')
print(type(int(country_code)))


