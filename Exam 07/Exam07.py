from packages import Main_mod

while True:

    print(f"\n===============================\nWelcome to Multi-utility Toolkit\n===============================")
    print("Choose an option:")
    print("1. Datetime and Time Operations")
    print("2. Mathematical operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir(()))")
    print("7. Exit")
    devider = "=" *40 

    choice = int(input("Enter Your Choice : "))
    match choice:
        case 1:
            while True:
                print("\n===> Datetime and Time Operations <===")
                print("--> 1. Display Current date and time")
                print("--> 2. Calculate difference between two dates/times")
                print("--> 3. Format date into custom format")
                print("--> 4. Stopwatch")
                print("--> 5. Countdown Timer")
                print("--> 6. Back to Main Menu")
                choose = int(input("Enter Your Choice menu: "))
                match choose:
                    case 1:
                        print(Main_mod.current_time())
                        print(devider) 
                    case 2:
                        print(Main_mod.get_dates())
                        print(devider)
                    case 3:
                        print(Main_mod.Format())
                        print(devider)
                    case 4:
                        print(Main_mod.Stop_watch())
                        print(devider)
                    case 5:
                        print(Main_mod.countdown())
                        print(devider)
                    case 6:
                        break
                    case _:
                        print("Invalid option. Please select a valid option from the menu.")           
        case 2:
            while True:
                print("\n===> Mathematical Operations <===")
                print("--> 1. Calculate Factorial")
                print("--> 2. Solve Compound Interest")
                print("--> 3. Trigometric Calculations")
                print("--> 4. Area of Geometric Shapes")
                print("--> 5. Back to Main Menu")
                choose2 = int(input("Enter Your Choice menu: "))
                match choose2:
                        case 1:
                            print(Main_mod.factorial())
                            print(devider)
                        case 2:
                            print(Main_mod.compound_interest())
                            print(devider)
                        case 3:
                            print(Main_mod.trigonometric())
                            print(devider)
                        case 4:
                            print(Main_mod.geometric_area_shapes())
                            print(devider)
                        case 5:
                            break
                        case _:
                            print("Invalid option. Please select a valid option from the menu.")
        case 3:
            while True:
                print("\n===> Random Data Generation <===")
                print("--> 1. Generate Random Number")
                print("--> 2. Generate Random List")
                print("--> 3. Create Random Password")
                print("--> 4. Generate Random OTP")
                print("--> 5. Back to Main Menu")
                choose3 = int(input("Enter Your Choice menu: "))
                match choose3:
                        case 1:
                            print(Main_mod.random_number())
                            print(devider)
                        case 2:
                            print(Main_mod.random_list())
                            print(devider)
                        case 3:
                            print(Main_mod.random_password())
                            print(devider)
                        case 4:
                            print(Main_mod.generate_otp())
                            print(devider)
                        case 5:
                            break
                        case _:
                            print("Invalid option. Please select a valid option from the menu.")
        case 4: 
            print(Main_mod.generate_uuid())
        case 5:
            while True:
                print("\n===> File Operations <===")
                print("--> 1. Create a new file")
                print("--> 2. Write to a file")
                print("--> 3. Read from a file")
                print("--> 4. Append to a  file")
                print("--> 5. Back to Main Menu")
                choose4 = int(input("Enter Your Choice menu: "))
                match choose4:
                        case 1:
                            fname = Main_mod.create_file()
                            print(devider)
                        case 2:
                            Main_mod.write_to_file(fname)
                            print(devider)
                        case 3:
                            Main_mod.read_from_file(fname)
                            print(devider)
                        case 4:
                            Main_mod.append_to_file(fname)
                            print(devider)
                        case 5:
                            break
                        case _:
                            print("Invalid option. Please select a valid option from the menu.")
        case 6:
            print(dir())
        case 7:
            print(f"===============================\nThank you for using the Multi-Utility Toolkit!\n===============================")
            break
        case _:
            print("Invalid option. Please select a valid option from the menu.")