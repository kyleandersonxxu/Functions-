# Get information from the user about conversion
# TODO User input validation 
# user input on the type of conversion
# -1 user enters in --> inches to mm enter mm --> in 
#menu system 1-inches to mm 2-mm to inches 
userConversionInput = input('What type of conversion \n\t 1-inches to mm \n\t 2-mm to inches: \n')

userInput = input ('what is the number: ')
print ('Your number is:', userInput)
userNumber = float(userInput)

# Perform the conversion 
# Convert in to mm 25.4 mm in every 1 in

#Conditional statement that determines 1 or 2 
if userConversionInput == '1':
    print ('in to mm')
    # Convert from in to mm (userNumber * 25.4) (1 * 25.4) = 25.4 mm
    userAnswer = userNumber * 25.4
if userConversionInput == '2'
    print ('mm to in')
    #convert from mm to in (userNumber/25.4 )1/25.4 = 0.394
    userAnswer = userNumber/25.4
# userAnswer = userNumber/25.4

print (type(userNumber))
# Preform the conversion
# Print out the answer to the user  