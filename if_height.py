height = int(input("what is your height in cm?: "))
if height > 150:
    print("you can ride the coaster!!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $8. ")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you can not ride")


x = int(input("Enter the number: "))
if x%2 == 0:
    print("No is even")
else:
    print("No is odd")