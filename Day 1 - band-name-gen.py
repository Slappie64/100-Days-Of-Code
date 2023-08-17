# Store a welcome message in the variable welcome_message.
welcome_message = "Welcome to the Band Name Generator!"

# Print the welcome message to the console
print(welcome_message)
# Add dashes equal to the length of the welcome message.
print("-" * len(welcome_message))

# Get the users home town name and store in town_name variable.
town_name = input("Enter the town you grew up in: \n")
# Get the users pet name and store in pet_name variable. 
pet_name = input("Enter the name of your first pet: \n")

# Print a new line for better readability.
print("\n")
# Print the town_name and pet_name with a space between to the console.
print(town_name + " " + pet_name)