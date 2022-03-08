def zadanie5(path):
    lista = []
    with open(path, "r") as file:
        for i in file.readlines():
            lista.append(int(i))

    lista.sort()

    print("Średnia: ", str(sum(lista) / len(lista)))
    if len(lista) % 2 == 0:
        
        print(f"Mediana: {(lista[len(lista) // 2 - 1] + lista[len(lista) // 2]) / 2}")
    else:
        print(f"Mediana: {lista[len(lista) // 2]} ")

    print("Max: " + str(max(lista)))
    print("Min: " + str(min(lista)))


zadanie5("C:\\Users\\micha\\Desktop\\python_zadania\\zadanie4_08.03.22\\zadanie4.dat")
