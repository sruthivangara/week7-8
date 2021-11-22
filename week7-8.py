import json
def id(): #created a function named id()
    while True:
        employee_id = input("Enter your employee ID\n")
        if employee_id == "":  #if employee id is empty
            print("Employee ID can not be empty")
        elif len(employee_id) > 7:  #if employee id is greater than 7
            print("Employee ID must be less than or 7, Enter again")
        elif employee_id.isdigit(): #it must be a number
            break
        else:
            print("Employee ID has non numberic digits")
    return employee_id  #returns data in employee_id

def e_name(): #created a function named e_name()
    while True:
        employee_name = input("Enter your name\n")
        if employee_name.strip()=="":  #if employee name is empty
            print("employee name should not be empty")
        elif employee_name.lower().replace("-","").replace("'","").replace(" ","").isalpha():  #Spaces, the ' and - character are all allowed as well.
            break
        else:
            print("please enter correct name")
    return employee_name  #returns data in employee_name      

def e_email(): #created a function named e_email()
    while True:
        employee_email = input("Enter employee email address\n")
        if len(set("!'#$%^&*()=+,<>/?;:[]{ }").intersection(set(employee_email)))>0: #if users enters these characters it will not accepct
            print("Please enter correct email address")
        elif employee_email.strip().replace("@","").replace(".","").replace("_","").isalnum(): #if user enters @._ it will accepct
            break
        else:
            print("Try again")
    return employee_email   #returns data in employee_email      

def e_salary(): #created a function named salary()
    while True:
        employee_salary = input("Enter employee salary:\n")
        try:
            employee_salary = float(employee_salary)
            if employee_salary<18 or employee_salary>27: #if user enters value less than 18 and greater than 27 it will not accepct
                print("employee salary should be in between 18 and 27")
            else:
                break
        except:
            print("salary must be a floating value")
    return employee_salary #returns data in employee_salary

employees = list()
while True:
    employee_id = id()           #calling a function id()
    employee_name = e_name()     #calling a function e_name()
    employee_email = e_email()   #calling a function e_email()
    employee_salary = e_salary() #calling a function salary()
    break

employees_list = list() #created an empty list
my_dict = {"Employee_ID":employee_id,"Employee_Name":employee_name,"Employee_Email":employee_email,"Employee_Salary":employee_salary} #create a list of dictionaries that hold all of the information.
employees_list.append(my_dict)

for i in employees_list:
    i["Employee_Name"] = "IT Department " + i["Employee_Name"]   #Add the words "IT Department" to each name in your list
    i["total_updated_salary"] = i["Employee_Salary"]*1.3         #Update salary information to be 30% higher than the number provided to reflect total salary information with benefits included
print(employees_list)

#Your code must also write out your list of employee data to a JSON file once it's done executing. Write a function to perform this action.

def item1():  #created a function named item1()
    with open('my_file.json', 'w') as f:
        for item in employees_list:
            f.write("%s\n" % item)
    return item  #returning item
item = item1()   #calling function item1()   
       