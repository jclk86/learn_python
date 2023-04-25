def person(**kwargs):
  print(kwargs)
  
details = { "name": "Jon", "age": 25 }

person(**details)

person(name='bob', age=36)

# keyward argument **kwargs is a dictionary and you must pass in keywords

def print_nicely(*args, **kwargs):
  person(**kwargs)
  print(*args)
  # items() returns tuples
  for name, age in kwargs.items():
    print(f"{name}: {age}")

print_nicely(1,2,3, **details)