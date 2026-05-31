x = 100
y = 200
z = 300

print(x+y+z)

print("Before swapping:")
print("x = ",x)
print("y = ",y)
print("z = ",z)

"""x, y, z = z,y,x
print("After swapping:")
print("x = ",x)
print("y = ",y)
print("z = ",z)
"""
x,y,z = y,z, x
print("After swapping:")
print("x = ",x)
print("y = ",y)
print("z = ",z)