# While Loop Walkthrough
count = 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")



# Your code below: 

# countdown = 10

# while countdown >= 0:
#   print(countdown)
#   countdown -= 1
# print("We have liftoff!")


# ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

# ingredients_length = len(ingredients)
# index = 0

# while index < ingredients_length:
#   print(ingredients[index])
#   index += 1


# python_topics = ["variables", "control flow", "loops", "modules", "classes"]

# length = len(python_topics)
# index = 0

# while index < length:
#   print("I am learning about " + python_topics[index])
#   index += 1




# items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]

# print("Checking the sale list!")

# for item in items_on_sale:
#   print(item)
#   if item == "knit dress":
#     break

# print("End of search!")



# dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
# dog_breed_I_want = "dalmatian"

# print("Checking the list of dogs available for adoption...")

# for dog_breed in dog_breeds_available_for_adoption:
#     print(dog_breed)
#     if dog_breed == dog_breed_I_want:
#       break
# print("Found it!")




# What if we want to print out all of the numbers in a list, 
# but only if they are positive integers. We can use another common loop control statement called continue.

# for i in big_number_list:
#   if i <= 0:
#     continue
#   print(i)



# Your computer is the doorman at a bar in a country where the drinking age is 21.
# Loop through the ages list. If an entry is less than 21, skip it and move to the next entry. Otherwise, print() the age.

# ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

# for agecheck in ages:
#   if agecheck < 21:
#     continue
#   print(agecheck)




#what if we wanted to print each individual student? 
# In this case, we would actually need to nest our loops to be able to loop through each sub-list. Here is what it would look like:

# # Loop through each sublist
# for team in project_teams:
#   # Loop elements in each sublist
#   for student in team:
#     print(student)


# sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

# scoops_sold = 0

# for location in sales_data:
#   for scoops in location:
#     scoops_sold += scoops

# print(scoops_sold)


#//////////////////////////////////////////////////////////////////



#LIST COMPREHENSIONS

# SYNTAX:
# new_list = [ <expression> for <element> in <collection> ]

# grades = [90, 88, 62, 76, 74, 89, 48, 57]

# scaled_grades = [grade + 10 for grade in grades]
# print(scaled_grades)




# numbers = [2, -1, 79, 33, -45]
# doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]
# print(doubled)

#NOTE: This is a bit different than our previous comprehension since 
# the conditional if num < 0 else num * 3 comes after the expression num * 2 but before our for keyword. 
# The placement of the conditional expression within the comprehension is dependent on whether or not an else clause is used. 
# When an if statement is used without else, the conditional must go after for <element> in <collection>. 
# If the conditional expression includes an else clause, the conditional must go before for. 
# Attempting to write the expressions in any other order will result in a SyntaxError.

# numbers = [2, -1, 79, 33, -45]

# no_if   = [num * 2 for num in numbers]
# if_only = [num * 2 for num in numbers if num < 0]
# if_else = [num * 2 if num < 0 else num * 3 for num in numbers]



# heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

# can_ride_coaster = [num for num in heights if num > 161]

# print(can_ride_coaster)


#//////////////////////////////////////////////////////////////////

#LESSON END PRACTICE

# single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# squares = []

# for number in single_digits:
#   print(number)
#   squares.append(number*number)

# print(squares)

# cubes = [num**3 for num in single_digits]

# print(cubes)

