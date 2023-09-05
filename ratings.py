"""Restaurant rating lister."""


# put your code here
def restaurant_dictionary(filename):
    full_list = open(filename)

    split_list = []

    for row in full_list:
        #row.rstrip().split(":")
        split_list.append(row.rstrip().split(":"))

    split_list.sort()

    restaurant_ratings = {}

    for row in split_list:
        name, rating = row
        restaurant_ratings[name] = rating
    
    return restaurant_ratings

sorted_ratings = restaurant_dictionary("scores.txt")

new_name = input("What is the restaurant name? > ").title()
new_score = input("What is the new score? > ")

sorted_ratings[new_name] = new_score

restaurant_tuples = tuple(sorted_ratings.items())

sorted_tuples = sorted(restaurant_tuples)

print(sorted_tuples)

# print(sorted_ratings.items())

# print(sorted_ratings)