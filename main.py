print("Welcome to the Love Calculator!")
name1= input("What is your name?\n")
name2= input("What is your partner's name?\n")
combined_string=name1+name2
c_string=combined_string.lower()

l_count=c_string.count("l")
o_count=c_string.count("o")
v_count=c_string.count("v")
e_count=c_string.count("e")
love_count=l_count+o_count+v_count+e_count

t_count=c_string.count("t")
r_count=c_string.count("r")
u_count=c_string.count("u")
e_count=c_string.count("e")
true_count=t_count+r_count+u_count+e_count

Love_Score=int(str(true_count)+str(love_count))

if Love_Score<=10 or Love_Score>=90:
    print(f"Your love score is {Love_Score}, you go together like coke and mentos")
if Love_Score>=40 and Love_Score<=50:
    print(f"Your love score is {Love_Score}, you are alright together.")
else :
    print(f"Your Score is {Love_Score}")