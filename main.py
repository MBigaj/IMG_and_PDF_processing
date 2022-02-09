import PySimpleGUI as sg
from functions import *

sg.theme('DarkBlack')

layout1 = [
    [sg.Text('Select one of the options below:'
             '\n--------------------------------', font='Consolas 20')],
    [sg.Button("Image - Resize")],
    [sg.Button("PDF - Merge")],
    [sg.Button("PDF - Add watermark")],
    [sg.T('')],
    [sg.Button('Exit', font='10')]
]

layout2 = [
    [sg.Text('Image - Resize:\n'
             '--------------------------------', font='Consolas 20')],
    [sg.Text('First select the images (jpg or png), That you want to resize\n'
             'Then select your desired image resolution and click Proceed')],
    [sg.Text('Choose files: '), sg.Input(key='-IN-'), sg.FilesBrowse()],
    [sg.Listbox(values=('1080', '720', '480'), default_values=['1080'], select_mode='LISTBOX_SELECT_MODE_SINGLE', size=(10, 3), key='Resolution')],
    [sg.Button('Proceed', key='validation1')],
    [sg.T('')],
    [sg.Button('Back', key='back1', font='10')]
]

layout3 = [
    [sg.Text('PDF - Merge'
             '\n--------------------------------', font='Consolas 20')],
    [sg.Text('First select the PDF files that you want to merge\n'
             'Then all you have to do is click Proceed')],
    [sg.Text('Choose files: '), sg.Input(key='-IN-0'), sg.FilesBrowse()],
    [sg.Button('Proceed', key='validation2')],
    [sg.T('')],
    [sg.Button('Back', key='back2', font='10')]
]

layout4 = [
    [sg.Text('PDF - Add watermark'
             '\n--------------------------------', font='Consolas 20')],
    [sg.Text('First select PDF files that you want to watermark\n'
             'Then select a PDF file with the watermark and click Proceed')],
    [sg.Text('Choose files: '), sg.Input(key='-IN-1'), sg.FilesBrowse()],
    [sg.Text('Choose Watermark file: '), sg.Input(key='-IN-2'), sg.FileBrowse(key='watermark')],
    [sg.Button('Proceed', key='validation3')],
    [sg.T('')],
    [sg.Button('Back', key='back3', font='10')]
]

layout_all_done = [
    [sg.Text('All Done!'
             '\n--------------------------------', font='Consolas 20')],
    [sg.Ok(font='10', size=(15, 1))]
]

layout = [
    [sg.Column(layout1, key='-COL1-'),
     sg.Column(layout2, visible=False, key='-COL2-'),
     sg.Column(layout3, visible=False, key='-COL3-'),
     sg.Column(layout4, visible=False, key='-COL4-'),
     sg.Column(layout_all_done, visible=False, key='-COL5-')]
]

window = sg.Window('Image and PDF processing Application', layout)

layout = 1

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
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
        layout = 5
        window[f'-COL{layout}-'].update(visible=True)

    if event == 'validation2':
        if values['-IN-0'] != '':
            pdf_merge(values['-IN-0'].split(';'))
        window[f'-COL{layout}-'].update(visible=False)
        layout = 5
        window[f'-COL{layout}-'].update(visible=True)

    if event == 'validation3':
        if values['-IN-1'] != '' and values['watermark'] != '':
            add_watermark(values['-IN-1'].split(';'), values['watermark'])
        window[f'-COL{layout}-'].update(visible=False)
        layout = 5
        window[f'-COL{layout}-'].update(visible=True)

    if event == 'Ok':
        window[f'-COL{layout}-'].update(visible=False)
        layout = 1
        window[f'-COL{layout}-'].update(visible=True)

window.close()
