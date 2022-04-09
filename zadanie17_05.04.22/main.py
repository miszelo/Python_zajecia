import time
import os
from poem import poem

assessments = {
    "Paweł": [1],
    "Ola": [2]
}


def update_dictionary(dictionary, name, assessment):
    if name in dictionary:
        dictionary[name].append(assessment)
    else:
        dictionary[name] = [assessment]


def show_file(file_name):
    with open(f"C:\\Users\\{os.getlogin()}\\Desktop\\{file_name}.txt", "r", encoding="utf8") as file:
        for line in file.readlines():
            print(line, end="")


def save_to_file(file_name, grades):
    with open(f"C:\\Users\\{os.getlogin()}\\Desktop\\{file_name}.txt", "w", encoding="utf8") as file:
        file.write("Imię".ljust(20) + "Oceny".center(20) + "\n")
        for key, value in grades.items():
            file.write(str(key).ljust(20))
            file.write(','.join(map(str, value)).center(20))
            file.write("\n")

        file.write(f"\nOstatnia modyfikacja pliku: {time.strftime('%m/%d/%Y, %H:%M:%S')}\n")
        file.write("Skrypt utworzony przez MK")


def case_yes():
    add_assessments()
    user_choice = input("Czy chcesz zapisać oceny w pliku?: ").lower()
    if user_choice == "tak":
        file_name = input("Podaj nazwe pliku: ")
        save_to_file(file_name, assessments)
        match input("Chcesz podejrzeć plik?: ").lower():
            case "tak":
                show_file(file_name)
            case _:
                case_no()
    else:
        case_no()


def add_assessments():
    how_many_persons = int(input("Ilu osobom chcesz dodać oceny?: "))
    for _ in range(how_many_persons):
        update_dictionary(assessments, input("Podaj imię: ").capitalize(), int(input("Podaj ocenę: ").capitalize()))


def case_no():
    print("Jak nie chcesz to chociaż sobie poczytaj ;)")
    print(poem)


def default_case():
    print("Wpisz tak albo nie!")


def show_menu():
    while True:
        user_choice = input("Czy chcesz dodać nowe oceny?: ").lower()
        match user_choice:
            case "tak":
                case_yes()
                break
            case "nie":
                case_no()
                break
            case _:
                default_case()
                continue


if __name__ == '__main__':
    show_menu()
