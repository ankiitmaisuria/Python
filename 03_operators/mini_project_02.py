#Assignment Operators
x = 5
x+=2 #x = x + 2
print(x)
x-=2 #x = x -2
print(x)
x*=2 #x = x * 2
print(x)
x//=2 #x = x // 2
print(x)
x%=2 #x = x%2
print(x)
x**=2 #x = x ** 2
print(x)
x&=2
print(x)

x|=2
print(x)

#very important
"""
The Walrus Operator ':='
Python 3.8 introduce this operator. It assigns value to variable as part of a large expression.
"""
numbers = [1,2,3,4,5]

if(count := len(numbers)) > 3 :
    print(f"The list has {count} elements.")