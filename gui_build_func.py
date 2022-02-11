import PySimpleGUI as sg


def proceed_button(label, keyword):
    return sg.Button(label, key=keyword, font=('Eternal Ancient', 12), size=(10, 2))


def back_button(label, keyword):
    return sg.Button(label, key=keyword, font=('Eternal Ancient', 10), border_width=5, pad=((400, 0), (0, 0)))