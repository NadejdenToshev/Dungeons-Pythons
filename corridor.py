class Corridor:
    def __init__(self, cave1, cave2, passable=True):
        self.cave1 = cave1
        self.cave2 = cave2
        self.passable = passable

    def __repr__(self):
        return f"Corridor({self.cave1}, {self.cave2}, passable={self.passable})"
