# Formatting for an electronic store:


data = "14inch l@ptop,699|16inch l@ptop,999|sm@rtphone,1099|t@blet,499|g@ming pc,1999" 
device_list = data.split("|") # taking the string and int variable above and converting them into a list
formatted_list = [] # is an empty list with nothing in it so we can format it for later
for device in device_list: # creating a for loop to go inisde of device list and add values inside of it
 device_info_list = device.split(",") # creating a variable and assigning a splitting value of comma inside of it
 name = device_info_list[0] # name variable with 0 to start at the beginning of the list 
 price = int(device_info_list[1]) # price is going to start after name as the second value going inside of formatted list
 new_price = int(price * 1.1); # here is a scenario that inflation and raised the prices to go up by 10% so we are increasing the value of laptops by 10%
 formatted_device = f"Device Name: {name}, Device Price: ${price}" # is a formmated variable that is going to have the new formatted info when we print it out, I later did it ouside to test it
 corrected_formatted_device = formatted_device.replace("@","a") # using this scenario as a manager's a key was broken and used '@' to replace a. so here we will replace @ for a 
 formatted_list.append(corrected_formatted_device) # here is adding the corrected formatted device into formatted list
print(formatted_list) # print will go outside of the for loop and console should print out the proper formatted list as needed.
