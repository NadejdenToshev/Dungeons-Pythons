from maze import Maze

def main():
    rows, cols = 5, 5  
    maze = Maze(rows, cols)
    maze.generate()
    print(maze)

    
    cave1 = maze.caves[0][0]
    cave2 = maze.caves[0][1]
    print(f"Is passable between {cave1} and {cave2}? {maze.is_passable(cave1, cave2)}")

if __name__ == "__main__":
    main()


