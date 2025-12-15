print("Welcome to the Data Analyzer And Transformer Program\n")

print("===> Main Menu <===\n")
print("1. Input Data")
print("2. Display Data Summary(Built in Function)")
print("3. Calculate Factorial (Recursion)")
print("4. Filter Data By TheReshold (Lambda Function)")
print("5. Sort Data")
print("6. Display Dataset Statastics (Return Multiple Value)")
print("7. Exit Program\n")


while True:
    
    choice = int(input("Enter Your Choice Number : "))

    match choice:
        case 1:
            data_num =int(input("enter data number : "))
            arr = []
            for i in range(data_num):
                print(f"Data Count Number--> {i+1}\n")

                a = int(input("Enter Number : "))
           
                arr.append(a)
          
            print("\n-->", arr)

            print("\nData has been Stored Successfully!")
        case 2:
            def dataset():
                print("\nDataset Statistics :")

                return (f"--> Minimum Value : {min(arr)}",
                        f"--> Maximum Value: {max(arr)}",
                        f"--> Sum of All Value : {sum(arr)}",
                        f"--> Average Value : {sum(arr)/data_num}")

            minimum, maximum, sum_all, average = dataset()
            print(minimum)
            print(maximum)
            print(sum_all)
            print(average)

        case 3:
            def factorial():
                print("\nThe Factorial is :")
                num = int(input("Enter a Number to calculate factorial: "))
                factorial = 1

                if num < 0:
                    print("Factorial does not exist for negative numbers")
                elif num == 0:
                    print("The factorial of 0 is 1")
                else:
                    for i in range(1, num + 1):
                        factorial *= i
                    return f"--> Factorial of {num} is {factorial}"

            fact = factorial()
            print(fact)

        case 4:
            f_input = int(input("Enter a threshold value to filter out data above this value : "))

            f_arr = list(filter(lambda x: x >= f_input, arr))
            print(f"\n--> Filtered Data(values >={f_input}) <--\n")
            print("-->", f_arr) 

            

        case 5:
            def sort_array(arr):
                print("\n--> Choose Sorting Option <--")
                print("\nPress 1 For Ascending")
                print("Press 2 For Descending")
                
                sort_input = int(input("Choose Sorting Num : "))

                match sort_input:
                    case 1:
                        print("\nAscending :")
                        print(sorted(arr))
                    case 2:
                        print("\nDescending :")
                        print(sorted(arr, reverse=True))
            sort_array(arr)


        case 6:
            def dataset():
                print("\nDataset Statistics :")

                return (f"--> Minimum Value : {min(arr)}",
                        f"--> Maximum Value: {max(arr)}",
                        f"--> Sum of All Value : {sum(arr)}",
                        f"--> Average Value : {sum(arr)/data_num}")

            minimum, maximum, sum_all, average = dataset()
            print(minimum)
            print(maximum)
            print(sum_all)
            print(average)
                    

        case 7:
            print("\nThank You For Using the Data Anlyzer And Transfomer Program. Goodbye!")
            break

        case _:
            print("Entered Number Is Invalid.")