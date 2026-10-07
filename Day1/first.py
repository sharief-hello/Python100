print("Hello World!")

user_input = input("Enter Your Name: ")

print(f'Hello {user_input}')

user_age = int(input("Enter your Age: "))

if user_age>18:
    print("Adult")
elif user_age>0:
    print("Kid")
else:
    print("Enter positive value")