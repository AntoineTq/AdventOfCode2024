import re


class Restroom:

    def __init__(self, file):

        with open(file, "r") as f:
            data = f.read()

        pattern = re.compile(r"p=(\d+),(\d+) v=(-*\d+),(-*\d+)")

        matches = pattern.findall(data)

        self.robots = []
        for match in matches:
            tmp = list(map(int, match))
            # inverted coord from exercice (y is x and y is x so we swap it here)
            self.robots.append([[tmp[1], tmp[0]], [tmp[3], tmp[2]]])

        self.x_max = 103
        self.y_max = 101
        if file == "example.txt":
            self.x_max = 7
            self.y_max = 11

    def run1(self):

        pos = [0, 0, 0, 0]
        for robot in self.robots:
            x = robot[0][0]
            y = robot[0][1]
            for i in range(100):
                new_x = (x + robot[1][0]) % self.x_max
                new_y = (y + robot[1][1]) % self.y_max
                x = new_x
                y = new_y

            if x < (self.x_max // 2) and y < (self.y_max // 2):
                pos[0] += 1
            elif x < (self.x_max // 2) and y > (self.y_max // 2):
                pos[1] += 1
            elif x > (self.x_max // 2) and y < (self.y_max // 2):
                pos[2] += 1
            elif x > (self.x_max // 2) and y > (self.y_max // 2):
                pos[3] += 1

        res = 1
        for i in pos:
            res *= i
        return res

    def run2(self):
        positions = [["0"] * self.y_max for i in range(self.x_max)]
        for i in range(self.x_max*self.y_max):
            for robot in self.robots:
                x = robot[0][0]
                y = robot[0][1]
                new_x = (x + robot[1][0]) % self.x_max
                new_y = (y + robot[1][1]) % self.y_max
                if positions[x][y] != "0":
                    positions[x][y] = str(int(positions[x][y]) - 1)
                robot[0][0] = new_x
                robot[0][1] = new_y
                new_val = int(positions[new_x][new_y]) +1
                positions[new_x][new_y] = str(new_val)

            # Print into a txt file the positions
            with open("test.txt", "a") as file:
                candidate = False
                # First loop used to filter and write only candidates solutions
                # (those which have namy robots on the same line)
                for line in positions:
                    count = 0
                    for elem in line:
                        if int(elem) >= 1:
                            count+=1
                    if count >= 28:
                        candidate = True

                if candidate:
                    file.write(f"\n\n----------------{i}\n")
                    for line in positions:
                        for elem in line:
                            if elem != "0":
                                file.write(elem)
                            else:
                                file.write(".")
                        file.write("\n")



if __name__ == "__main__":
    restroom = Restroom("data.txt")

    print(restroom.run1())

    print(restroom.run2())
