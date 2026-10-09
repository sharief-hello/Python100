print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))

tip_percent = int(input("How much tip would you like to give? 10, 12 or 15? "))

split_people = int(input("How many people to split the bill between? "))

per_person = (total_bill + total_bill*tip_percent/100)/split_people

print(f"Each person should pay: ${per_person:.2f}")