def zadanie15(path):
    text = ""
    with open(path, "r", encoding='utf-8') as file:
        for letter in file.read():
            if letter != " ":
                text += letter + "#"
    
    return text[:-1]

def pomocniczaDo15(path, text):
    with open(path, "w", encoding='utf-8') as file:
        file.write(text)

pomocniczaDo15("C:\\Users\\micha\\Desktop\\python_zadania\\zadanie15_15.03.22\\pythonPoprawiony.txt", zadanie15("C:\\Users\\micha\\Desktop\\python_zadania\\zadanie15_15.03.22\\python.txt"))
