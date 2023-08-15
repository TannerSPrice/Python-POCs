#loops in range POC

n = int(input()) # input a number and program will loop the input and multiply its number within the list
# [x,x,x,x]
for i in range(n): # i starts at the 0 of a list 
    if(i<n): # if the number is less than n continune on looping until there are no more numbers
        print(i*i) # printing the number it is checking and multiplys itself
