# Request input from the user to provide a dog's age in human years and convert it to an integer
h_age = int(input("Input a dog's age in human years: "))

# Check if the entered age is less than zero; if true, display an error message and exit the program
if h_age < 0:
    print("Age must be a positive number.")
    exit()
# If the entered age is 2 years or less, calculate the dog's age in dog's years using the formula 10.5 times the human years
elif h_age <= 2:
    d_age = h_age * 10.5
# For ages greater than 2, calculate the dog's age in dog's years using the formula 21 plus 4 times the remaining human years after 2
else:
    d_age = 21 + (h_age - 2) * 4

# Display the calculated dog's age in dog's years
print("The dog's age in dog's years is", d_age) 
