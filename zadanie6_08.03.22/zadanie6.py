def zadanie6(path):
    number_of_lines = 0
    with open(path, "r") as file:
        for _ in file:
            number_of_lines += 1
    return number_of_lines


path = "C:\\Users\\micha\\Desktop\\python_zadania\\zadanie6_08.03.22\\cyfry.txt"
print(f"\nLiczba linii w pliku {path}: \n{zadanie6(path)}")
