import copy
import re


class Computer:

    def __init__(self, file):
        self.registers = {}
        with open(file, "r") as f:
            data = f.read()

        pattern = re.compile(r"Register (.): (.*)")
        matches = re.findall(pattern, data)
        for match in matches:
            self.registers[match[0]] = int(match[1])

        print(self.registers)
        self.base_registers = copy.deepcopy(self.registers)
        self.program = list(map(int, re.findall(r"Program: (.*)", data)[0].split(",")))
        print(self.program)

    def combo(self, operand):
        if operand == 4:
            return self.registers['A']
        elif operand == 5:
            return self.registers['B']
        elif operand == 6:
            return self.registers['C']
        elif operand == 7:
            raise Exception("Operand not allowed")
        else:
            return operand

    def run_program(self):
        output = []
        pointer = 0
        while pointer < len(self.program):
            #print(self.registers)
            opcode = self.program[pointer]
            operand = self.program[pointer + 1]
            if opcode == 0:
                # adv instruction (opcode 0) performs division
                numerator = self.registers['A']
                denominator = pow(2, self.combo(operand))
                self.registers['A'] = numerator // denominator

            elif opcode == 1:
                # bxl instruction (opcode 1) calculates the bitwise XOR
                a = self.registers['B'] ^ operand
                self.registers['B'] ^= operand

            elif opcode == 2:
                # bst instruction (opcode 2) calculates the value of its combo operand modulo 8
                self.registers['B'] = self.combo(operand) % 8

            elif opcode == 3:
                # jnz instruction (opcode 3) does nothing or jump based on A
                if self.registers['A'] != 0:
                    pointer = operand
                    continue

            elif opcode == 4:
                # bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C
                self.registers['B'] = self.registers['B'] ^ self.registers['C']

            elif opcode == 5:
                # out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value
                value = self.combo(operand) % 8
                output.append(value)

            elif opcode == 6:
                # bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register
                numerator = self.registers['A']
                denominator = pow(2, self.combo(operand))
                self.registers['B'] = numerator // denominator

            elif opcode == 7:
                # cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register
                numerator = self.registers['A']
                x = pow(2,operand)
                denominator = pow(2, self.combo(operand))
                self.registers['C'] = numerator // denominator

            pointer += 2

        return ",".join(map(str,output))

    # Part 2 pas opti, ca teste juste toutes les possibilités
    def get_A_value(self):
        a = 0
        self.registers = self.base_registers
        self.registers['A'] = a
        for i in reversed(range(len(self.program))):
            print(self.program[i:])
            a <<=3
            print(a)
            while list(map(int,self.run_program().split(","))) != self.program[i:]:
                a += 1
                self.registers = self.base_registers
                self.registers['A'] = a
        return a
if __name__ == "__main__":
    computer = Computer("data.txt")
    print(computer.run_program())
    print(computer.get_A_value())