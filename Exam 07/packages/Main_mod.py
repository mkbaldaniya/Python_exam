from datetime import datetime
import time
import math
import random
import uuid
import os

from datetime import datetime
def current_time():
    now = datetime.now()
    return f"Current Date and Time: {now}"


from datetime import datetime

# Date And Time Module 

def get_dates():
    start = input("Enter the first date (YYYY-MM-DD): ")
    end = input("Enter the second date (YYYY-MM-DD): ")
    
    Start = datetime.strptime(start, "%Y-%m-%d")
    End = datetime.strptime(end, "%Y-%m-%d")
    Difference = End - Start

    return f"Difference : {Difference.days} Days"
    
def Format():
    now = datetime.now()
    print("Current Date Time:", now)
    format = input("Enter custom format (%d-%m-%Y %H:%M): ")
    print("Formatted Date:",end = "")
    return now.strftime(format)


def Stop_watch():
    print("----- STOPWATCH -----")
    print("Press Enter to START")
    start = time.time()

    print("Stopwatch started (Press Enter to STOP)")
    input()
    end = time.time()

    return round(end - start, 2)
    

def countdown():
    sec = int(input("Enter seconds for countdown: "))
    for i in range(sec,0,-1):
        print(f"Time Left is: {i} sec", end="\n")
        time.sleep(1)
    print("\nTimes Up")

    return "Done"

# Mathematical Calculations Module


def factorial():

    f = int(input("Enter a number to calculate its factorial :-"))
    if f < 0:
        print("\nSorry, factorial does not exist for negative numbers")

    elif f == 0:
        print("\nThe factorial of 0 is 1")
    else:
        fact = 1
        for i in range(1,f+1):
            fact=fact*i
        return fact
def compound_interest():
    P = float(input("Enter Principal Amount: "))
    r = float(input("Enter Annual Interest Rate (in %): ")) / 100
    t = float(input("Enter time in years: "))
    A = P * math.exp(r * t)


    CI = A - P
    final_amount = round(A, 2)
    compound_int = round(CI, 2)

    return final_amount, compound_int

    # print("\n-----Compound Interest Result-----")        

def trigonometric():
    angle = float(input("Enter angle in degrees: "))
    rad = math.radians(angle)
    print("sin =", math.sin(rad))
    print("cos =", math.cos(rad))
    print("tan =", math.tan(rad))
    s, c, t = math.sin(rad), math.cos(rad), math.tan(rad)
    return s, c, t

def geometric_area_shapes():
    print("1. Area of Circle")
    print("2. Area of Square")
    ch = int(input("Enter choice: "))
    if ch == 1:
        r = float(input("Enter radius: "))
        return math.pi * r * r
    elif ch == 2:
        a = float(input("Enter side: "))
        return a * a

# Random Generation Module

def random_number():
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))
    num = random.randint(start, end)    
    print("Random Number:", num)
    return num


def random_list():
    size = int(input("\nEnter size of list: "))
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))

    lst = []
    for i in range(size):
        num = random.randint(start, end)
        lst.append(num)

    return lst


def random_password():
    print("\nChoose password type:")
    print("\n1. Digits only")
    print("2. Symbols only")
    print("3. Digits + Symbols")
    print("4. Back to Menu")

    choice = int(input("\nEnter your choice: "))
    length = int(input("Enter password length: "))

    digits = "\n0123456789"
    symbols = "\n!@#$%^&*()_+-=[]{}|;:,.<>?/"

    if choice == 1:
        chars = digits
    elif choice == 2:
        chars = symbols
    elif choice == 3:
        chars = digits + symbols
    elif choice == 4:
        return ""       
    else:
        chars = digits + symbols

    password = ""
    for i in range(length):
        password += chars[random.randint(0, len(chars)-1)]

    return password

def generate_otp():
    length = int(input("Enter OTP length (4–8): "))
    
    digits = "0123456789"
    otp = ""

    for i in range(length):
        otp += digits[random.randint(0, len(digits)-1)]

    return otp

# Generate Uuid Module

def generate_uuid():
    generated_id = uuid.uuid4()
    return f"\nGenerated UUID: {generated_id}"

# File Handling Module

def create_file():
    filename = input("Enter File Name (e.g. mydata.txt): ")
    try:
        with open(filename, 'x') as f:
            pass 
        print(f"Success: '{filename}' File Created.")
        return filename
    except FileExistsError:
        print(f"Note: '{filename}' File Alreddy Exist.")
        return filename
    except Exception as e:
        print(f"Error: {e}")

def write_to_file(filename):
    if os.path.exists(filename):
        data = input("\nWrite Content (Write Mode): ")
        try:
            with open(filename, 'w') as f:
                f.write(data)
            print("Success: Data Writed.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Error: File Not Found.")

def append_to_file(filename):
    if os.path.exists(filename):
        data = input("\nAdd Content (Append Mode): ")
        try:
            with open(filename, 'a') as f:
                f.write("\n" + data)
            print("Success: Data Appendded.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Error: File Not Found.")

def read_from_file(filename):
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                content = f.read()
            print("\n---- File Content ----")
            print(content)
            print("--------------------------")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Error: File Not Found.")
    
    
    