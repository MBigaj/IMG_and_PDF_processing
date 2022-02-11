import PySimpleGUI as sg


def proceed_button(label, keyword):
    return sg.Button(label, key=keyword, size=(10, 2))