#!/usb/bin/env python
"""
Triple quotes are used for a multiline comments.
They're helpful for describing your program.
"""

"""
This is the top level.
Variables declared in the top level exist for all lower levels.
"""
import time # import another module/library
something = 10 # crunches are used for single line comments
def print_global_variable():
  print('something = ' + str(something)) # print can print strings concatenated with +
  
print_global_variable() # there's no 'argument' to this function
  
# Tis is a function
def ask_for_number():
  # anything within a method/function is indented at least once
  n = raw_input('Enter a number: ') # get string input
  try:
    n = int(n) # change type to int
  except Exception:
    print('That is not a number, returning 0.')
    n = None
  return n

# This is another function  
def display(value):
  print('That number is: ' + str(value) + '\n')

# This is another another function
def for_n_times(number):
  print('Counting up to the number: ' + str(number))
  for i in range(number):
    print('\t' + str(i))
    
# This is anther function
def if_n_is_condition(n,m):
  if (n > m):
    print('num1 > num2')
  elif (n < m):
    print('num1 < num2')
  else:
    print('num1 == num2')

# Code that comes after function(s) can use those functions
n = ask_for_number()
display(n)
m = ask_for_number()
for_n_times(n)
if_n_is_condition(n,m)
time.sleep(4)


