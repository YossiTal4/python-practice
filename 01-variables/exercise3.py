# input() always returns a string, even if the user types a number
age_text = input("Enter your age: ")

# Convert the string to an integer so we can do math with it
age_number = int(age_text)

# Calculate age in 10 years
age_in_10_years = age_number + 10

print(f"In 10 years you will be {age_in_10_years} years old")