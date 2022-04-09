from main import colors_dictionary, total_sum
import time


def save_file_header(path):
    with open(path, "w", encoding="utf8") as file:
        file.write(
            """===============================================================
\t\t\t\t\tPodsumowanie  dnia
===============================================================\n"""
        )


def save_file_footer(path):
    with open(path, "a", encoding="utf8") as file:
        file.write(f"\nRaport sporządzono {time.strftime('%m/%d/%Y, %H:%M:%S')}")
        file.write("\nPrzygotował MK")


def count_colors(color_list, dictionary):
    for color in color_list:
        if color in dictionary:
            dictionary[color] += 1
    return dictionary


def save_total_income_file(path, suma):
    with open(path, "a", encoding="utf8") as file:
        file.write("Dziś sprzedano towar o łącznej wartości:\n")
        file.write(str(round(suma, 2)) + "$\n")


def save_colors_file(path, colors):
    with open(path, "a", encoding="utf8") as file:
        file.write("===============================================================\n")
        for key, value in colors.items():
            file.write(f"- Ubrań o kolorze {key} sprzedano: {value}\n")
        file.write("===============================================================\n")


def best_colors(colors):
    return max(colors)


def save_best_color(path, colors):
    with open(path, "a", encoding="utf8") as file:
        file.write("Najlepiej sprzedały się ubrania w kolorze:\n")
        file.write(best_colors(colors))
        file.write("\n===============================================================\n")


save_file_header("Podsumowanie_dnia.txt")
save_total_income_file("Podsumowanie_dnia.txt", total_sum)
save_colors_file("Podsumowanie_dnia.txt", colors_dictionary)
save_best_color("Podsumowanie_dnia.txt", colors_dictionary)
save_file_footer("Podsumowanie_dnia.txt")
