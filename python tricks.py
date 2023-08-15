# some python tricks that I picked up playing around and messing with Twitch emote names



# swapping numbers in place
x,y = 8, 4
print(x,y)
x,y = y,x # this will swap the numbers
print(x,y) #prints the swapped numbers
a,b,c = 1,2,3 #example using 3 numbers
print(a,b,c)
a,b,c = c,a,b
print(a,b,c)

#scrambling words in a string
import random

str = ["shuffle these words"]
print(str)
str = [''.join(random.sample(word, len(word)))for word in str] #this will scramble words in the list above using the random import
print(str)



str = " this is a reverse string"
print(str)
print(str[::-1]) #Start at the end of the string (the minus does that for you), end when nothing's left and walk backwards by 1.



list = ["Joeler", "JoelerRave", "Joeler" ,"jol", "joeliest", "Joeler","jol","JoelerRave","kekw","kek"]
print(max(set(list),key = list.count)) #using this will go through the set and see which either word or if you use number that repeats the most.


squares = [i*i for i in range(10)]
print(squares) # this will calculate square roots in the list. will print 0*0 = 0, 1*1 = 1, 2*2 = 4 and so on within the range you set
