first_name =input("Please enter your first name\n")
last_name =input("Please enter your last name\n")
CNIC_number = input("Please enter your CNIC number\n")
age = input("Please enter your age\n")
print("your name is " + str(first_name) + str(last_name) + "\n" + "your CNIC_number is " + str(CNIC_number) + "\n" +"your age is " + str(age))
if int(age) > 18:
    print("congratulations you can vote")
elif int(age) < 18 and int(age) > 10:
    print("Sorry you can not vote")
else:
    print("you are a kid")


