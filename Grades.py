# Strudent Grades python POC

print("Enter 5 grades for you average: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

total = markOne+markTwo+markThree+markFour+markFive
average = total/5
print("your average is:",average)

if average>=90 and average<=100:
    print("Your Grade is A")
elif average>=80 and average<89:
    print("Your Grade is B")
elif average>=70 and average<79:
    print("Your Grade is C")
elif average>=0 and average<69:
    print("Your Grade is F")
else:
    print("Invalid Input!")


