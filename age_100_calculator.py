# asking a user to enter his/her name
name = str(input('enter your name '))

# asking a user to enter his/her birth year
birth_year = int(input('enter your birth year '))

# asking a user to enter current year
current_year = int(input('enter current year '))

# calculating a user's age by subtracting his year of birth from the current year
age = current_year - birth_year

# calculating the amount of years left until the user is 100 years old
left_to_live_till_100 = 100 - age

# calculating the year when the user is going to be 100 y/o by adding current_year to left_to_live_till_100
one_hundred_birthday = current_year + left_to_live_till_100

print(f'{name}, you are {age} years old, you are going to be 100 years old in {one_hundred_birthday}')
