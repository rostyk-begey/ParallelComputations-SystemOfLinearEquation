import random


def gen_equation(filename, size, prec):
    roots = [round(random.uniform(-20, 20), prec) for _ in range(size)]
    freeCol = []

    with open(filename + ".txt", "w") as file:
        for i in range(size):
            numbers = [round(random.uniform(-20, 20), prec) for _ in range(size - 1)]
            absSum = sum([abs(number) for number in numbers])
            numbers.insert(i, round(random.uniform(absSum + 1, absSum + 3), prec))
            freeCol.append(sum([roots[i] * numbers[i] for i in range(size)]))
            file.write("\t".join([str(number) for number in numbers]) + "\n")

    with open(f"{filename}_fcol.txt", "w") as file:
        for i in range(size):
            file.write(f"{freeCol[i]:.{prec}f}\n")

    with open(f'{filename}_roots.txt', "w") as file:
        for i in range(size):
            file.write(f"{roots[i]}\n")


def check(filename):
    with open(filename) as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            numbers = [abs(float(strNum)) for strNum in line.split()]
            diagNum = numbers.pop(i)
            if sum(numbers) >= diagNum:
                return False
        return True


filename = "equation"
size = int(input("size: "))
prec = int(input("precision: "))

gen_equation(filename, size, prec)
