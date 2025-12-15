print("Welcome to the Pattern Generator And Number Analyzer!\n")

while True:
    print("---> Select An Option <---\n")
    print("--> 1. Generate A Pattern")
    print("--> 2. Analyze a Range of Numbers")
    print("--> 3. Exit\n")

    choice = int(input("Enter your choice Number: "))

    match choice:
        case 1:
            print("Pattern :\n")
            num = int(input("Enter Your Pattern Number: "))

            for i in range(1, num + 1):
                for j in range(1, i + 1): 
                    print("*", end=" ") 
                print()

        case 2:
            print("Analyze is Here\n")
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            
            total = 0

            for num in range(start, end):
                if num % 2 == 0:
                    print(f"{num} - Even")
                else:
                    print(f"{num} - Odd")

                total += num

            print(f"Sum Of All Numbers From {start} to {end} is: {total}")

        case 3:
            print("Exiting The Program. Goodbye!")
            break  

        case _:
            print("Invalid choice, please try again.")
