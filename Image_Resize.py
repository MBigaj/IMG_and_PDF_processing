from PIL import Image
import sys
import os

src_dir = sys.argv[1]

if os.path.isdir(src_dir) is False:
	print(f'Folder {src_dir} not found...')
	sys.exit(1)

if os.path.isdir('Reduced_img') is False:
	os.mkdir('Reduced_img')

for filename in os.listdir(src_dir):
	image = Image.open(f'{src_dir}/{filename}')
	image.thumbnail((1920, 1920))
	# rotated = image.rotate(-90)

	img_name = os.path.splitext(filename)[0]
	image.save(f"Reduced_img/{img_name}.jpg")