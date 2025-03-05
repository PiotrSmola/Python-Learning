import PySimpleGUI as sg
from datetime import datetime


sg.theme_background_color("gray")
sg.theme_element_background_color("pink")

layout = [
    [sg.Text("Podaj imię:"), sg.InputText(key="name")],
    [sg.Text("Podaj wiek:"), sg.InputText(key="age")],
    [sg.Text("Wybierz płeć:")],
    [sg.Radio("Mężczyzna", "gender", key="male"), sg.Radio("Kobieta", "gender", key="female")],
    [sg.Text("Wybierz ulubiony kolor:")],
    [sg.Combo(["Czerwony", "Niebieski", "Zielony", "Żółty", "Fioletowy", "Czarny", "Biały"], key="color")],
    [sg.Checkbox("Chcę otrzymywać powiadomienia", key="notifications")],
    [sg.Button("Powitaj"), sg.Button("Zresetuj")],
    [sg.Text("Wprowadzone dane:")],
    [sg.Table(values=[], headings=["Imię", "Rok urodzenia", "Płeć", "Kolor", "Powiadomienia"],
              auto_size_columns=False, justification="center", key="table", num_rows=5)]
]

window = sg.Window("HD", layout)
table_data = []

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == "Powitaj":
        name = values["name"]
        age = values["age"]
        gender = "Mężczyzna" if values["male"] else "Kobieta" if values["female"] else "Nieokreślona"
        color = values["color"] if values["color"] else "Brak ulubionego koloru"
        notifications = "Tak" if values["notifications"] else "Nie"

        if not name or not age or not age.isdigit():
            sg.popup("Proszę podać poprawne dane!")
            continue

        year_of_birth = datetime.now().year - int(age)

        table_data.append([name, year_of_birth, gender, color, notifications])
        window["table"].update(values=table_data)

        greeting = (
            f"Cześć {name}!\n"
            f"Masz {age} lat i urodziłeś/aś się w {year_of_birth} roku.\n"
            f"Płeć: {gender}\n"
            f"Ulubiony kolor: {color}\n"
            f"Czy chcesz otrzymywać powiadomienia? {notifications}"
        )
        sg.popup(greeting)

    if event == "Zresetuj":
        window["name"].update("")
        window["age"].update("")
        window["male"].update(False)
        window["female"].update(False)
        window["color"].update("")
        window["notifications"].update(False)

window.close()
