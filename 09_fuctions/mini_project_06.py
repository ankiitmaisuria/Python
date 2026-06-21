#Arbitrary Keyword Arguments (**args)

def demo(**stud):
    print("Student Name : ",stud['sName'])
    print("Student Age : ",stud['age'])

demo(sName="Ronaldo" , age=40 , rank = 1)