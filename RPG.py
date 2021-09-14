# Python Text RPG
# TheDestroyer99
# Copyright 2021 Ayden Quinn
# 7 Hours of coding


import sys
import cmd
import os
import textwrap
import time
import random

screen_width = 100



##############
#Player Setup#
##############

class player:
  def __init__(self):
    self.name = ''
    self.hp = 0
    self.mp
    self.status_effects = []
    self.location = 'home'
    
myPlayer = player()
  
  
  
#############
#Help Screen#
#############

def help_menu():
  print('############################')
  print('# Welcome To The Text RPG! #')
  print('############################')
  print('-Use Up, Down, Left, Right  ')
  print(' To Move                    ')
  print('-Type your commands to do them')
  print('-Use "look" to inspect something')
  print('         Good Luck!         ')
  title_screen_selections()

##############
#Title Screen#
##############

def title_screen_selections():
  option = input('> ')
  if option.lower() == ('play'):
    start_game() # Placeholder
  elif option.lower() == ('help'):
    help_menu() # Placeholder
  elif option.lower == ('tos'): 
    tac_menu() # Placeholder
  elif option.lower() == ('quit'):
 sys.exit
  while option.lower() not in ['play','help','quit']:
    print('Please Enter A Valid Command')
      if option.lower() == ('play')
        start_game() # Placeholder
  elif option.lower() == ('help')
        help_menu() # Placeholder
      elif option.lower() == ('quit')
        sys.exit
  
def title_screen:
  print('############################')
  print('# Welcome To The Text RPG! #')
  print('############################')
  print('           -Play-           ')
  print('           -Help-           ')
  print('           -Quit-           ')
  print('                            ')
  print(' Copyright 2021 Ayden Quinn ')
  title_screen_selections()

  
#####
#Map#
#####
'''
 a  b  c  d
-------------
|  |  |  |  |  1
-------------
|  |  |  |  |  2
-------------
|  |  |  |  |  3
-------------
|  |  |  |  |  4
-------------
'''

ZONENAME = 'zone'
DESCRIPTION = 'desc.'
INFORMATION = 'info'
SOLVED = False
UP = 'up','north'
DOWN = 'down','south'
LEFT = 'left','west'
RIGHT = 'right','east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False, 
                 'b1': False, 'b2': False, 'b3': False, 'b4': False, 
                 'c1': False, 'c2': False, 'c3': False, 'c4': False, 
                 'd1': False, 'd2': False, 'd3': False, 'd4': False,}


###################################################################### Start Of ND ######################################################################


