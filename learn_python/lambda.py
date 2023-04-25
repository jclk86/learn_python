# lambda returns output, no need to specify return keyword - almost always single line or else will be complicated. Not used to perform action

add = lambda x, y: x + y
# or without variable assignment:
# print((lambda x, y: x + y)(5,7)) - like IIFE - not common usage.

# print(add(5,7))


# non lambda example
def double(x):
  return x * 2

sequence = [1,3,5,9]
# doubled = [double(x) for x in sequence] - list comprehension, likely to use this 
# doubled = [x*2 for x in sequence]
doubled = map(double,sequence) 

# Lambda example
# unreadable
# doubled_bad_lambda_ex = [(lambda x: x * 2)(x) for x in sequence]

# readable with lambda
doubled_mapped_lambda = list(map(lambda x: x * 2,sequence))
# turn to list or tuple first 
# print(doubled_mapped_lambda)

some_dics = [{ "name": "Bob", "grades": [50]}, { "name": "Missy", "grades": [100]}]

def sum_func(arr):
  if arr != None:
    total = 0
    count = 0
    for student in arr:
      total = total + sum(student["grades"])
      count = count + len(arr)
    return total / count

print(sum_func(some_dics))
      



