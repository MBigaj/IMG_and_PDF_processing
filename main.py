import PySimpleGUI as sg
from functions import *


def eng_main():
    sg.theme('DarkBlack')

    layout1 = [
        [sg.Text('Select one of the options below:'
                 '\n--------------------------------', font='Consolas 20')],
        [sg.Button("Image - Resize")],
        [sg.Button("PDF - Merge")],
        [sg.Button("PDF - Add watermark")],
        [sg.T('')],
        [sg.Button('Polish', font='10'), sg.Button('Exit', font='10')]
    ]

    layout2 = [
        [sg.Text('Image - Resize:\n'
                 '--------------------------------', font='Consolas 20')],
        [sg.Text('First select the images (jpg or png), That you want to resize\n'
                 'Then select your desired image resolution and click Proceed')],
        [sg.Text('Choose files: '), sg.Input(key='-IN-', do_not_clear=False), sg.FilesBrowse(file_types=(('All JPG/PNG Files', '*.*g'), ))],
        [sg.Listbox(values=('1080', '720', '480'), default_values=['1080'], select_mode='LISTBOX_SELECT_MODE_SINGLE', size=(10, 3), key='Resolution'),
         sg.Button('Proceed', key='validation1', size=(10, 2))],
        [sg.T('')],
        [sg.Button('Back', key='back1', font='10')]
    ]

    layout3 = [
        [sg.Text('PDF - Merge'
                 '\n--------------------------------', font='Consolas 20')],
        [sg.Text('First select the PDF files that you want to merge\n'
                 'Then all you have to do is click Proceed')],
        [sg.Text('Choose files: '), sg.Input(key='-IN-0', do_not_clear=False), sg.FilesBrowse(file_types=(('All PDF Files:', '*.pdf'), ))],
        [sg.Button('Proceed', key='validation2')],
        [sg.T('')],
        [sg.Button('Back', key='back2', font='10')]
    ]

    layout4 = [
        [sg.Text('PDF - Add watermark'
                 '\n--------------------------------', font='Consolas 20')],
        [sg.Text('First select PDF files that you want to watermark\n'
                 'Then select a PDF file with the watermark and click Proceed')],
        [sg.Text('Choose files: '), sg.Input(key='-IN-1', do_not_clear=False), sg.FilesBrowse(file_types=(('All PDF Files:', '*.pdf'), ))],
        [sg.Text('Choose Watermark file: '), sg.Input(key='-IN-2'), sg.FileBrowse(key='watermark', file_types=(('All PDF Files:', '*.pdf'), ))],
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

        if event == 'Polish':
            window.close()
            pl_main()

    window.close()


def pl_main():
    layout1 = [
        [sg.Text('Wybierz jedną z opcji:'
                 '\n--------------------------------', font='Consolas 20')],
        [sg.Button("Zmień rozmiar obrazów", key='Image - Resize')],
        [sg.Button("Połącz pliki PDF", key='PDF - Merge')],
        [sg.Button("Dodaj wybrany znak wodny do plików PDF", key='PDF - Add watermark')],
        [sg.T('')],
        [sg.Button('English', font='10'), sg.Button('Wyjdź', key='Exit', font='10')]
    ]

    layout2 = [
        [sg.Text('Zmień rozmiar obrazów:\n'
                 '--------------------------------', font='Consolas 20')],
        [sg.Text('Najpierw wybierz pliki (w formacie jpg lub png), których rozmiar chciałbyś zmienić\n'
                 'Następnie wybierz rozmiar z podanych i kliknij Potwierdź')],
        [sg.Text('Wybierz pliki: '), sg.Input(key='-IN-', do_not_clear=False), sg.FilesBrowse('Przeglądaj', file_types=(('All JPG/PNG Files', '*.*g'), ))],
        [sg.Listbox(values=('1080', '720', '480'), default_values=['1080'], select_mode='LISTBOX_SELECT_MODE_SINGLE',
                    size=(10, 3), key='Resolution')],
        [sg.Button('Potwierdź', key='validation1')],
        [sg.T('')],
        [sg.Button('Cofnij', key='back1', font='10')]
    ]

    layout3 = [
        [sg.Text('Połącz pliki PDF'
                 '\n--------------------------------', font='Consolas 20')],
        [sg.Text('Wybierz pliki PDF które chciałbyś połączyć w jeden\n'
                 'Następnie kliknij Potwierdź')],
        [sg.Text('Wybierz pliki: '), sg.Input(key='-IN-0', do_not_clear=False), sg.FilesBrowse('Przeglądaj', file_types=(('All PDF Files:', '*.pdf'), ))],
        [sg.Button('Potwierdź', key='validation2')],
        [sg.T('')],
        [sg.Button('Cofnij', key='back2', font='10')]
    ]

    layout4 = [
        [sg.Text('Dodaj wybrany znak wodny do plików PDF'
                 '\n--------------------------------', font='Consolas 20')],
        [sg.Text('Wybierz pliki PDF do których chciałbyś dołączyć znak wodny\n'
                 'Następnie wybierz plik PDF ze znakiem wodnym i kliknij Potwierdź')],
        [sg.Text('Wybierz pliki: '), sg.Input(key='-IN-1', do_not_clear=False), sg.FilesBrowse('Przeglądaj', file_types=(('All PDF Files:', '*.pdf'), ))],
        [sg.Text('Wybierz plik ze znakiem wodnym: '), sg.Input(key='-IN-2'), sg.FileBrowse('Przeglądaj', file_types=(('All PDF Files:', '*.pdf'), ), key='watermark')],
        [sg.Button('Potwierdź', key='validation3')],
        [sg.T('')],
        [sg.Button('Cofnij', key='back3', font='10')]
    ]

    layout_all_done = [
        [sg.Text('Skończone!'
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

        if event == 'English':
            window.close()
            eng_main()

    window.close()


if __name__ == "__main__":
    eng_main()