#Python has 2 main loops
"""
1. for loop
2. while loop
"""
name = "Ankiit Maisuria"

for char in name:
    print(char,end=", ")

val = 123456

for digit in str(val):
    print(int(digit), end=", ")

for str in range(0,len(name),2):
    print("\n"+name[str], end=", ")