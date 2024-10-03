# performing analysis on plant growth 
growth = [3, 1, 2, 4, 2, 3, 2] # growth variable and stored values
growth.sort() # sort to sort the list from asscending order
## print(growth) to test if the order is sorted from smallest to largest
smallest_growth = growth[0] # set the first element of the sorted list as its value.
print(f'The smallest growth in the week is: {smallest_growth}cm') # printing the smallest growth
biggest_growth = growth[len(growth) - 1] # creating biggest growth and getting the length of a list 
print(f'The biggest growth in the week is: {biggest_growth}cm') # prints the largest growth in the list
average_growth = sum(growth) / len(growth) # here is making an average so we can see the average growth of the plants
print(f'The average growth in the week is: {average_growth}cm') 

new_growth = [2, 0, 3, 2, 4, 5, 4]   # creating a new variable for another week of growth
joined_growth = growth + new_growth # joining both of the lists together named 

joined_smallest_growth = min(joined_growth) # getting the smallest growth within the joined growth list
print(f'The smallest growth in these 2 weeks is: {joined_smallest_growth}cm') 
joined_biggest_growth = max(joined_growth) # getting the largest growth wihtin the joined growth list
print(f'The biggest growth in these 2 weeks is: {joined_biggest_growth}cm')

joined_average_growth = sum(joined_growth) / len(joined_growth)  # calculating average of the joined lists
print(f'The average growth in these 2 weeks is: {joined_average_growth}cm')

joined_smallest_growth_count = joined_growth.count(joined_smallest_growth) # counting the smallest growth of the joined list
print(f'The smallest growth happened {joined_smallest_growth_count} times in these 2 weeks')

joined_biggest_growth_count = joined_growth.count(joined_biggest_growth) # counting the number of largest plant growth of the joined lists
print(f'The biggest growth happened {joined_biggest_growth_count} times in these 2 weeks')
