#Arbitrary arguments (*args)

def sports(*args):
    for arg in args:
        print(arg)
sports("Football","Cricket")