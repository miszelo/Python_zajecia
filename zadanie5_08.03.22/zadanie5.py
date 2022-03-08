def zadanie5(path):
    lista = []
    with open(path, "r") as file:
        for i in file.readlines():
            lista.append(int(i))

    lista.sort()

    print(f"Średnia: {sum(lista) / len(lista)}")
    print(mediana(lista))
    print(f"Max: {max(lista)}")
    print(f"Min: {min(lista)}")

def mediana(lista):
    if len(lista) % 2 == 0:
        return f"Mediana: {(lista[len(lista) // 2 - 1] + lista[len(lista) // 2]) / 2}"
    else:
        return f"Mediana: {lista[len(lista) // 2]} "

zadanie5("C:\\Users\\micha\\Desktop\\python_zadania\\zadanie4_08.03.22\\zadanie4.dat")
