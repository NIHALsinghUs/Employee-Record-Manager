# Import Pandas library
import pandas as pd  

# Display application title
print("--- Employee Record Manager ---")

print("-----------------------------------")

# Create an empty DataFrame
task = pd.DataFrame(columns=['Name', 'Age', 'Salary', 'Department'])

# Main program loop
while True:

    # Display menu options
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Remove Employee")
    print("4. Exit")
    print("-----------------------------------")

    # Get user choice
    userchoice = int(input("Enter the option : "))

    # Add Employee
    if (userchoice == 1):

        # Loop to add multiple employees
        while True:
            print("-----------------------------------")

            # Take employee details as input
            name = input("Enter the Employee Name : ")
            age = int(input("Enter the age of Employee : "))
            salary = int(input("Enter the salary of Employee : "))
            department = input("Enter the Department of Employee : ")

            # Add employee data to DataFrame
            task.loc[len(task)] = [name , age , salary , department]

            # Display current DataFrame
            print(task.to_string(index = False))
            print("-----------------------------------")

            # Ask user whether to add another employee
            choice = input("Add another employee? (y/n): ")

            # Save data and exit Add Employee loop
            if choice.lower() == 'n':
                task.to_csv("employees.csv")
                break

            print("-----------------------------------")

    # View Employee
    elif (userchoice == 2):

        try:

            # Ask for file name or path
            file = input("Enter the file name Or location : ")

            # Read employee data from CSV file
            task = pd.read_csv("employees.csv")

            # Display employee records
            print(task.to_string(index=False))

        # Handle file not found or other errors
        except:
            print("Employee Not Found")

    # Remove Employee
    elif (userchoice == 3):

        # Ask for employee name to remove
        name = input("Enter the EMP Name : ")

        # Read employee data from CSV
        task = pd.read_csv("employees.csv")

        # Remove matching employee records
        task = task.drop(task[task.Name == name].index)

        # Save updated data back to CSV
        task.to_csv("employees.csv", index=False)

        print("-----------------------------------")

        # Display updated employee list
        print(task.to_string(index=False))

    # Exit program
    elif (userchoice == 4):
        break

    # Handle invalid menu option
    else:
        print("-----------------------------------")
        print("Invalid option")
        print("-----------------------------------")