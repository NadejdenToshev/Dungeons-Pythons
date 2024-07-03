from random import randint
from item import Sword, Shield

""" 
A class to represent a game character with health, position and combat capabilities.
Parameters:
position (list): The initial position of the character on the grid.
"""
class Character:
    """
    Initialize  a character with default health, postion and no combat bonuses.
    """
    def __init__(self, position):
        self.health = 100
        self.position = position
        self.bonus_atttack = 0
        self.bonus_deffence = 0
    
    """
    Check if the character is alive.
    Returns:
    bool: True is health is greater than 0, False otherwise.
    """
    def alive(self):
        return self.health > 0

    """
    Calculate the attack power based on a dice roll
    Returns:
    int: The attack power determined by the dice roll.
    Raises:
    Exception: If the character is dead.
    """
    def attack(self):
        if not self.alive():
            raise Exception('Character is dead')

        dice = randint(0, 3)  
        attack_power = [0, 10 + self.bonus_attack, 25 + self.bonus_attack]
        return attack_power[dice]

    """
    Calculate the defence effect based on a dice roll and reduce health accordingly.
    Parameters:
    attack_power (int): The incoming attack power.
    """
    def deffence(self, attack_power):
        dice = randint(0, 2)   
        defence_points = [attack_power, attack_power // 2 - self.bonus_deffence]
        self.health -= defence_points[dice]

    """
    Move the character in the specified direction.
    Parameters:
    direction (str): The direction to move ('left', 'right', 'up', 'down').
    Raises:
    Exception: If the character is dead or the direction is invalid.
    """
    def move(self, direction):
        if not self.alive():
            raise Exception('Character is dead')

        offset = [0, 0]
        if direction == 'left':
            offset[1] = -1
        elif direction == 'right':
            offset[1] = 1
        elif direction == 'up':
            offset[0] = -1
        elif direction == 'down':
            offset[0] == 1
        else:
            raise Exception('Invalid direction')

        self.position = [self.position[0] + offset[0],
                         self.position[1] + offset[1]]
        
"""
A class to represent monster, inheriting from Character and adding inventory management.
"""
class Monster(Character):
    """
    Initialize a monster with default attributes and an empty inventory.
    Parameters:
    position (list): The initial position of the monster on the grid.
    """
    def __init__(self, position):
        super.__init__(position)
        self.inventory = {
            'sword': None,
            'shield': None,
            'boots': None,
            'small health portion': None,
            'big health portion': None
        }

    """
    Move the monster in the specified direction. 
    If the monster has boots, it moves an extra step.
    Parameters:
    direction (str): The direction to move ('left', 'right', 'up', 'down').
    """
    def move(self, direction):
        super.move(direction)
        if self.inventory['boots']:
            super.move(direction)

    """
    Add an item to the monster's inventory and update combat bonuses.
    Parameters:
    item (object): The item to add (Sword or Shield)
    """
    def get_item(self, item):
        if type(item) is type(sword):
            self.inventory['sword'] = item
        elif type(item) is type(shield):
            self.inventory['shield'] = item
        # Update combat bonuses based on inventory
        self.bonus_attack = (self.inventory['sword'] or {'power':
            0})['power']
        self.bonus_defence = (self.inventory['shield'] or {'defence':
            0})['defence']


