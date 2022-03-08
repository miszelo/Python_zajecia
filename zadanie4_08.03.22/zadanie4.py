import random

def zadanie4(path):
    with open(f"{path}.dat", "w") as file:
        for i in range(10):
            file.write(str(random.randint(1, 100)) + "\n")
    return str(path + ".dat")

zadanie4("zadanie4")
