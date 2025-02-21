import copy
import re


class MemoryMaze:

    def __init__(self, file):
        self.maze_size = 71
        self.memory = 1024
        self.maze = [["."] * self.maze_size for i in range(self.maze_size)]
        n = 0
        with open(file, "r") as f:
            for line in f:
                if n == self.memory:
                    break
                y,x = map(int, line.strip().split(","))
                self.maze[x][y] = "#"
                n += 1

        # for i in self.maze:
        #     print(i)

    def bfs(self):
        start = (0, 0)
        parents_list = {}
        visited = set()
        nodes = [start]
        visited.add(start)
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        while nodes:
            current = nodes.pop(0)
            for direction in directions:
                new_x = current[0] + direction[0]
                new_y = current[1] + direction[1]
                if 0 <= new_x < self.maze_size and 0 <= new_y < self.maze_size:
                    if self.maze[new_x][new_y] == "#":
                        continue
                    if not (new_x, new_y) in visited:
                        parents_list[(new_x, new_y)] = current
                        if (new_x, new_y) == (self.maze_size - 1, self.maze_size - 1):
                            return parents_list
                        visited.add((new_x, new_y))
                        nodes.append((new_x, new_y))
        return None

    def reconstruct_path(self, parents):
        current = parents[(self.maze_size-1, self.maze_size-1)]
        node_count = 1
        while current != (0,0):
            self.maze[current[0]][current[1]] = "0"
            node_count += 1
            current = parents[current]
        return node_count


    def simulate_space(self,file):
        with open(file, "r") as f:
            data = f.readlines()

        while True:
            y,x = map(int, data[self.memory].strip().split(","))
            self.maze[x][y] = "#"
            path = self.bfs()
            if path is None :
                print(f"ended : {y,x}")
                return
            self.memory += 1



if __name__ == "__main__":
    file = "data.txt"
    maze = MemoryMaze(file)
    parents_list = maze.bfs()
    print(maze.reconstruct_path(parents_list))
    maze.simulate_space(file)
