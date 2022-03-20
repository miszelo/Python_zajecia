
def zadanie13(path):
    with open(path, "r", encoding="utf-8") as f:
        list = f.read().split()

    lista = []
    for word in list:
        if len(word) < 5:
            lista.append(word)

    extension = input("Podaj rozszerzenie: ")
    pomocniczaDo13(lista, extension)


def pomocniczaDo13(list, extension):
    with open(
        "C:\\Users\\micha\\Desktop\\python_zadania\\zadanie13_15.03.22\\slowa_krotsze_niz_5_liter."
        + extension,
        "w",
        encoding="utf-8",
    ) as f:
        for word in list:
            f.write(word + " ")


zadanie13("C:\\Users\\micha\\Desktop\\python_zadania\\zadanie13_15.03.22\\wiersz.txt")
