def zadanie8(path):
    lista = []
    with open(path, "r", encoding="utf8") as file:
        for line in file.readlines():
            lista.append(line.replace(",", "").replace(
                "!", "").replace("-", "").replace(".", "").split())

    longest_word = lista[0][0]
    shortest_word = lista[0][0]
    for line in lista:
        for word in line:
            if len(word) > len(longest_word):
                longest_word = word
            if len(word) < len(shortest_word):
                shortest_word = word
    print(f"\nNajdłuższe słowo: {longest_word}")
    print(f"Najkrótsze słowo: {shortest_word}")


zadanie8("C:\\Users\\micha\\Desktop\\python_zadania\\zadanie8_08.03.22\\wiersz.txt")
