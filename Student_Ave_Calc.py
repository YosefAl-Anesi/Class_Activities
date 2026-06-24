Choice = "y"
while Choice == "y" or Choice == "Y":
    Quiz_1 = float(input("Enter Quiz 1 mark: "))
    Quiz_2 = float(input("Enter Quiz 2 mark: "))
    Quiz_3 = float(input("Enter Quiz 3 mark: "))
    Average = (Quiz_1 + Quiz_2 + Quiz_3) / 3
    print(f"Average Mark: {Average}")
    if Average >= 50:
        print("Status: Pass")
    else:
        print("Status: Fail")
    Choice = input("Continue? Select Y/N: ")
print("Program Ended")
