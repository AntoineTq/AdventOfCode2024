import functools


class Pluto:

    def __init__(self, file_name):
        with open(file_name, "r") as file:
            self.raw_data = file.read()
            self.stones = list(map(int, self.raw_data.split()))

    def blink(self, input, depth):
        if depth == 0:
            return len(input)
        new_input = []
        for elem in input:
            text = str(elem)
            elem_size = len(text)
            if elem == 0:
                new_input.append(1)
            elif elem_size % 2 == 0:
                new_input.append(int(text[:int(elem_size / 2)]))
                new_input.append(int(text[int(elem_size / 2):]))
            else:
                new_input.append(str(int(elem) * 2024))
        depth -= 1
        return self.blink(new_input, depth)

    @functools.cache
    def single_blink(self, value):
        text = str(value)
        num_of_digit = len(text)
        if value == 0:
            return (1,None)
        elif num_of_digit % 2 == 0:
            left_stone = int(text[:(num_of_digit // 2)])
            right_stone = int(text[(num_of_digit // 2):])
            return left_stone,right_stone
        else:
            return (value*2024, None)

    @functools.cache
    def count_blink(self,stone, depth):

        left_stone, right_stone = self.single_blink(stone)

        if depth == 1:
            return 1 if right_stone is None else 2

        else:
            output = self.count_blink(left_stone,depth-1)
            if right_stone is not None:
                output += self.count_blink(right_stone,depth-1)
            return output


    def run(self, depth):
        result = 0
        for stone in self.stones:
            result += self.count_blink(stone,depth)
        return result


if __name__ == '__main__':
    pluto = Pluto("data.txt")
    print(pluto.stones)
    print(pluto.blink(pluto.stones, 25))

    # Part 2 : based on reddit post.
    # Important to remember to use memoization for such problems in order to speed up the process
    # because we basically call the same function on the same values alot
    # so its better to remember their output
    print(pluto.run(75))
