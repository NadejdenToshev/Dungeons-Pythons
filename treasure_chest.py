import random

class Treasure_Chest:
    def __init__(self, max_items):
        self.items = []
        num_items = random.randint(0, max_items)
        possible_items = [
            Item("Sword", "+10 attack power"),
            Item("Shield", "-10 attack damage"),
            Item("Small Health Potion", "+10 health"),
            Item("Large Health Potion", "+50 health"),
            Item("Booth","Allows movement of two steps instead of 1")
        ]
        for _ in range(num_items):
            self.items.append(random.choice(possible_items))
    def __repr__(self):
        return f"Treasure_Chest({self.items})"