zonemap = {
    'a1': {
      ZONENAME = 'Home',
      DESCRIPTION = 'This is where i live.',
      INFORMATION = 'Looks the same.',
      SOLVED = False,
      UP = '',
      DOWN = 'a2',
      LEFT = '',
      RIGHT = 'b1',
                 } , 'a2': {
                   ZONENAME = 'zone',
                   DESCRIPTION = 'desc.',
                   INFORMATION = 'info',
                   SOLVED = False,
                   UP = '',
                   DOWN = 'b2',
                   LEFT = 'a1',
                   RIGHT = 'right',
                 } , 
                  'a3': {
                   ZONENAME = 'zone',
                   DESCRIPTION = 'desc.',
                   INFORMATION = 'info',
                   SOLVED = False,
                   UP = 'up','north',
                   DOWN = 'down','south',
                   LEFT = 'left','west',
                   RIGHT = 'right','east',} , 
                  'a4': {
                   ZONENAME = 'zone',
                   DESCRIPTION = 'desc.',
                   INFORMATION = 'info',
                   SOLVED = False,
                   UP = 'up','north',
                   DOWN = 'down','south',
                   LEFT = 'left','west',
                   RIGHT = 'right','east',
                 } , 
                  'b1': {
                   ZONENAME = 'zone',
                   DESCRIPTION = 'desc.',
                   INFORMATION = 'info',
                   SOLVED = False,
                   UP = 'up','north',
                   DOWN = 'down','south',
                   LEFT = 'left','west',
                   RIGHT = 'right','east',
                  } , 
                  'b2': {
                   ZONENAME = 'zone',
                   DESCRIPTION = 'desc.',
                   INFORMATION = 'info',
                   SOLVED = False,
                   UP = 'up','north',
                   DOWN = 'down','south',
                   LEFT = 'left','west',
                   RIGHT = 'right','east',
                  } , 
                  'b3': {
                   ZONENAME = 'zone',
                   DESCRIPTION = 'desc.',
                   INFORMATION = 'info',
                   SOLVED = False,
                   UP = 'up','north',
                   DOWN = 'down','south',
                   LEFT = 'left','west',
                   RIGHT = 'right','east',
                  } , 
                  'b4': {
                   ZONENAME = 'zone',
                   DESCRIPTION = 'desc.',
                   INFORMATION = 'info',
                   SOLVED = False,
                   UP = 'up','north',
                   DOWN = 'down','south',
                   LEFT = 'left','west',
                   RIGHT = 'right','east',
                 } , 
                  'c1': {
                   ZONENAME = 'zone',
                   DESCRIPTION = 'desc.',
                   INFORMATION = 'info',
                   SOLVED = False,
                   UP = 'up','north',
                   DOWN = 'down','south',
                   LEFT = 'left','west',
                   RIGHT = 'right','east',
                  } , 
                  'c2': {
                   ZONENAME = 'zone',
                   DESCRIPTION = 'desc.',
                   INFORMATION = 'info',
                   SOLVED = False,
                   UP = 'up','north',
                   DOWN = 'down','south',
                   LEFT = 'left','west',
                   RIGHT = 'right','east',
                  } , 
                  'c3': {
                   ZONENAME = 'zone',
                   DESCRIPTION = 'desc.',
                   INFORMATION = 'info',
                   SOLVED = False,
                   UP = 'up','north',
                   DOWN = 'down','south',
                   LEFT = 'left','west',
                   RIGHT = 'right','east',
                  } , 
                  'c4': {
                   ZONENAME = 'zone',
                   DESCRIPTION = 'desc.',
                   INFORMATION = 'info',
                   SOLVED = False,
                   UP = 'up','north',
                   DOWN = 'down','south',
                   LEFT = 'left','west',
                   RIGHT = 'right','east',
                 } , 
                  'd1': {
                   ZONENAME = 'zone',
                   DESCRIPTION = 'desc.',
                   INFORMATION = 'info',
                   SOLVED = False,
                   UP = 'up','north',
                   DOWN = 'down','south',
                   LEFT = 'left','west',
                   RIGHT = 'right','east',
                  } , 
                  'd2': {
                   ZONENAME = 'zone',
                   DESCRIPTION = 'desc.',
                   INFORMATION = 'info',
                   SOLVED = False,
                   UP = 'up','north',
                   DOWN = 'down','south',
                   LEFT = 'left','west',
                   RIGHT = 'right','east',
                  } , 
                  'd3': {
                   ZONENAME = 'zone',
                   DESCRIPTION = 'desc.',
                   INFORMATION = 'info',
                   SOLVED = False,
                   UP = 'up','north',
                   DOWN = 'down','south',
                   LEFT = 'left','west',
                   RIGHT = 'right','east',
                  } , 
                  'd4': {
                   ZONENAME = 'zone',
                   DESCRIPTION = 'desc.',
                   INFORMATION = 'info',
                   SOLVED = False,
                   UP = 'up','north',
                   DOWN = 'down','south',
                   LEFT = 'left','west',
                   RIGHT = 'right','east'
                 } } 


####################################################################### End Of ND #######################################################################


####################
#Game Interactivity#
####################
def print_location():
  print('\n' + ('#' * (4+len(myPlayer.location))))
  print('#' + myPlayer.location + '#') 
  print('#' + [myPlayer.location][DESCRIPTION])
  print('\n' + ('#' * (4+len(myPlayer.location))))
def prompt():
  print('==============================================================')
  print('What Do You Want To Do?')
  action = input('> ')
  valid_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
  while action.lower() not in valid_actions:
    print('Please Input A Valid Action.\n')
    action = input('> ')
  if action.lower() in ['move', 'go', 'walk', 'travel']:
    player_move(action.lower())
  elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
    player_examine(action.lower())
  elif action.lower() == 'quit':
    sys.exit()
def player_move():
  ask = 'Where Do You Want To Go?\n\n> '
  dest = input(ask)
  if dest == in ['up','north']:
    movement_handler
  elif dest == in ['down','south']:
    
  elif dest == in ['left','east']:
    
  elif dest == in ['right','west']:
    
  

    
###################
#Game Functinalaty#
###################
  
def start_game():
  
