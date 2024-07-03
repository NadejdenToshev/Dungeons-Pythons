import unittest
from unittest.mock import patch
from character.py import Character, Monster
from item import Sword, Shield

class TestCharacter(unittest.TestCase):
    def setUp(self):
        """Set up a character for testing"""
        self.character = Character(position=[0, 0])

    def test_initial_health(self):
        """Test that the character initializes with 100 health."""
        self.assertEqual(self.character.health, 100)

    def test_alive(self):
        """Test that the character is alive initallly."""
        self.assertTrue(self.character.alive())

    def test_attack(self):
        """Test the attack method returns valid attack power."""
        with patch('character.randint', return_value=1)
        self.character.bonus_attack = 5
        self.assertEqual(self.character.attack(), 15)

    def test_attack_dead(self):
        """Test the attacking a dead character raises an exceprion."""
        self.character.health = 0
        with self.assertRaises(Exception) as context:
            self.character.attack()
        self.assertEqual(str(context.exception), 'Character is dead')
    
    """Mocks the randint function to return 1 and tests the defense calculation.
    This ensures the defense method correctly reduces the character's health.
    """
    def test_defence(self):
        with patch('character.py.randint', return value=1):
            self.character.bonus_deffence = 2
            self.character.deffence(attack_power=10)
            self.assertEqual(self.character.health, 97)

    """Tests that the move method updates the character's 
    position correctly for valid directions.
    """
    def test_move(self):
        self.character.move('right')
        self.assertEqual(self.character.position, [0, 1])
        self.character.move('up')
        self.assertEqual(self.character.position, [-1, 1])

    """Ensures that the exception is raised when the character
     tries to move in an invalid direction.
     """
     def test_move_invalid_direction(self):
        with self.assertRaises(Exception) as context:
            self.character.move('invalid direction')
        self.assertEqual(str(context.exception), Invalid direction)

    class TestMonster(unittest.TestCase):
        def setUp(self):
            """Set ip a monster for testing"""
            self.monster = Monster(position=[0, 0])
            self.sword = Sword(power=10)
            self.shield = Shield(defense=5)

        def test_initial_inventory(self):
            """Test that the monster's inventory initializes correctly."""
            self.assertIsNone(self.monster.inventory['sword'])
            self.assertIsNone(self.monster.inventory['shield'])
            self.assertIsNone(self.monster.inventory['boots'])
            self.assertIsNone(self.monster.inventory['small health portion'])
            self.assertIsNone(self.monster.inventory['big health portion'])

        def test_move_without_boots(self):
            """Test the move method without boots."""
            self.monster.move('right')
            self.assertEqual(self.monster.position, [0, 1])

        def test_move_with_boots(self):
            """Test the moove method with boots."""
            self.monster.inventory['boots'] = True
            self.monster.move('right')
            self.assertEqual(self.monster.position,[0, 2])

        def get_item_sword(self):
            """Test adding a sword to the monstr's inventory and updating attack bonus."""
            self.monster.get_item(self.sword)
            self.assertEqual(self.monster.inventory['sword'], self.sword)
            self.assertEqual(self.monster.bonus_attack, 10)

        def test_get_item_shield(self):
            """Test adding a shield to the monster's inventory and updating defense bonus."""
            self.monster.get_item(self.shield)
            self.assertEqual(self.monster.inventory['shield'], self.shield)
            self.assertEqual(self.monster.bonus_defence, 5)






