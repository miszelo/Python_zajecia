import random


def save_to_file(filename, array):
    with open(f"C:\\Users\\micha\Desktop\\{filename}.txt", "w", encoding="utf8") as file:
        for i in array:
            for j in i:
                file.write(str(j) + "\t")
            file.write("\n")


def save_sum_and_mean_to_file(filename, column, sum, mean):
    with open(f"C:\\Users\\micha\Desktop\\{filename}.txt", "w", encoding="utf8") as file:
        file.write(f"Suma kolumny {column + 1}: {sum}\n")
        file.write(f"Średnia kolumny {column + 1}: {mean}")


def save_sum_of_every_column_to_file(filename, array):
    with open(f"C:\\Users\\micha\Desktop\\{filename}.txt", "w", encoding="utf8") as file:
        for i in array:
            file.write(str(i) + " ")


def generate_array(rows, columns, bottom_range, upper_range):
    return [[random.randint(bottom_range, upper_range) for i in range(rows)] for j in range(columns)]


def sum_of_column(array, column):
    total_sum = 0
    for i in range(len(array)):
        total_sum += array[i][column]
    return total_sum


def mean_of_column(array, column):
    total_sum = 0
    for i in range(len(array)):
        total_sum += array[i][column]
    return total_sum / len(array)


def sum_of_every_columns(array):
    return [sum(x) for x in zip(*array)]


def sum_of_diagonal(array):
    total_sum = 0
    index = 0
    for i in range(len(array)):
        total_sum += array[i][index]
        index += 1
    return total_sum


if __name__ == '__main__':
    matrix = generate_array(11, 11, 1, 10)
    sum_of_every_column = sum_of_every_columns(matrix)

    print(f"Suma przekątnej: {sum_of_diagonal(matrix)}")
    save_to_file("matrix", matrix)
    save_sum_of_every_column_to_file("suma przekątnych", sum_of_every_column)
    save_sum_and_mean_to_file("Średnia i suma", 2, sum_of_column(matrix, 2), mean_of_column(matrix, 2))
