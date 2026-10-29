height = int(input("what is your height in cm?: "))
bill = 0 
if height > 150:
    print("you can ride the coaster!!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print(f"you have to pay 5.")
    elif age <= 18:
        bill = 8
        print(f"you have to pay $8. ")
    else:
        bill = 12
        print("you have to pay $12.")

    click=input("If you want to have photo? Type y for YES and n for NO ")
    if click == "y":
        bill += 3
        print(f"Your final bill is ${bill} ")

else:
    print("Sorry, you have to grow taller before you can ride")

