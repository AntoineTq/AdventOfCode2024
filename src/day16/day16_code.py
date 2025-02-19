import re
import copy
from collections import defaultdict


class Maze:

    def __init__(self, file):

        with open(file, "r") as f:
            data = f.read()
            self.maze = []
            arr = data.split("\n")
            for i in range(len(arr)):
                self.maze.append(list(arr[i]))
                if "S" in arr[i] or "E" in arr[i]:
                    for j in range(len(arr[i])):
                        if arr[i][j] == "S":
                            self.start_x = i
                            self.start_y = j
                        if arr[i][j] == "E":
                            self.end_x = i
                            self.end_y = j

    def bfs(self, start_x, start_y, end_x, end_y, curr_direction):
        maze = self.maze
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        costs = [[float('inf')] * len(maze[0]) for i in range(len(maze))]
        min_cost = float('inf')
        nodes = []
        nodes.append((start_x, start_y, curr_direction, 0))
        costs[start_x][start_y] = 0

        while len(nodes) > 0:

            curr = nodes.pop(0)
            x = curr[0]
            y = curr[1]
            curr_direction = curr[2]
            cost = curr[3]
            if x == end_x and y == end_y:
                min_cost = min(cost + 1, min_cost)

            for direction in directions:
                if curr_direction is not None and direction[0] == -1 * curr_direction[0] and direction[1] == -1 * curr_direction[1]:
                    continue
                new_x = x + direction[0]
                new_y = y + direction[1]

                new_cost = cost + 1
                if direction != curr_direction and curr_direction is not None:
                    new_cost += 1000

                if new_x == end_x and new_y == end_y:
                    min_cost = min(new_cost, min_cost)
                if maze[new_x][new_y] == "#":
                    continue
                if costs[new_x][new_y] > new_cost:
                    costs[new_x][new_y] = new_cost
                    nodes.append((new_x, new_y, direction, new_cost))


        return min_cost

    def reverse_bfs(self, min_value):
        maze = self.maze
        maze[self.end_x][self.end_y] = "O"
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        nodes = []
        nodes.append((self.end_x, self.end_y, None))
        visited = set()
        visited.add((self.end_x, self.end_y))

        while len(nodes) > 0:

            curr = nodes.pop(0)
            x = curr[0]
            y = curr[1]
            curr_direction = curr[2]

            for direction in directions:
                if curr_direction is not None and direction[0] == -1 * curr_direction[0] and direction[1] == -1 * curr_direction[1]:
                    continue

                new_x = x + direction[0]
                new_y = y + direction[1]

                if maze[new_x][new_y] == "#":
                    continue

                a = self.bfs(self.start_x,self.start_y, new_x,new_y,[0, 1])
                b = self.bfs(new_x, new_y, self.end_x, self.end_y, None)

                if self.start_x == new_x and self.start_y == new_y :
                    visited.add((self.start_x,self.start_y))

                if (new_x,new_y) not in visited and (a+b == min_value or 1000 == abs(a+b-min_value)):
                    nodes.append((new_x,new_y,direction))
                    maze[new_x][new_y] = "O"
                    visited.add((new_x,new_y))


        return len(visited)


if __name__ == "__main__":
    maze = Maze("data.txt")
    min_value = maze.bfs(maze.start_x, maze.start_y, maze.end_x, maze.end_y, [0, 1])
    print(min_value)

    print(maze.reverse_bfs(min_value))
