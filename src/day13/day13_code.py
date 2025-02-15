import re
import sympy as sp
class Lobby:

    def __init__(self, file):
        with open(file, "r") as f:
            data = f.read()

            pattern = re.compile(
                r"Button A: X\+(\d+), Y\+(\d+)\n"
                r"Button B: X\+(\d+), Y\+(\d+)\n"
                r"Prize: X=(\d+), Y=(\d+)"
            )

            matches = pattern.findall(data)

            self.machines = []
            for match in matches:
                self.machines.append({
                    "Button A": {"X": int(match[0]), "Y": int(match[1])},
                    "Button B": {"X": int(match[2]), "Y": int(match[3])},
                    "Prize": {"X": int(match[4]), "Y": int(match[5])},
                })


    def compute(self, a, b, result):
        for i in range(100):
            for j in range(100):
                if i*a["X"] + j*b["X"] == result["X"] and i*a["Y"] + j*b["Y"] == result["Y"]:
                    return i,j
        return -1,-1

    def compute2(self, a, b, result):

        x, y, z1, z2, z3, z4 = sp.symbols("x y z1 z2 z3 z4")
        eq1 = sp.Eq(x*a["X"], z1)
        eq2 = sp.Eq(x*a["Y"], z2)
        eq3 = sp.Eq(y*b["X"], z3)
        eq4 = sp.Eq(y * b["Y"], z4)
        eq5 = sp.Eq(z1+z3, result["X"]+10000000000000)
        eq6 = sp.Eq(z2+z4, result["Y"]+10000000000000)

        sol = sp.solve([eq1,eq2,eq3,eq4,eq5,eq6], [x,y,z1,z2,z3,z4])

        if int(sol[x]) == sol[x] and int(sol[y]) == sol[y]:
            return sol[x], sol[y]
        return -1,-1




    def run(self, is_part2):
        result = 0
        for machine in self.machines:
            if not is_part2:
                x, y = self.compute(machine["Button A"], machine["Button B"], machine["Prize"])
            else :
                x, y = self.compute2(machine["Button A"], machine["Button B"], machine["Prize"])
            if  x != -1:
                result += 3*x + y

        return result









if __name__ == "__main__":
    lobby = Lobby("data.txt")
    print(lobby.run(False))

    print(lobby.run(True))