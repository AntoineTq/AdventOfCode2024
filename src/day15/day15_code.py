import re


class Warehouse:

    def __init__(self, file):

        with open(file, "r") as f:
            data = f.read()
        map_pattern = re.compile(r"(#.*)")
        matches = map_pattern.findall(data)
        self.board = []
        for i in range(len(matches)):
            self.board.append(list(matches[i]))
            for j in range(len(matches[i])):
                if matches[i][j] == '@':
                    self.x = i
                    self.y = j
                    break

        moves_pattern = re.compile(r"([\^<>v])")
        moves = moves_pattern.findall(data)
        self.directions = self.get_moves(moves)

    def get_moves(self, moves):
        directions = []
        for move in moves:
            if move == "<":
                directions.append([0, -1])
            elif move == ">":
                directions.append([0, 1])
            elif move == "^":
                directions.append([-1, 0])
            elif move == "v":
                directions.append([1, 0])
        return directions

    def move_boxes1(self, i, j, new_x, new_y):
        # look at the boxes next to the robot
        while self.board[new_x][new_y] in ["O", "[", "]"]:
            new_x += i
            new_y += j
        # if next to a wall no need to continue
        if self.board[new_x][new_y] == "#":
            return
        # Move all the boxes
        while self.board[new_x - i][new_y - j] != "@":
            self.board[new_x][new_y] = self.board[new_x - i][new_y - j]
            new_x -= i
            new_y -= j

        # move robot
        self.board[new_x][new_y] = "@"
        self.board[self.x][self.y] = "."
        self.x = new_x
        self.y = new_y

    def check_box_path(self, i, j, x, y, positions):
        new_x = x + i
        new_y = y + j
        if not 0<= new_x < len(self.board):
            return
        if self.board[new_x][new_y] == self.board[x][y]:
            self.check_box_path(i, j, new_x, new_y, positions)
        elif self.board[new_x][new_y] in ["[","]"]:
            if self.board[x][y] == "[":
                self.check_box_path(i, j, new_x, new_y , positions)
                self.check_box_path(i, j, new_x, new_y - 1, positions)
            else:
                self.check_box_path(i, j, new_x, new_y , positions)
                self.check_box_path(i, j, new_x, new_y + 1, positions)
        if not (x,y,self.board[x][y]) in positions:
            positions.append((x,y, self.board[x][y]))
        return

    def move_boxes2(self, i, j, new_x, new_y):
        box_pos = [(new_x, new_y, self.board[new_x][new_y])]
        if self.board[new_x][new_y] == "[":
            box_pos.append((new_x,new_y+1, self.board[new_x][new_y+1]))
        else:
            box_pos.append((new_x,new_y-1, self.board[new_x][new_y-1]))
        positions = []
        for x,y,value in box_pos:
            self.check_box_path(i, j, x, y, positions)

        for pos in positions:
            if self.board[pos[0]+i][pos[1]+j] == "#":
                return

        for pos in positions:
            self.board[pos[0]+i][pos[1]] = pos[2]
            self.board[pos[0]][pos[1]] = "."
        self.board[new_x][new_y] = "@"
        self.board[self.x][self.y] = "."
        self.x = new_x
        self.y = new_y


    def run(self, is_part_2):
        for i, j in self.directions:
            new_x = self.x + i
            new_y = self.y + j
            # wall in that direction
            if self.board[new_x][new_y] == "#":
                continue
            # Position is free
            elif self.board[new_x][new_y] == ".":
                self.board[self.x][self.y] = "."
                self.board[new_x][new_y] = "@"
                self.x = new_x
                self.y = new_y
            # Box in that direction : need to move it
            elif self.board[new_x][new_y] in ["O", "[", "]"]:
                if is_part_2 and j == 0:
                    # Vertical move will be different for part 2
                    self.move_boxes2(i, j, new_x, new_y)
                else:
                    self.move_boxes1(i, j, new_x, new_y)
            # for i in self.board:
            #     for e in i:
            #         print(e, end="")
            #     print("")

    def compute_coordinates(self):
        result = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == "O" or self.board[i][j] == "[":
                    result += (100 * i + j)
        return result


if __name__ == "__main__":
    warehouse1 = Warehouse("data1.txt")
    warehouse1.run(False)
    print(f"part 1 = {warehouse1.compute_coordinates()}")

    warehouse2 = Warehouse("data2.txt")
    warehouse2.run(True)
    print(f"part 2 = {warehouse2.compute_coordinates()}")

