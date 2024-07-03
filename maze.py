from cave import Cave


class Maze:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.__generate__()
        self.graph = {i: {'up': None, 'down': None,
                          'left': None, 'right': None}
                      for i in range(self.n * self.m)}
        self.__generate_graph__()

    def block(self, x, y):
        if (y < x):
            x, y = y, x

        # left
        if x == y - 1:
            self.graph[y]['left'][1] = False
            self.graph[x]['right'][1] = False
        # up
        elif x == y - self.m:
            self.graph[y]['up'][1] = False
            self.graph[x]['down'][1] = False

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        matrix = [[self.__get_cave__(i, j) for j in range(self.m)]
                  for i in range(self.n)]

        result = ''
        for x in range(self.n):
            row = ''
            connection = ''
            for y in range(self.m):
                cave = str(matrix[x][y])
                row += cave

                if y < self.m - 1:
                    row += '-'\
                        if self.graph[self.__get_index__(x, y)]['right'][1]\
                        else 'x'

                if x < self.n - 1:
                    down_edge = list(' ' * len(cave))
                    down_edge[len(cave) // 2] = '|'\
                        if self.graph[self.__get_index__(x, y)]['down'][1]\
                        else 'x'
                    down_edge = ''.join(down_edge)

                    connection += down_edge + ' '
            result += row + '\n'

            if x < self.n - 1:
                result += connection + '\n'

        return result

    def __generate__(self):
        self.caves = [Cave() for _ in range(self.n * self.m)]

    def __generate_graph__(self):
        for x in range(self.n):
            for y in range(self.m):
                index = (x * self.m) + y
                if y > 0:
                    left = self.__get_index__(x, y - 1)
                    self.graph[index]['left'] = [left, True]
                if y < self.m - 1:
                    right = self.__get_index__(x, y + 1)
                    self.graph[index]['right'] = [right, True]
                if x > 0:
                    up = self.__get_index__(x - 1, y)
                    self.graph[index]['up'] = [up, True]
                if x < self.n - 1:
                    down = self.__get_index__(x + 1, y)
                    self.graph[index]['down'] = [down, True]

    def __get_index__(self, x, y) -> int:
        return (x * self.m) + y

    def __get_cave__(self, x, y) -> Cave:
        return self.caves[self.__get_index__(x, y)]
