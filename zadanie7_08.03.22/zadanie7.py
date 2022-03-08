def zadanie7(path):
    number_of_lines = 0
    with open(path, "r") as file:
        for line in file:
            if line != "\n":
                number_of_lines += 1
    return number_of_lines


path = "C:\\Users\\micha\\Desktop\\python_zadania\\zadanie7_08.03.22\\cyfry.txt"
print(f"\nLiczba linii, które nie są puste, w pliku {path}: \n{zadanie7(path)}")