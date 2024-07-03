import unittest

class ItemTestCase(unittest.TestCase)
    def test_init(self):
        type = "Sword"
        description = "A sharp sword with a strong blade."


        effects = {
            'power': 5,
            'defence': 10,
            'health': 20,
            'movement': 3
        }

        item1 = Item(type, description, effects)
        self.assertEqual(item1.type, type)
        self.assertEqual(item1.effects, expected_effects)

    
    def test_str(self):
        type = 'swprd'
        description = "A sharp sword with a strong blade."
        effects = {
            'power': 7,
            'defence': 10,
            'health': 25,
            'movement': 1
        }
        item2 = ItemTestCase(type,description, effects)
        expectesd_str = "Sword | 'power': 7, 'defence': 10, 'health': 25, 'movement': 1 | 
        A sharp sword with a strong blade."
        self.assertEqual(str(item2), expected_str)

        
if __name__ = '__main__':
    unittest.main()