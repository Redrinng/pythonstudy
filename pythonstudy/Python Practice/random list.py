number_list = range(9)
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))

range_five_three = range(5, 15, 3)
print(list(range_five_three))

range_diff_five = range(0, 40, 5)
print(list(range_diff_five))

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 100)

# Your code below: 

long_list_len = len(long_list)
print(long_list_len)

big_range_length = len(big_range)
print(big_range_length)


suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]

# Your code below: 
print(beginning)


middle = suitcase[2:4]
print(middle)

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 

last = suitcase[4:6]

last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below: 

jake_votes = votes.count("Jake")
print(jake_votes)

# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]


# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
#sort(names)


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort()

addresses.sort()
print(addresses)


games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
games_sorted = sorted(games)
print(games_sorted)


inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", 
             "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", 
             "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# Your code below:
inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count("twin bed")
removed_item = inventory.pop(4)

#first the index to be inserted (one index LESS than the target index, 
#we are inserting the bed frame to be the 11th element), then the item to be inserted
inventory.insert(10, "19th Century Bed Frame")

inventory.sort()
print(inventory)
