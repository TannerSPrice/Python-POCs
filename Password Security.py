#simple python program that shows an account can be locked for a certin amount of time. If a hacker tried to get into the account

password_length = 6
counter = 1
permutations = 1
while counter <= password_length: #while loop has a count of password lenth and the total combinations of a the length declared
  permutations *= counter
  counter += 1
print(f"The possible combination of a {password_length}-character password is: {permutations}") #will print out the combination total in the output
attempts = 5
max_lock = permutations/attempts   #declaring a max_lock that would lock the account after the set amount of attempts
max_lock = int(max_lock)
print(f"The maximum number of times the account might be locked is {max_lock} times.") #after the amount of times it would lock
locks = 0
total_lock_time = 0     #declaring the lock time and a multiplier that will increase 
lock_time_multiplier = 5
for i in range(max_lock):       
    locks += 1
    total_lock_time += lock_time_multiplier * locks
    print(f"Your account is locked for {lock_time_multiplier*locks} minutes")   # multiplier times the amount of locks will be distributed in minutes going up by 5

print(f"Assuming the hacker only got the password right with the last possible combination, your account would have been locked for {total_lock_time} minutes in total.")
