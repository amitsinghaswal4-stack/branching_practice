bill = float(input("Total bill? "))
tip_percent = int(input("What percent of tip want to givr? 10, 15, 20, 30: "))
people = int(input("No. of people: "))

tip = print(bill*(tip_percent/100))
print(f"Tip by {people} would be {tip} dollars")

