from tools_func import *
from gui_build_func import *

def eng_main():
    sg.theme('DarkBlack')

    layout1 = [
        [sg.Text('Select one of the options below:\n'
                 '-----------------------------------------------', font=('Impact',  30), justification='center')],
        [sg.Button('Image - Resize', font=('Eternal Ancient', 20), size=(20))],
        [sg.Button('PDF - Merge', font=('Eternal Ancient', 20), size=(20))],
        [sg.Button('PDF - Add watermark', font=('Eternal Ancient', 20), size=(20))],
        [sg.Text('-----------------------------------------------', font=('Impact', 30), justification='center')],
        [sg.Text('Language:', font=('Impact',))],
        [sg.Button('Polish', font=('Eternal Ancient', 10)), sg.Button('Exit', font=('Eternal Ancient', 10), border_width=5, pad=((400, 0), (0, 0)))]
    ]

    layout2 = [
        [sg.Text('Image - Resize:\n'
                 '---------------------------------------', font=('Impact',  30), justification='center')],
        [sg.Text('First select the images\n'
                 '(jpg or png) that you want to resize\n'
                 'Then select your desired image\n'
                 'resolution and click -Proceed-', font=('Impact', 16), justification='center'),
         sg.Listbox(values=('1080', '720', '480'), default_values=['1080'], select_mode='LISTBOX_SELECT_MODE_SINGLE', size=(5, 3), key='Resolution', font=('Eternal Ancient', 17))],
        [sg.T('')],
        [sg.Text('Choose files: ', font=('Impact', 15, 'underline'))],
        [sg.Input(key='-IN-', do_not_clear=False), sg.FilesBrowse(file_types=(('All JPG/PNG Files', '*.??g'), ), font=('Eternal Ancient', 10), pad=((25, 0), (0, 0)))],
        [sg.T('')],
        [proceed_button('Proceed', 'validation1')],
        [back_button('Back', 'back1')]
    ]

    layout3 = [
        [sg.Text('PDF - Merge\n'
                 '-------------------------------------', font=('Impact',  30), justification='center')],
        [sg.Text('First select the PDF files that you want to merge\n'
                 'Then all you have to do is click Proceed', font=('Impact', 16), justification='center')],
        [sg.T('')],
        [sg.Text('Choose files: ', font=('Impact', 15, 'underline'))],
        [sg.Input(key='-IN-0', do_not_clear=False), sg.FilesBrowse(file_types=(('All PDF Files:', '*.pdf'), ), font=('Eternal Ancient', 10), pad=((25, 0), (0, 0)))],
        [sg.T('')],
        [proceed_button('Proceed', 'validation2')],
        [sg.T('')],
        [back_button('Back', 'back2')]
    ]

    layout4 = [
        [sg.Text('PDF - Add watermark\n'
                 '-------------------------------------------', font=('Impact',  30), justification='center')],
        [sg.Text('First select PDF files that you want to watermark\n'
                 'Then select a PDF file with the watermark and click Proceed', font=('Impact', 16), justification='center')],
        [sg.T('')],
        [sg.Text('Choose files: ', font=('Impact', 15, 'underline'))],
        [sg.Input(key='-IN-1', do_not_clear=False), sg.FilesBrowse(file_types=(('All PDF Files:', '*.pdf'), ), font=('Eternal Ancient', 10), pad=((25, 0), (0, 0)))],
        [sg.Text('Choose Watermark file: ', font=('Impact', 15, 'underline'))],
        [sg.Input(key='-IN-2'), sg.FileBrowse(key='watermark', file_types=(('All PDF Files:', '*.pdf'), ), font=('Eternal Ancient', 10), pad=((25, 0), (0, 0)))],
        [sg.T('')],
        [proceed_button('Proceed', 'validation3')],
        [sg.T('')],
        [back_button('Back', 'back3')]
    ]

    layout5 = [
        [sg.Text('PDF -> DOCX converter\n'
                 '-----------------------------------------------', font=('Impact', 30), justification='center')],
        [sg.Text('First select PDF files that you want to watermark\n'
                 'Then select a PDF file with the watermark and click Proceed', font=('Impact', 16), justification='center')],
        [sg.Text('Choose files: '), sg.Input(key='-IN-1', do_not_clear=False),
         sg.FilesBrowse(file_types=(('All PDF Files:', '*.pdf'),))],
        [sg.Text('Choose Watermark file: '), sg.Input(key='-IN-2'),
         sg.FileBrowse(key='watermark', file_types=(('All PDF Files:', '*.pdf'),))],
        [proceed_button('Proceed', 'validation3')],
        [sg.T('')],
        [back_button('Back', 'back3')]
    ]

    layout_all_done = [
        [sg.Text('All Done!\n'
                 '----------------', font=('Impact',  30), justification='center')],
        [sg.Button('Ok', font=('Eternal Ancient', 15), expand_x=True)]
    ]

    layout = [
        [sg.Column(layout1, key='-COL1-'),
         sg.Column(layout2, visible=False, key='-COL2-'),
         sg.Column(layout3, visible=False, key='-COL3-'),
         sg.Column(layout4, visible=False, key='-COL4-'),
         sg.Column(layout5, visible=False, key='-COL5-'),
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

        if event == 'PDF -> DOCX converter':
            window[f'-COL{layout}-'].update(visible=False)
            layout = 5
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
        [sg.Text('Wybierz jedn?? z opcji:'
                 '\n-----------------------------------------------', font=('Impact',  30), justification='center')],
        [sg.Button("Zmie?? rozmiar obraz??w", key='Image - Resize', font=('Eternal Ancient', 20), size=(20))],
        [sg.Button("Po????cz pliki PDF", key='PDF - Merge', font=('Eternal Ancient', 20), size=(20))],
        [sg.Button("Dodaj wybrany znak wodny do plik??w PDF", key='PDF - Add watermark', font=('Eternal Ancient', 20), size=(20))],
        [sg.Text('-----------------------------------------------', font=('Impact', 30), justification='center')],
        [sg.Text('J??zyk:', font=('Impact',))],
        [sg.Button('English', font=('Eternal Ancient', 10)), sg.Button('Wyjd??', key='Exit', font=('Eternal Ancient', 10))]
    ]

    layout2 = [
        [sg.Text('Zmie?? rozmiar obraz??w:\n'
                 '----------------------------------------------', font=('Impact', 30), justification='center')],
        [sg.Text('Najpierw wybierz pliki (w formacie jpg lub png),\n'
                 'kt??rych rozmiar chcia??by?? zmieni??\n'
                 'Nast??pnie wybierz rozmiar\n'
                 'z podanych i kliknij Potwierd??', font=('Impact', 16), justification='center'),
         sg.Listbox(values=('1080', '720', '480'), default_values=['1080'], select_mode='LISTBOX_SELECT_MODE_SINGLE',
                    size=(5, 3), key='Resolution', font=('Eternal Ancient', 17))],
        [sg.T('')],
        [sg.Text('Wybierz pliki: ', font=('Impact', 15, 'underline'))],
        [sg.Input(key='-IN-', do_not_clear=False),
         sg.FilesBrowse('Przegl??daj', file_types=(('All JPG/PNG Files', '*.??g'), ), font=('Eternal Ancient', 10), pad=((25, 0), (0, 0)))],
        [sg.T('')],
        [proceed_button('Potwierd??', 'validation1')],
        [back_button('Cofnij', 'back1')]
    ]

    layout3 = [
        [sg.Text('Po????cz pliki PDF'
                 '\n--------------------------------', font='Consolas 20')],
        [sg.Text('Wybierz pliki PDF kt??re chcia??by?? po????czy?? w jeden\n'
                 'Nast??pnie kliknij Potwierd??')],
        [sg.Text('Wybierz pliki: '), sg.Input(key='-IN-0', do_not_clear=False), sg.FilesBrowse('Przegl??daj', file_types=(('All PDF Files:', '*.pdf'), ))],
        [proceed_button('Potwierd??', 'validation2')],
        [sg.T('')],
        [back_button('Cofnij', 'back2')]
    ]

    layout4 = [
        [sg.Text('Dodaj wybrany znak wodny do plik??w PDF'
                 '\n--------------------------------', font='Consolas 20')],
        [sg.Text('Wybierz pliki PDF do kt??rych chcia??by?? do????czy?? znak wodny\n'
                 'Nast??pnie wybierz plik PDF ze znakiem wodnym i kliknij Potwierd??')],
        [sg.Text('Wybierz pliki: '), sg.Input(key='-IN-1', do_not_clear=False), sg.FilesBrowse('Przegl??daj', file_types=(('All PDF Files:', '*.pdf'), ))],
        [sg.Text('Wybierz plik ze znakiem wodnym: '), sg.Input(key='-IN-2'), sg.FileBrowse('Przegl??daj', file_types=(('All PDF Files:', '*.pdf'), ), key='watermark')],
        [proceed_button('Potwierd??', 'validation3')],
        [sg.T('')],
        [back_button('Cofnij', 'back3')]
    ]

    layout_all_done = [
        [sg.Text('Sko??czone!'
                 '\n--------------------------------', font='Consolas 20')],
        [sg.Button('Ok', font='10', size=(15, 2), expand_x=True)]
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
