#!/usb/bin/env python

"""
This is a skeleton of a robot.
Very similiar to the base for the one we made in summer 2013. 
"""

import ast # import a module with import
import time as t # when importing you can rename a module to make typing easier

# It's good practice to define global values before everything else
RUN_TIME = 10

"""
A class is a collection of functions.
It works much the same as a module like math, numpy, or ast.
"""
class Robot:

  # This is the init function, it runs ONCE when the class is created
  def __init__(self):
    """
    'self' is a special object
    It is the class itself, and is passed around within
    all functions in a class
    """
    self.startup_time = t.time()
    self.mode = 'starting'   
    
  # Do an action
  def action(self, action=None):
    print(self.time_stamp + ' Doing Something: ' + str(None))    
    
  # What is the time
  def get_state(self):
    self.current_time = t.time()
    self.time_stamp = '[' + str(self.current_time - self.startup_time) + ']'
    if self.current_time - self.startup_time > RUN_TIME:
      self.mode = 'off'
    else:
      self.mode = 'running'
    print('\t' + self.mode) # \t is TAB
    
  # Turn off at end of trial
  def shutdown(self):
    print(self.time_stamp + ' Trial Run Complete')
    self.mode = 'off'

# Main
if __name__ == '__main__':
  root = Robot()
  while not (root.mode == 'off'): # check if the self.mode variable is not 'off'
    root.get_state()
    root.action()
  else:
    root.shutdown()
