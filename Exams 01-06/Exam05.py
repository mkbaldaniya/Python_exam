print("\n--- Python OOP Project : Employee Management System ---\n")
print("---> Choose an operation <---\n")
print("1. Create A Person")
print("2. Create An Employee")
print("3. Create A Manager")
print("4. Show Details")
print("5. Exit\n")

while True:
    choice = int(input("Enter Your Choice : "))

    match choice:
        case 1:
            class Person:
                name = None
                age = None

                def set_person(self):
                    self.name = input("Enter Name : ")
                    self.age = int(input("Enter Age : "))

                def get_person(self):
                    print(f"\nPerson created with name: {self.name} and age: {self.age}")

            def display_all_p(person_list):
                    print("\n===== All Person Details =====")
                    for p in person_list:
                        print(f"Name : {p.name}")
                        print(f"Age : {p.age}\n")


            person_data = []

            num = int(input("How Many person ? "))

            for obj in range(num):
                person_data.append(Person())

            for i in range(num):
                person_data[i].set_person()

            for i in range(num):
                person_data[i].get_person()

            # display_all_p(person_data)


        case 2:
            class Employee:
                name = None
                age = None
                employee_ID = None
                salary = None

                def set_employee(self):
                    self.name = input("Enter Name : ")
                    self.age = int(input("Enter Age : "))
                    self.employee_ID = int(input("Enter Employee ID : "))
                    self.salary = float(input("Enter Salary : "))

                def get_employee(self):
                     print(f"Employee created with name: {self.name}, age: {self.age}, ID: {self.employee_ID}, and salary: ${self.salary}\n")
            

            def display_all_e(employee_list):
                    print("\n===== All Employee Details =====")
                    for e in employee_list:
                        print(f"Name : {e.name}")
                        print(f"Age : {e.age}")
                        print(f"employee ID : {e.employee_ID}")
                        print(f"salary : {e.salary}\n")


            employee_data = []

            num = int(input("How Many Employee ? "))

            for obj in range(num):
                employee_data.append(Employee())

            for i in range(num):
                employee_data[i].set_employee()

            for i in range(num):
                employee_data[i].get_employee()

            # display_all_e(employee_data)
        case 3:
            class Manager:
                name = None
                age = None
                employee_ID = None
                salary = None
                department = None

                def set_manager(self):
                    self.name = input("Enter Name : ")
                    self.age = int(input("Enter Age : "))
                    self.employee_ID = int(input("Enter Employee ID : "))
                    self.salary = float(input("Enter Salary : "))
                    self.department = input("Enter Department : ")

                def get_manager(self):
                      print(f"Manager created with name: {self.name}, age: {self.age}, ID: {self.employee_ID}, salary: ${self.salary}, and department: {self.department}\n")

            

            def display_all_m(manager_list):
                    print("\n===== All Manager Details =====")
                    for m in manager_list:
                        print(f"Name : {m.name}")
                        print(f"Age : {m.age}")
                        print(f"employee ID : {m.employee_ID}")
                        print(f"salary : {m.salary}")
                        print(f"department: {m.department}\n")


            manager_data = []

            num = int(input("How Many manager ? "))

            for obj in range(num):
                manager_data.append(Manager())

            for i in range(num):
                manager_data[i].set_manager()

            for i in range(num):
                manager_data[i].get_manager()

            # display_all_m(manager_data)
        case 4:
            print("\n--> Choose Details to Show <--")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            choose = int(input("Enter Your Choice : "))
            match choose:
                case 1:
                    display_all_p(person_data)

                case 2:
                    display_all_e(employee_data)
                    
                case 3:
                    display_all_m(manager_data)
                    
        case 5:
            print("Exiting the system. All resources have been freed.")
            print("Goodbye.")
            break