#!/usr/bin/env/python
"""
Simple python robot with arduino
"""

# Modules
import serial, time, ast
from serial import SerialException

# Global
BAUD = 9600
DEVICE = '/dev/ttyACM0'
RUN_TIME = 10
WAIT_TIME = 1

class Robot():
  
  # Initialize
  def __init__(self):
    self.mode = 'init'
    self.start_time = time.time()
    self.arduino = serial.Serial(DEVICE, BAUD)
  
  # Determine Action
  def determine_state(self):
    self.current_time = time.time()
    self.up_time = self.current_time - self.start_time
    if int(self.up_time) != RUN_TIME: # cast into integer or else it may never shutdown (10 != 10.00001)
      self.mode = 'running'
      self.action = 'forward'
    else:
      self.mode = 'off'
      self.action = 'none'
    
  # Command Arduino
  def execute_action(self):
    try:
      self.command = self.action[0]
      self.arduino.write(self.command)
    except Exception as error:
      print(str(error))
        
  # Display
  def display_info(self):
    print('[' + str(self.up_time) + ']')
    print('\tMode: ' + self.mode)
    print('\tAction: ' + self.action)
    print('\tCommand: ' + self.command)
    
if __name__ == '__main__':
  root = Robot() # initialize robot
  while not (root.mode == 'off'):
    time.sleep(WAIT_TIME)
    root.determine_state()
    root.execute_action()
    root.display_info()
    
