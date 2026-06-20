employees = {}
def add_employee():
    print("\n----Add Employee----")
    while True:
        emp_id = int(input("enter employee id: "))
        if emp_id in employees:
            print("employee id already exist!")
        else:
            break
            name = input("enter employee name: ")
            age = int(input("enter age of the employee: "))
            department = input("enter employee department: ")
            salary = int(input("enter employee salary: "))
            employees[emp_id] = {"Name" : name, "Age" : age, "Department" : department, "Salary" : salary}
            print("Employee added succesfully")

def view_employees():
    print("\n----Employee Records----")
    if len(employees) == 0:
        print("No employee available")
        return
    print("-" * 70)
    print(f"{'ID':<10}{'Name':<20}{'Age':<10}{'Department':<15}{'Salary':<15}")

    for emp_id, details in employees.items():
        print(f"{'ID':<10}"
              f"{'Name':<20}"
              f"{'Age':<10}"
              f"{'Department':<15}"
              f"{'Salary':<15}")
        print("-" * 70)

def search_employee():
    print("\n----Search Employee----")

    emp_id = int(input("enter employee id to search: "))
    if emp_id in employees:
        print("\nEnployee Found")
        print("ID :",emp_id)
        print("Name :",employees[emp_id]["name"])
        print("Age :",employees[emp_id]["age"])
        print("Department :",employees[emp_id]["department"])
        print("Salary :",employees[emp_id]["salary"])
    else:
        print("employee not found")

def main_menu():
    while True:
        print("\n====Employee Mangement System====")
        print("1. Add Employee")
        print("2. View all Employee")
        print("3. Search employee")
        print("4. Exit")

        choice = int(input("enter your choice(1-4): "))
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print("\nThank you for using Employee mangement system")
            break
        else:
            print("Invaild choice")