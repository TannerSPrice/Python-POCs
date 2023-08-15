 # have a list of fruits listed in a list
fruits = ["apple", "banana", "cherry"]
#this print will print the full list
print(fruits)

# here this list will just print out the second item in fruits list just banana
print(fruits[1]) 

# changing the value of banana to pineapple
fruits[1] = "pineapple"
# when you print out fruits banana is now pineapple
print(fruits)

# use .append in front of the list name then follow () with what item you want to add to the list
fruits.append("orange")
print(fruits)

# using the .insert method to add "lemon" as the second item in the fruits list
fruits.insert(1,"lemon")
print(fruits)

# using the .remove method to remove an item listed, want to remove pineapple 
##fruits.remove("pineapple")
##print(fruits)

# this print will print the last item in the list in a reverse index
print(fruits[-1])

# creating a second list
second_fruits = ["blueberry", "mango", "kiwi", "melon", "blackberry", "watermelon"]
# Will print items 3 4 and 5
print(second_fruits[2:5])

second_fruits.remove("blueberry") #remove blueberry
print(second_fruits) # prints list where blueberry is removed

# print the length of second fruits 
#print(len(second_fruits))

# joining lists of fruits and second_fruits
#joined_fruits = fruits + second_fruits
#print(joined_fruits)
