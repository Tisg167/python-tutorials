#!/usb/bin/env python

"""
This is a skeleton of a robot.
Very similiar to the base for the one we made in summer 2013. 
"""

import ast # import a module with import
import time as t # when importing you can rename a module to make typing easier

# It's good practice to define global values before everything else
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
    self.start_time = t.time()
    self.mode = 'BOOT'
    self.task = {}

  def display():
    print('Hearbeat: ' + str(self.heartbeat))
    print('Mode: ' + self.mode)
    print('Task: ' + self.task)


  # Ask for user input
  def ask_for_task(self, task_type='NIL'):
    # anything within a method/function is indented at least once
    string = raw_input(task_type + ': ') # get string input
    while not self.task:
      try:
        task = ast.literal_eval(string) # change type to int
      except Exception as msg:
        print('That is not a proper task.')
        task = {}
    else:
      return task
        
  # Do an action
  def action(self, task):
    print(self.time_stamp) + task    

  # Refresh
  def refresh(self):
    self.current_time = t.time()
    self.up_time = (self.current_time - self.start_time)

  # Enter standby
  def standby(self, timeout=0):
    print(self.time_stamp + ' Trial Run Complete')
    self.mode = 'STANDBY'
    
  # Turn off completely
  def off(self, timeout=0):
    print(self.time_stamp + ' Trial Run Complete')
    self.mode = 'OFF'

# Main
if __name__ == '__main__':
  root = Robot()
  while not (root.mode == 'OFF'): # check if the self.mode variable is not 'off'
    task = root.ask_for_task()
    action = root.action(task)
    #root.queue = root.queue_task(task)
  else:
    root.off()
