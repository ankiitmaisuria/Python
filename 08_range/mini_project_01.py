#The buil-in range()
"""
range(start, stop, step)
start argument is optional
if range function is called with one argument ,the argument represents stop value
"""

x = range(10) # 0 to 9
print(x)

for n in x:
    print(n)

y = range(3,10)
print(y)
for n in y:
    print(n)

z = range(3,10,2)
print(z)
for n in z:
    print(n)