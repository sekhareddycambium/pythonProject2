# Sekhar = int(input("ENter your score"))
# if  Sekhar>=90:
#     print("your score is >90 and grade is A")
# elif 80 <= Sekhar <= 89:
#     print("your grade is B")
# elif 70<= Sekhar <=79:
#     print("your grade is C")
# elif 60<= Sekhar <=69:
#     print("your grade is D")
# else:
#     print("""your grade is F  "you are FAIL" """)

#Check whether a given year is a leap year or not.

year =int(input("Enter year : "))
if year % 100 == 0 :
    if year % 400 == 0:
        print("Give year is leap year")
    else:
        print("Given year is Not leap year")
elif year % 4 ==0:
    print("it's leap year")
else:
    print("It's not leap year")