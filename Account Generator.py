# Account Generator 

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  account_name = first_name[0:3] + last_name[0:3] # takes the first three letters of the first and last name and concatenates them together
  return account_name # returns the generated account name

new_account = account_generator(first_name, last_name)

print(new_account)