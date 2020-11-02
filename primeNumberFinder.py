# Beserat Tafesse Assingment 3 Part 2
# import math for square root
import math

# entering the number you'd like to check to see if Prime
x = eval(input("Enter a number. Positive numbers only: "))

# to make sure only positive numbers are put in
while x <= 0:
    x = eval(input("Sorry, positive numbers only. Enter a number: "))


# making range of i start at 2 and increase by x * sqrt so if-elif-else statements
# can check if x divisible by more than just itself
# Doesn't work for 2 or 3 so put this in there
if x == 2 or x == 3:
    print("Prime")
for i in range(2,int(math.sqrt(x)) +1):
    if x == 2:
        print("Prime")
    elif x % i == 0:
        print("Not Prime")
        break
    else:
        print("Prime")
        break

