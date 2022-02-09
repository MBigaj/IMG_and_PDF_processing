import PySimpleGUI as sg
from PIL import Image
import sys
import os


def size_reduction(image_paths, resolution):
    if os.path.isdir('Reduced_img') is False:
        os.mkdir('Reduced_img')

    resolution = int(resolution[0])

    for single_path in image_paths:
        ext = os.path.splitext(single_path)[1]
        if ext != '.jpg' and ext != '.png':
            continue

        image = Image.open(single_path)

        img_name = os.path.basename(single_path)
        img_name = img_name.split('.')

        if resolution == 1080:
            image.thumbnail((1920, 1920))
        elif resolution == 720:
            image.thumbnail((1280, 1280))
        elif resolution == 480:
            image.thumbnail((640, 640))

        image.save(f"Reduced_img/{img_name[0]}{ext}")


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
    [sg.Text('Image - Resize:', font='Consolas 17')],
    [sg.T('')],
    [sg.Text('Choose files: '), sg.Input(key='-IN-'), sg.FilesBrowse()],
    [sg.Listbox(values=('1080', '720', '480'), default_values=['1080'], select_mode='LISTBOX_SELECT_MODE_SINGLE', size=(10, 3), key='Resolution')],
    [sg.Button('Proceed', key='validation1')],
    [sg.T('')],
    [sg.Button('Back', key='back1', font='Bold')]
]

layout3 = [
    [sg.Text('PDF - Merge', font='Consolas 17')],
    [sg.T('')],
    [sg.Button('Back', key='back2', font='Bold')]
]

layout4 = [
    [sg.Text('PDF - Add watermark', font='Consolas 17')],
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

    if event == 'validation1':
        if values['-IN-'] != '':
            size_reduction(values['-IN-'].split(';'), values['Resolution'])
        window[f'-COL{layout}-'].update(visible=False)
        layout = 1
        window[f'-COL{layout}-'].update(visible=True)

window.close()