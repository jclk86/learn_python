users = [(0, "Bob", "password"),
(1, "Rolf", "bob123"),
(2, "Jose", "long4ssword"),
(3, "username", "1234")]

# like list comprehension, but get dictionary
# create mapping of above

# value is key-val pair - user[1]
username_mapping = {user[1]: user for user in users}

print(username_mapping)

# output: user[1] references the second index of tuple
# {'Bob': (0, 'Bob', 'password'), 'Rolf': (1, 'Rolf', 'bob123'), 'Jose': (2, 'Jose', 'long4ssword'), 'username': (3, 'username', '1234')}

username_input = input("Ente your username: ")
password_input = input("Enter password: ")
# underscore ignores
_, username, password = username_mapping[username_input]

# if password_input == password:
#   print("your details are correct")
# else: 
#   print("incorrect password")
