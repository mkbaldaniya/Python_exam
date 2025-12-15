# program flow

#Welcome Message
print("Welcome to the Interactive Personal Data Collector!")

#inputs
Name = input("Enter Your Name : ")
Age = input("Enter Your Age : ")
Height = input("Enter Your Height : ")
Favourite_no = input("Enter Your Favourite No :  ")

#Collected Data
print("Thank you! Here is the information we collectted")

print(f"Name : {Name}                 Type is : {type(Name)}         Memory Address : {id(Name)}")

print(f"Age is : {Age}                Type Is : {type(Age)}          Memory Address : {id(Age)}")

print(f"Height is : {Height}          Type Is : {type(Height)}       Memory Address : {id(Height)}")

print(f"Favourite No : {Favourite_no} Type Is : {type(Favourite_no)} Memory Address : {id(Favourite_no)}")


print(f"Your Birth Year is Approximately : {2025 - int(Age)} Base On Your Age of {Age}")

#thank you message
print("Thank you for using the personal data Collector. Goodbye!")



