#===>Take a number as input and check whether it is even or odd.
# number = int(input("ENter number : "))
# if number %2 ==0:
#     print("Give number is even")
# else:
#     print("Given number is ODD")
#from test01 import score
from test01 import score

#====>  Input a person's age and check if they are eligible to vote (18+).

# Age = int(input("Enter age : "))
# if Age >=18:
#     print("he can eligible for voting")
# else:
#     print("He can't eligible for voting")

#==>Take marks of a student (0-100) and print their grade:
#A (>=90), B (80–89), C (70–79), D (60–69), F (<60)
#Sekhar = int(input("Enter your score"))

Sekhar = int(input("ENter your score"))
if  Sekhar>=90:
    print("your score is >90 and grade is A")
elif 80 <= Sekhar <= 89:
    print("your grade is B")
elif 70<= Sekhar <=79:
    print("your grade is C")
elif 60<= Sekhar <=69:
    print("your grade is D")
else:
    print("your grade is F ' 'you are FAIL")





