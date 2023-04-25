## user_age = int(input("Enter your age: "))
## months = user_age * 12
## print(f"Your age {user_age} years is equal to this many {months} months")



l = ["bob", "jae", "anne"]

## tuples - can't modify tuple. ## if 1 value needs to end in comma. Because the brackets are for mathematical pemdas preference. Python needs comma to know with 1 value it is a tuple. May be other values behind it. 
t = ("forest", "jill", "mac") 

## can't have duplicates, but can modify. Unlike other 2, doesn't care about order
s = { "john", "paul", "jones"}

## l[0] is subscript notation
## print(l[0])

## sets do not have order so can't go by index

## l.append("ricku")
## l.remove("bob")

## s.add("Rucki")

## Advanced Set operators
friends = {"Bob", "Rolf", "Anne"}
aboard = {"Bob", "Anne"}

## removes aboard friends
local_friends = friends.difference(aboard)

## print(local_friends)

## s.union unites sets and gives total

## s.intersection finds intersecting values in 2 sets (same items)


## Booleans 
## print(5 == 5), print(10 != 10), print(tuple === tuple)

## IS keyword is not the same as ==, because IS checks if two elements are exactly the same, not if they are similar -- doesn't matter if same value. 

## if statements
## if day_of_week == "monday": 
## must indent here - use 4 spaces to be consistent

## input("something").lower()

number = 7
# user_input = input("Enter 'y' if you would like to play: ").lower()



# if user_input == "y":
# while user_input != "n":
# while True:
#   user_input = input("wOULD YOU LIKE TO PLAY? (Y/n)")
  
#   if user_input == "n":
#       break
#   user_number = int(input("Guess our number: "))
#   if user_number == number:
#       print("You guessed correctly!")
#       ## abs gets absolute value - no need for in below if youse abs, just example 
#   elif abs(number - user_number) in (1,-1):
#       print("You were off by one.")
#   else:
#       print("Sorry, it's wrong!")

# friends = ["ross", "jim", "ted", "mary"]

# # for friend in friends:
# for friend in friends:
#     print(f"{friend.capitalize()} is my friend")

grades = [67, 85, 99, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

# print(total/ amount)

# or do sum(grades) this doesn't need looping

#  LIST

numbers = [1,3,5]
# Looks reversed, but it isn't
# num * 2 goes into new list
doubled = [x * 2 for x in numbers]
# print(doubled)
#  same as:
# for num in numbers: 
#     doubled.append(num * 2)

friends = ["Rolf", "Sam", "Samanthha", "Sog", "Jen"]

starts_s = [friend for friend in friends if friend.startswith("S")]

# Same as: 
# for friend in friends:
#     if friend.startswith("s"):
#         starts_s.append(friend)

# print("friends ", id(friends), "starts_s ", id(starts_s) )

#  Dictionaries
# Assoc. keys and value together
friend_ages = { "Rolf": 24, "Adam": 30, "Anne": 27 }
# print(friend_ages["Rolf"])
# friend_ages["Rolf"] = 74
# print(friend_ages["Rolf"])

# for friend in friend_ages:
#     print(f"{friend} is {friend_ages[friend]}")

# prefered way - items() provides 2 values 
# The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as **tuples** in a list.
# for friend, ages in friend_ages.items():
#     print(f"{friend} is {ages}")
    
    #  IN keyword allows to check keys
# if "Rolf" in friend_ages:
#     print(f"Rolf is {friend_ages['Rolf']} old")
# else:
#     print("Rolf is not a firend")

# if you want VALUES
friend_age_values = friend_ages.values()

# print(sum(friend_age_values))

# destructuring 
# tuples
t = 5, 11
x, y = t
# print(x,y)

# print(list(friend_ages.items()))

people = [("Bob", 34, "Teacher"), ("Jill", 23, "Lawyer")]
# can do people people[0]
for name, age, profession in people:
    print(f"{name} is {age} old and works as a {profession}")

# ignore a variable when destructuring
# print(name, _, profession = person)

# destructuring to separate into 2 list - first element and the rest
# * ASTERISK collects all destructured that isn't head OR if you place it in front of head then head collects all values that is not tails
*head, tail = [1,2,3,4,5]
print(f"first: {head} and rest: {tail}")


