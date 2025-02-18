import re
import copy
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

    def bfs(self):
        maze = self.maze
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        costs = [[float('inf')]*len(maze[0]) for i in range(len(maze))]
        min_cost = float('inf')
        nodes = []
        curr_direction = [0,1]
        nodes.append((self.start_x,self.start_y, curr_direction, 0))
        costs[self.start_x][self.start_y] = 0

        while len(nodes)>0:

            curr = nodes.pop(0)
            x = curr[0]
            y = curr[1]
            curr_direction = curr[2]
            cost = curr[3]
            if x == self.end_x and y == self.end_y:
                min_cost = min(cost + 1, min_cost)

            for direction in directions:
                if direction[0] == -1*curr_direction[0] and direction[1] == -1*curr_direction[1]:
                    continue
                new_x = x + direction[0]
                new_y = y + direction[1]

                new_cost = cost+1
                if direction != curr_direction:
                    new_cost += 1000

                if new_x == self.end_x and new_y == self.end_y:
                    min_cost = min(new_cost, min_cost)
                if maze[new_x][new_y] == "#":
                    continue
                if costs[new_x][new_y] > new_cost:
                    costs[new_x][new_y] = new_cost
                    nodes.append((new_x,new_y,direction,new_cost))




        return min_cost


if __name__ == "__main__":
    maze = Maze("data.txt")
    print(maze.bfs())
