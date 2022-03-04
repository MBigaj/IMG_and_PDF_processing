from PIL import Image
import PyPDF2
import os
# from pdf2docx import Converter


def pdf_to_docx():
    pass


def add_watermark(pdf_paths, watermark_path):
    if os.path.isdir('Edited_pdf') is False:
        os.mkdir('Edited_pdf')

    pdf_list = (pdf for pdf in pdf_paths if os.path.splitext(pdf)[1] == '.pdf')
    if os.path.splitext(watermark_path)[1] != '.pdf':
        watermark_path = ''

    if pdf_list and watermark_path:
        for pdf in pdf_list:
            pdf_file = PyPDF2.PdfFileReader(open(pdf, 'rb'))
            watermark = PyPDF2.PdfFileReader(open(watermark_path, 'rb'))
            output = PyPDF2.PdfFileWriter()

            for i in range(pdf_file.getNumPages()):
                page = pdf_file.getPage(i)
                page.mergePage(watermark.getPage(0))
                output.addPage(page)

            pdf_name = os.path.basename(pdf)
            pdf_name = pdf_name.split('.')
            with open('Edited_pdf/watermarked_' + pdf_name[0] + '.pdf', 'wb') as new_file:
                output.write(new_file)


def pdf_merge(pdf_paths):
    if os.path.isdir('Merged_pdf') is False:
        os.mkdir('Merged_pdf')

    pdf_list = (pdf for pdf in pdf_paths if os.path.splitext(pdf)[1] == '.pdf')
    if pdf_list:
        counter = len(os.listdir('Merged_pdf')) + 1
        merger = PyPDF2.PdfFileMerger()
        for pdf in pdf_list:
            merger.append(open(pdf, 'rb'))
        with open(f'Merged_pdf/merged_pdf{counter}.pdf', 'wb') as file:
            merger.write(file)


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
        image.save(f"Reduced_img/{img_name[0]}_{resolution}{ext}")
