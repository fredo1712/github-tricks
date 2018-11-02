name = input ("Please enter your name: ")
print (f'Hello ,{name}')

age = input ("Please enter your age: ")
age_num = int(age)
print (f'You have lived for {age_num * 12} months')

age = int(input("Please enter your age again: "))
seconds = age * 365 * 24 * 60 * 60
print (f'You have lived for {seconds} seconds')