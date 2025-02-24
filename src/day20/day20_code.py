class RaceTrack:

    def __init__(self, file):
        with open(file, "r") as f:
            self.track = [list(line) for line in f.read().split("\n")]
        for i in range(len(self.track)):
            for j in range(len(self.track[0])):
                if self.track[i][j] == "S":
                    self.start = (i, j)
                elif self.track[i][j] == "E":
                    self.end = (i, j)
            # print(self.track[i])

        print(f"start = {self.start}, end = {self.end}")
        self.visited = self.bfs(self.track)
        # for line in self.costs:
        #     print(line)

    def bfs(self, track):

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        nodes = []
        visited = {}
        nodes.append((self.start[0], self.start[1], 0))

        while nodes:
            x, y, cost = nodes.pop(0)
            visited[(x,y)] = cost
            if (x,y) == self.end:
                break

            for direction in directions:
                new_x, new_y, new_cost = x + direction[0], y + direction[1], cost + 1
                if 0 <= new_x < len(track) and 0 <= new_y < len(track[0]):
                    if track[new_x][new_y] != "#" and (new_x, new_y) not in visited:
                        visited[(new_x, new_y)] = new_cost
                        nodes.append((new_x, new_y, new_cost))

        return visited

    def count_cheats(self, visited):
        counter = 0
        directions = [[-2, 0], [2, 0], [0, -2], [0, 2]]
        for x,y in visited:
            for direction in directions:
                new_x, new_y = x+direction[0], y+direction[1]
                if visited.get((new_x,new_y),0) >= visited.get((x,y))+102:
                    counter += 1
        return counter

    def count_bigger_cheats(self,visited):
        counter = 0
        cheats = set()

        for x, y in visited:
            for x2, y2 in visited:
                if abs(x-x2)+ abs(y-y2) <= 20:
                    if visited.get((x2, y2), 0) >= visited.get((x, y)) + 100 + abs(x-x2)+ abs(y-y2):
                        counter += 1
        return counter




if __name__ == "__main__":
    file = "data.txt"
    rt = RaceTrack(file)
    print(f"part 1 : {rt.count_cheats(rt.visited)}")

    print(f"part 2 : {rt.count_bigger_cheats(rt.visited)}")
