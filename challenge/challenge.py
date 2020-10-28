# Write a short program that prints one of several messages to the user based on their input.

# First, prompt the user about whether they want to continue or not.

# If the user responds with either no or n, print the phrase Exiting.

# Match the following output in this no scenario. The user entered no when prompted.

userInput = input('Would you like to continue? ')

if userInput == 'no' or userInput == 'n':
    print('Exiting')
elif userInput == 'yes' or userInput == 'y':
    print('Continuing ...\nComplete!')
else:
    print('Please try again and respond with yes or no')
    
