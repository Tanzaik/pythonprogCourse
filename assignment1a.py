#
# assignment1a.py
#
# Tanzim Amin
# 06/04/22
# In the program below, first we accept a temperature value in Celcius from the user. 
# Then converts it into a floating point value for further calculations. 
# After that, it uses this Celcius value to calculate the corresponding fahrenheit value.

# accept temperature in celcius from user and convert the same into a float value
celcius = float(input("Enter celcius temperature: "))

# now calculate the corresponding fahrenheit value
fahrenheit = celcius*1.8 + 32

# now print the results
print(celcius, "oC = ", fahrenheit, "oF")