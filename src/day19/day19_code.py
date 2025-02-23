import copy
import functools


class Towel:

    def __init__(self, file):
        with open(file, "r") as f:
            self.models = sorted(set(elem.strip() for elem in f.readline().split(",")), key=len, reverse=True)
            self.designs = [line.strip() for line in f.readlines() if line != '\n']

    def run(self, isTwo):
        valid = 0
        for design in self.designs:
            if isTwo:
                n = self.count_arrangements(design)
                valid += n
            else:
                n = self.count_arrangements(design)
                if n != 0:
                    valid += 1
        return valid

    @functools.cache
    def count_arrangements(self, design):
        i = min(len(self.models), len(design))
        count = 0
        while i > 0:
            current = design[len(design) - i:len(design)]
            if current in self.models:
                remaining = design[:len(design) - i]
                if len(remaining) > 0:
                    count += self.count_arrangements(remaining)
                else:
                    count += 1
            i -= 1
        # print(f"design {design} called and returned {count}")
        return count


if __name__ == "__main__":
    file = "data.txt"
    towel = Towel(file)
    print(towel.run(False))
    print(towel.run(True))
