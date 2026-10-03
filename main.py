

age=input("Enter Your Age:\n")
Years_left=90-int(age)
Days_left=Years_left*365
months_left=Years_left*12
weeks_left=round(Days_left/7)
print(f"You have {Days_left} days, {weeks_left} weeks, {months_left} months left.")