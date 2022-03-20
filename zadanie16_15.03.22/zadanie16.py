def zadanie16(path):
    text = ""
    with open(path, "r", encoding='utf8') as file:
        for letter in file.read():
            if letter.lower() == "j":
                text += "i"
                continue
            elif letter.lower() == "i":
                text += "j"
                continue
            text += letter
    pomocniczaDo16(
        "C:\\Users\\micha\\Desktop\\python_zadania\\zadanie16_15.03.22\\wiersz poprawiony.txt", text)


def pomocniczaDo16(path, text):
    with open(path, "w", encoding='utf8') as file:
        file.write(text)


zadanie16("C:\\Users\\micha\\Desktop\\python_zadania\\zadanie16_15.03.22\\wiersz.txt")
