class Garden:

    def __init__(self, file_name):
        with open(file_name, "r") as file:
            data = file.read()
            self.garden_input = [list(row) for row in data.split()]

    def run(self, is_part2):
        cost = 0
        visited = [list(False for i in row) for row in self.garden_input]

        for i in range(len(self.garden_input)):
            for j in range(len(self.garden_input[i])):
                if not visited[i][j]:
                    cost += self.check_region(i, j, visited, is_part2)
        return cost

    def check_position1(self, x, y, visited):
        visited[x][y] = True
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        sides = 4
        plant_count = 1
        for i, j in directions:
            new_x = x + i
            new_y = y + j
            if (0 <= new_x < len(self.garden_input)) and (0 <= new_y < len(self.garden_input[0])):
                if self.garden_input[new_x][new_y] == self.garden_input[x][y]:
                    if not visited[new_x][new_y]:
                        # if a neighbor of the current node is in the same region ( and not visited yet),
                        # visit it and add its number of sides to the current node)
                        new_side, new_plant_count = self.check_position1(new_x, new_y, visited)
                        sides += new_side
                        plant_count += new_plant_count
                    sides -= 1 # Remove 1 side for each neighbor from same region

        return sides, plant_count

    def get_region(self, x, y, positions ,visited):
        positions.append((x,y))
        visited[x][y] = True
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for i, j in directions:
            new_x = x + i
            new_y = y + j
            if (0 <= new_x < len(self.garden_input)) and (0 <= new_y < len(self.garden_input[0])):
                if self.garden_input[new_x][new_y] == self.garden_input[x][y]:
                    if not visited[new_x][new_y]:
                        self.get_region(new_x, new_y, positions, visited)
        return positions
    def check_position2(self,x_start,y_start, visited):
        visited[x_start][y_start] = True
        positions = self.get_region(x_start,y_start,[],visited)
        diagonals = [[-1, -1], [-1, 1], [1, 1], [1, -1]] # North West (NW), NE , SE , SW
        row_size = len(self.garden_input)
        col_size = len(self.garden_input[0])
        corners = 0
        for x,y in positions:
            corner = 0
            for diag in diagonals:
                """
                example : 
                d    a1
                
                a2  (x,y)  
                -------
                so we want to see if an angle of a region is convex / concave.
                """
                a1 = (x+diag[0], y) # first pos adj to curr position
                a2 = (x, y+diag[1]) # second pos adj to curr position
                d = (x+diag[0], y+diag[1]) # pos in diag of curr position
                if (not a1 in positions and not a2 in positions) or (d not in positions and a1 in positions and a2 in positions):
                    corner += 1
            corners += corner

        return len(positions), corners


    def check_region(self, x, y, visited, is_part_two):

        if is_part_two:
            plants, corners = self.check_position2(x,y, visited)
            return plants * corners

        else:
            plants, cost = self.check_position1(x, y, visited)
            return plants * cost


if __name__ == "__main__":
    # part 1
    garden1 = Garden("data.txt")
    print(f"part 1 : {garden1.run(False)}")

    # part 2: just count the diagonals to get the number of edges (either convex / concave)
    garden2 = Garden("data.txt")
    print(f"part 2 : {garden2.run(True)}")
