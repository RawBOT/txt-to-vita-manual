# Copyright (c) 2021 RawBOT

import math, os, sys
from PIL import Image, ImageDraw, ImageFont

# Image Size = 960x544
img_size = (960, 544)
max_imgs = 999

# Iosevka Fixed 22pt (80x22)
font_path = "fonts/iosevka-fixed-regular.ttf"
font_size = 22
fgcolor = "white"
bgcolor = "black"
start_coord = (35,30)

# Other params
max_lines_per_image = 22
max_chars_per_line = 80
output_dir = "Manual/"

if __name__ == "__main__":
    os.makedirs(output_dir, exist_ok=True)
    txt_file_path = sys.argv[1]
    normal_font = ImageFont.truetype(font_path, size=font_size)
    half_font = ImageFont.truetype(font_path, size=int(font_size / 2))

    # Open the file with UTF-8 encoding; if it fails, then with default
    try:
        input_file = open(txt_file_path, mode='r', encoding="UTF8")
        txt_content = input_file.readlines()
    except UnicodeDecodeError:
        input_file = open(txt_file_path, mode='r')
        txt_content = input_file.readlines()
    except:
        print("ERROR: Unknown file encoding!")
        quit()

    try:
        num_lines = len(txt_content)
        num_pages = math.ceil(num_lines/max_lines_per_image)
        if num_pages > max_imgs:
            max_lines = max_imgs*max_lines_per_image
            print("ERROR:The text file exceeds the maximum length allowed!")
            print("      Current: {0}, Max: {1} lines".format(num_lines, max_lines))
            quit()
        for current_page in range(num_pages):
            image = Image.new("RGB", img_size, bgcolor)
            draw = ImageDraw.Draw(image)
            # Draw border
            border_coord = [(int(start_coord[0] / 2), int(start_coord[1] / 2)), \
                            (int(img_size[0] - (start_coord[0] / 2)), int(img_size[1] - (start_coord[1] / 2)))]
            draw.rectangle(border_coord, outline=fgcolor, width=2)
            # Draw lines contained in image
            text_coord = (int(img_size[0] - (start_coord[0] / 2)), 2)
            draw.text(text_coord, "{0} / {1}".format((current_page * max_lines_per_image), num_lines), \
                      font=half_font, fill=fgcolor, anchor="rt")
            line_idx = slice(current_page*max_lines_per_image, \
                             min((current_page*max_lines_per_image) + max_lines_per_image, num_lines))
            drawn_text = ''.join(txt_content[line_idx]).expandtabs()
            draw.multiline_text(start_coord, drawn_text, font=normal_font, fill=fgcolor, spacing=0)
            image.save(output_dir + "{0:03d}".format(current_page+1) + ".png")
    finally:
        input_file.close()
