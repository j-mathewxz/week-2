# week 2 code

# Task 1

Name=input("Hello, what is your name? ")
print("Hello, " + Name + ". Good to meet you!") # string concatenation using f string i could do print(f"Hello, {Name}. Good to meet you!")

# Task 2
Celsius=input("Enter the temperature in celsius? ")
fahrenheit=float(Celsius)*1.8+32
print(f"{Celsius}C is equivalent to {fahrenheit}F.")

# Task 3
Students=int(input("How many students? "))
RequiredGroup=int(input("Required group size? "))

full_groups = Students // RequiredGroup
leftover = Students % RequiredGroup

student_text = "student" if leftover == 1 else "students"
group_text = "group" if full_groups == 1 else "groups"

print(f"There will be {full_groups} {group_text} with {leftover} {student_text} left over.")

# Task 4

StudentSweets=int(input("How many students? "))
TotalSweets=int(input("How many sweets are there? "))
sweets_per_student = TotalSweets // StudentSweets
leftoversweets = TotalSweets % StudentSweets

sweets_text = "sweet" if leftoversweets == 1 else "sweets"
print(f"Each student will get {sweets_per_student} sweets. ")
print(f"There will be {leftoversweets} {sweets_text} left over.")