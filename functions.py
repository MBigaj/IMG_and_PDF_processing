from PIL import Image
import PyPDF2
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


def pdf_merge(pdf_paths):
    if os.path.isdir('Merged_pdf') is False:
        os.mkdir('Merged_pdf')

    pdf_list = (pdf for pdf in pdf_paths if os.path.splitext(pdf)[1] == '.pdf')
    if pdf_list:
        merger = PyPDF2.PdfFileMerger()
        for pdf in pdf_list:
            merger.append(open(pdf, 'rb'))
        with open('Merged_pdf/result.pdf', 'wb') as file:
            merger.write(file)