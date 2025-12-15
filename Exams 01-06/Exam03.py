print("Welcome to the Student Data Organizer!\n")

students = [
    {"id" :101, "name" : "Alice", "age" : "25", "grade" : "A+", "subject" : "Maths"},
#    {"id" : 102, "name" : "carey", "age" : "20", "grade" : "B+", "subject" : "Maths"},
#    {"id" : 104, "name" : "Charlie", "age" : "23", "grade" : "B+", "subject" : "Maths"},
#    {"id" : 105, "name" : "finch", "age" : "26", "grade" : "C+", "subject" : "Maths"},
#    {"id" : 106, "name" : "stark", "age" : "22", "grade" : "A+", "subject" : "Maths"},
#    {"id" : 107, "name" : "speed", "age" : "19", "grade" : "A+", "subject" : "Maths"},
#    {"id" : 108, "name" : "mark", "age" : "22", "grade" : "B+", "subject" : "Maths"},

]

while True:
    print("\n===> Select An Option <===")
    print("1. Add new student")
    print("2. Display all student information")
    print("3. Update student")
    print("4. Delete student")
    print("5. Display subjects offered")
    print("6. Exit")

    choice_input = input("Enter your choice (1-6): ")

    
    if not choice_input.isdigit():
        print("Please enter a number between 1 and 6.")
        continue

    choice = int(choice_input)

    match choice:
        
        case  1:
            num_input = input("Enter Number Of Student Add : ")
            if not num_input.isdigit():
                print("Invalid input. Please enter a number.")
                continue

            num_students = int(num_input)

            for i in range(num_students):
                print(f"\n--- Adding Student {i+1} of {num_students} ---")

                s_id = input("Enter ID: ")
                if not s_id.isdigit():
                    print("Invalid ID.")
                    continue
                s_id = int(s_id)

                s_name = input("Enter name: ")
                s_age_in = input("Enter age: ")
                if not s_age_in.isdigit():
                    print("Invalid age.")
                    continue
                s_age = int(s_age_in)

                s_grade = input("Enter grade: ")
                s_subject = input("Enter subject: ")

                new_student = {
                    "id": s_id,
                    "name": s_name,
                    "age": s_age,
                    "grade": s_grade,
                    "subject": s_subject
                }
                students.append(new_student)
                print("Student successfully added.")


        case 2:
            if not students:
                print("No students found.")
            else:
                print("\n--- Student Information ---")
                for s in students:
                    print(f"ID: {s['id']} | Name: {s['name']} | "
                          f"Age: {s['age']} | Grade: {s['grade']} | Subject: {s['subject']}")

        
        case 3:
            update_id_input = input("Enter student ID to update: ")
            if not update_id_input.isdigit():
                print("Invalid ID.")
                continue
            update_id = int(update_id_input)

            found = False
            for s in students:
                if s["id"] == update_id:
                    print("-->Select An option<--")
                    print("Press 1 for Update Name")
                    print("Press 2 for Update Age")
                    print("Press 3 for Update Grade")
                    print("Press 4 for Update Subject")
                    print("Press 5 for Update all Details")
                    update_data = int(input("Enter Update choice (1-4) : "))
                

                    match update_data:
                        case 1:
                            s["name"]   = input("Enter new name: ") or s["name"]
                            print("Student Name updated successfully.")
                        case 2:
                            age_in = input("Enter new age: ")
                            if age_in.isdigit():
                                s["age"] = int(age_in)
                            else:
                                print("Invalid age. Keeping previous value.")
                            print("Student Age updated successfully.")
                        case 3:
                            s["grade"]  = input("Enter new grade: ") or s["grade"]
                            print("Student Grade updated successfully.")
                        case 4:
                            s["subject"]= input("Enter new subject: ") or s["subject"]
                            print("Student Subject updated successfully.")
                            found = True
                            break
                    # if not found:
                    #     print("Student not found.")
                        case 5:
                            # update_id_input = input("Enter student ID to update: ")
                            # if not update_id_input.isdigit():
                            #     print("Invalid ID.")
                            #     continue
                            # update_id = int(update_id_input)

                            # found = False
                            for s in students:
                                if s["id"] == update_id:
                                    s["name"]   = input("Enter new name: ") or s["name"]

                                    age_in = input("Enter new age: ")
                                    if age_in.isdigit():
                                        s["age"] = int(age_in)
                                    else:
                                        print("Invalid age. Keeping previous value.")

                                    s["grade"]  = input("Enter new grade: ") or s["grade"]
                                    s["subject"]= input("Enter new subject: ") or s["subject"]
                                    print("Student updated successfully.")
                                    found = True
                                    break
                            if not found:
                                print("Student not found.")
        
        case 4:
            del_id_input = input("Enter student ID to delete: ")
            if not del_id_input.isdigit():
                print("Invalid ID.")
                continue
            del_id = int(del_id_input)

            found = False
            for s in students:
                if s["id"] == del_id:
                    students.remove(s)
                    print("Student deleted successfully.")
                    found = True
                    break
            if not found:
                print("Student not found.")

       
        case 5:
            subjects = {s["subject"] for s in students}
            print("Subjects Offered:", ", ".join(subjects))

        
        case 6:
            print("Exiting program. Goodbye!")
            break

        case _:
            print("Invalid choice. Please select a number between 1 and 6.")
