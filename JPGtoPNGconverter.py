# python3 JPGtoPNGconverter.py Pokedex\ new\

import sys
import os
from PIL import Image

def convert(src_dir, new_dir):
	try:
		for filename in os.listdir(src_dir):
			if filename.endswith('.jpg'):
				img = Image.open(f'{src_dir}/{filename}')
				img_path = os.path.basename(new_dir)
				# filename = filename.replace('.jpg', '')
				img_name = os.path.splitext(filename)[0]	# os.path.splittext divides filename by: ('name', 'extension')
				img.save(f"{new_dir}/{img_name}.png", 'png')
	except FileNotFoundError:
		print(f"File '{src_dir}' could not be found!")
	return 0

try:
	source_folder = sys.argv[1]
	new_folder = sys.argv[2]
except IndexError:
	print('Please give 2 arguments')

try:
	if os.path.exists(source_folder):
		if not os.path.exists(new_folder):
			os.mkdir(new_folder)

		convert(source_folder, new_folder)
	else:
		raise FileNotFoundError(f"File {source_folder} could not be found")
except NameError:
	print('Not enough arguments to call function')