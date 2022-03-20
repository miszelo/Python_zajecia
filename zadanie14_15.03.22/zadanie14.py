from fpdf import FPDF


def zadanie14(path):
    count = 0
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    with open(path, "r", encoding="utf-8") as file:
        for word in file.read():
            if word.upper() == word:
                count += 1
    pdf.cell(
        200, 10, txt=f"Liczba duzych liter w tekscie: {count}", ln=1, align='C')
    pdf.output("C:\\Users\\micha\\Desktop\\python_zadania\\zadanie14_15.03.22\\zadanie14.pdf")

    return count


print("Liczba dużych liter w tekście:", zadanie14(
    "C:\\Users\\micha\\Desktop\\python_zadania\\zadanie14_15.03.22\\wiersz.txt"))
