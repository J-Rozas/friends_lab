def get_name (person):
    return person ["name"]

def get_favourite_tv_show (show):
    return show ["favourites"] ["tv_show"]

def likes_to_eat (person, food):
    if food in person ["favourites"] ["snacks"]:
        return True
    else:
        return False

def add_friend (person, friend):
    person ["friends"].append(friend)

def remove_friend (person, friend):
    person ["friends"].remove(friend)

def total_money (people):
    total_money = 0
    # total_money = monies from person 1 + monies from person 2 + ...
    for person in people:
        total_money += person ["monies"]
    
    return total_money

# Take amount of money of first person, subtract given money/loan.
# Second add the second amount of money to the second person.

def lend_money (lender, borrower, loan_amount):
    lender ["monies"] -= loan_amount
    borrower ["monies"] += loan_amount

# Find each persons' fav food
# Add all fav foods together
# Return list

def all_favourite_foods (people):
    list_of_food = []
    for person in people:
        list_of_food += person ["favourites"] ["snacks"]

    return list_of_food

# Go through list of people. 
# Create a blank list.
# If 1 person has no friends, add that persons name to the list.
# Return list of friendless names.

def find_no_friends (people):
    frindless_people = []
    for person in people:
        if len(person["friends"]) == 0:
            frindless_people.append(person)
    return frindless_people

# Find each person's fav TV show.
# Create blank list.
# Identify duplicates and remove them.
# Add the list of TV shows together.
# Return the list.

# def unique_favourite_tv_shows (people):
#     list_of_shows = [] # List with unique TV shows
#     # "tv_show" = each person's fav TV show
#     # if tv_show is NOT in list_of_shows, 
#     # then add that show in list_of_shows
#     for person in people:
#         if person ["favourites"] ["tv_show"] not in list_of_shows:
#             list_of_shows.append(person ["favourites"] ["tv_show"])

#     return list_of_shows

def unique_favourite_tv_shows (people):
    list_of_all_shows = []
    for person in people:
        list_of_all_shows.append(person["favourites"]["tv_show"])
    unique_tv_shows = set(list_of_all_shows)
    return unique_tv_shows