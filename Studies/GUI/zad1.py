import PySimpleGUI as sg
from datetime import datetime


sg.theme_background_color("darkblue")

layout = [
    [sg.Text("Podaj imię:"), sg.InputText(key="name")],
    [sg.Text("Podaj wiek:"), sg.InputText(key="age")],
    [sg.Text("Wybierz płeć:")],
    [sg.Radio("Mężczyzna", "gender", key="male"), sg.Radio("Kobieta", "gender", key="female")],
    [sg.Button("Powitaj")]
]

window = sg.Window("HD", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == "Powitaj":
        name = values["name"]
        age = values["age"]
        gender = "Mężczyzna" if values["male"] else "Kobieta" if values["female"] else "Nieokreślona"

        if not name or not age or not age.isdigit():
            sg.popup("Proszę podać poprawne dane!")
            continue

        year_of_birth = datetime.now().year - int(age)

        greeting = f"Cześć {name}!\nMasz {age} lat i urodziłeś/aś się w {year_of_birth} roku.\nPłeć: {gender}"
        sg.popup(greeting)

window.close()
