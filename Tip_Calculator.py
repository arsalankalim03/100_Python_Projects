print("Welcome to Tip Calculator")
Bill=float(input("What was the total bill? $"))
Percentage_tip=int(input("What percentage tip would you like to give? 10, 12, or 15?"))
Num_of_people=int(input("Among How many people Would you like to split the bill? "))
Total_tip=(Bill*Percentage_tip)/100
Total_bill=Bill+Total_tip
Tip_per_person=round(Total_bill/Num_of_people, 2)
print("Each person should pay: $"+str(Tip_per_person))