#Create a project - Take input from user to store Employee Information

emp_name = input('Enter your name: ')
job = input('Enter your job description: ')
experience = int(input('Enter your experience: '))

print(emp_name, job, experience)
print(type(emp_name), type(job), type(experience))

print("Employee Name is  ",emp_name,", work as a ",job,", has a ",experience," years of experience")
print(f"Employee = {emp_name}, job = {job}, experience = {experience}")