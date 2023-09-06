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

while True:
    new_score = input("What is the new score? > ")

    if new_score.isnumeric():
        new_score = int(new_score)
        if new_score >= 1 and new_score <= 5:
            break
        else:
            print("Please rate between 1 and 5!")
    else:
        print("Please enter a number 1-5! (ex. 4)")


sorted_ratings[new_name] = new_score

restaurant_tuples = tuple(sorted_ratings.items())

sorted_tuples = sorted(restaurant_tuples)

print(sorted_tuples)

for restaurant in sorted(sorted_ratings): # if you plug a dict into sorted, you get back an iterator with the sorted keys
    print(restaurant, sorted_ratings[restaurant])

# print(sorted_ratings.items())

# print(sorted_ratings)