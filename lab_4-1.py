#for the user to enter their first and last name
print('Enter your first name')
first_name = input()
print('Enter your last name')
last_name = input()
#for the program to put both the first and last name to make the full name
#full_name = first_name + last_name
#issue: it is only printing one name at a time or no name
full_name = input(first_name + " " + last_name)
print(full_name)