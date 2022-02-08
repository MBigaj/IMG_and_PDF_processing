import PySimpleGUI as sg
from PIL import Image
import sys
import os

def size_reduction(image_paths):
    pass


sg.theme('DarkBlack')

layout1 = [
    [sg.Text('Select one of the options below:'
             '\n--------------------------------', font='Consolas 17')],
    [sg.Button("Image - Size reduction")],
    [sg.Button("PDF - Merge")],
    [sg.Button("PDF - Add watermark")],
    [sg.OK(), sg.Cancel()]
]

layout2 = [
    [sg.Text('Image - Size reduction:', font='Consolas 17')],
    [sg.Text('Choose files: '), sg.Input(key='-IN-'), sg.FilesBrowse()],
    [sg.Button('Back', key='back1')]
]

layout3 = [
    [sg.Text('PDF - Merge', font='Consolas 17')],
    [sg.Button('Back', key='back2')]
]

layout4 = [
    [sg.Text('PDF - Add watermark', font='Consolas 17')],
    [sg.Button('Back', key='back3')]
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

    if event == 'Image - Size reduction':
        size_reduction(values['-IN-'])
        window[f'-COL{layout}-'].update(visible=False)
        layout = 2
        window[f'-COL{layout}-'].update(visible=True)
        # print(values['-IN-'])
        # break

    if event == 'PDF - Merge':
        #pdf_merge()
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

window.close()