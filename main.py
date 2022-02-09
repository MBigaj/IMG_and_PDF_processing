import PySimpleGUI as sg
from functions import *

sg.theme('DarkBlack')

layout1 = [
    [sg.Text('Select one of the options below:'
             '\n--------------------------------', font='Consolas 17')],
    [sg.Button("Image - Resize")],
    [sg.Button("PDF - Merge")],
    [sg.Button("PDF - Add watermark")],
    [sg.T('')],
    [sg.OK(), sg.Cancel()]
]

layout2 = [
    [sg.Text('Image - Resize:'
             '\n--------------------------------', font='Consolas 17')],
    [sg.Text('Choose files: '), sg.Input(key='-IN-'), sg.FilesBrowse()],
    [sg.Listbox(values=('1080', '720', '480'), default_values=['1080'], select_mode='LISTBOX_SELECT_MODE_SINGLE', size=(10, 3), key='Resolution')],
    [sg.Button('Proceed', key='validation1')],
    [sg.T('')],
    [sg.Button('Back', key='back1', font='Bold')]
]

layout3 = [
    [sg.Text('PDF - Merge'
             '\n--------------------------------', font='Consolas 17')],
    [sg.Text('Choose files: '), sg.Input(key='-IN-'), sg.FilesBrowse()],
    [sg.Button('Proceed', key='validation2')],
    [sg.T('')],
    [sg.Button('Back', key='back2', font='Bold')]
]

layout4 = [
    [sg.Text('PDF - Add watermark'
             '\n--------------------------------', font='Consolas 17')],
    [sg.T('')],
    [sg.Button('Back', key='back3', font='Bold')]
]

layout = [
    [sg.Column(layout1, key='-COL1-'),
     sg.Column(layout2, visible=False, key='-COL2-'),
     sg.Column(layout3, visible=False, key='-COL3-'),
     sg.Column(layout4, visible=False, key='-COL4-')]
]

window = sg.Window('Image and PDF processing Application', layout)

layout = 1

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

    if event == 'Image - Resize':
        window[f'-COL{layout}-'].update(visible=False)
        layout = 2
        window[f'-COL{layout}-'].update(visible=True)

    if event == 'PDF - Merge':
        window[f'-COL{layout}-'].update(visible=False)
        layout = 3
        window[f'-COL{layout}-'].update(visible=True)

    if event == 'PDF - Add watermark':
        #add_watermark()
        window[f'-COL{layout}-'].update(visible=False)
        layout = 4
        window[f'-COL{layout}-'].update(visible=True)

    if event == 'back1' or event == 'back2' or event == 'back3':
        window[f'-COL{layout}-'].update(visible=False)
        layout = 1
        window[f'-COL{layout}-'].update(visible=True)

    if event == 'validation1':
        if values['-IN-'] != '':
            size_reduction(values['-IN-'].split(';'), values['Resolution'])
        window[f'-COL{layout}-'].update(visible=False)
        layout = 1
        window[f'-COL{layout}-'].update(visible=True)

    if event == 'validation2':
        if values['-IN-0'] != '':
            pdf_merge(values['-IN-0'].split(';'))
        window[f'-COL{layout}-'].update(visible=False)
        layout = 1
        window[f'-COL{layout}-'].update(visible=True)

window.close()
