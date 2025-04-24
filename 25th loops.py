# for i in range(1,50):
#     if i % 2==1:
#         print( i," ")
#     else:
#         print()

#==>display the multiplication table of a number (e.g., 5 x 1 = 5 to 5 x 10 = 50).

number =int(input("Enter number "))

for i in range(1,11):
    print(f"{number}* {i} ={number * i}")

