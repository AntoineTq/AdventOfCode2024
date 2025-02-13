class TrailFinder:

    def __init__(self, file_name):

        with open(file_name, "r") as file:
            self.raw_data = file.readlines()
        self.trail_map = self.create_map()


    def create_map(self):
        trail_map = []
        for line in self.raw_data:
            trail_map.append([char for char in line if char.isdigit()])
        return trail_map

    def check_trail(self, x_start, y_start, improved):
        n_trails = 0
        directions = [[-1, 0],[1,0],[0,-1],[0,1]]
        nodes = []
        visited = set()
        visited.add((x_start,y_start))
        nodes.append((x_start,y_start))

        while(not len(nodes)==0):
            x ,y = nodes.pop()
            current_height = int(self.trail_map[x][y])
            if current_height == 9 and (x,y) not in visited:
                n_trails += 1
            if not improved :
                visited.add((x, y))

            for i, j in directions:
                new_x = x+i
                new_y = y+j
                if  (0 <= new_x < len(self.trail_map)) and (0 <= new_y < len(self.trail_map[0])):
                    if not (new_x, new_y) in visited and int(self.trail_map[new_x][new_y]) == current_height+1:
                        nodes.append((new_x,new_y))

        return n_trails

    def find_trails(self, improved):
        score = 0
        for row in range(len(self.trail_map)):
            for col in range(len(self.trail_map[row])):
                if self.trail_map[row][col] == "0":
                    score += self.check_trail(row, col, improved)
        return score










if __name__ == '__main__':
    # part 1
    finder = TrailFinder("data.txt")
    print(finder.find_trails(False))

    #part 2
    finder = TrailFinder("data.txt")
    print(finder.find_trails(True))

