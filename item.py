class Item:
    def __init__(self, type, description, effects):
        self.type = type
        self.description = description

        self.effects = {
            'power': 0,
            'defence': 0,
            'health': 0,
            'movement': 0
        }

        for key, value in effects.items():
            self.effects[key] = value

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f'{self.type} | {self.__effects_str__()} | {self.description}'

    def __effects_str__(self) -> str:
        effects = {key: value for key, value in self.effects.items()
                   if value != 0}

        return ', '.join([f'+{value} {key}' for key, value in effects.items()])


class Sword(Item):
    def __init__(self):
        effects = {'power': 10}

        super().__init__('sword',
                         'The sword chooses its wielder,\
 not the other way around.',
                         effects)


class Shield(Item):
    def __init__(self):
        effects = {'defence': 10}

        super().__init__('shield',
                         'The truth is often one\'s best shield.',
                         effects)

