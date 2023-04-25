# many args collected in tuple
# def multiply(*args):
#   print(args)
  
# multiply(1,6,2)

#  or destructure using *, but must have sam amount of values 
def add(x, y):
  return x + y

nums = [3,5]
# print(add(*nums))

# print(*nums)
# https://realpython.com/python-kwargs-and-args/
# now destructuring DICTIONARIES
some_dic = { "x": 25, "y": 35 }

def dest(x,y):
  return x + y
  
# print(dest(**some_dic))


def multiply(*args):
  total = 1
  for arg in args:
    total = total * arg
  return total

# operator is a named keyword, so you must pass in a name to execute, can't just be value operator="*"
# remembee *args is a tuple, so if you only do multiple(args) without *, you are passing in a tuple to be multiplied. * destructures the tuple
def calc(*args, operator):
  if operator == "*":
    return multiply(*args)
  elif operator == "+":
    return sum(args)
  else:
    return "No valid operator"
  
print(calc(2,3, operator="+"))