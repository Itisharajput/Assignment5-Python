# Task 1
student = {'Ram': 89,
           'Rohan': 87,
           'Jevan': 88,
           'Itisha': 100,
           'Priya': 87}

name = input("Enter the student's name :")
if name in student:
    print(f"{name}'s marks : {student[name]}")
else:
    print("Student not found.") 


# Task 2

numbers = [1,2,3,4,5,6,7,8,9,10]
print(f" Original list : {numbers}")

Extracted_nums = numbers[0:5]
print(f"Extrected first five elements: {Extracted_nums}")

reversed_nums = Extracted_nums[::-1]
print(f"Reversed exteacted elements:{reversed_nums}")
