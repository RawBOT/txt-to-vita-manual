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
max_lines_per_image = 22

# Other params
max_chars_per_line = 80
output_dir = "Manual/"


if __name__ == "__main__":
    os.makedirs(output_dir, exist_ok=True)
    txt_file_path = sys.argv[1]

    # Load fonts
    normal_font = ImageFont.truetype(font_path, size=font_size)  # font used for guide text
    half_font = ImageFont.truetype(font_path, size=11)  # font used for top-right line idx

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
        num_lines = len(txt_content)  # num. lines in the text guide
        num_pages = math.ceil(num_lines/max_lines_per_image)  # num. of pages/images (rounded up) in the vita guide

        # Check if predicted number of pages exceed Vita's max of {max_imgs}
        if num_pages > max_imgs:
            max_lines = max_imgs*max_lines_per_image
            print("ERROR:The text file exceeds the maximum length allowed!")
            print("      Current: {0}, Max: {1} lines".format(num_lines, max_lines))
            quit()

        # main loop
        for current_page in range(num_pages):
            print("Progress: {0} / {1}".format(current_page+1, num_pages))

            # Initialize image
            image = Image.new("RGB", img_size, bgcolor)
            draw = ImageDraw.Draw(image)

            # Draw border
            border_coord = [(int(start_coord[0] / 2), int(start_coord[1] / 2)), \
                            (int(img_size[0] - (start_coord[0] / 2)), int(img_size[1] - (start_coord[1] / 2)))]
            draw.rectangle(border_coord, outline=fgcolor, width=2)

            # line ranges for image
            current_line = current_page * max_lines_per_image
            line_idx = slice(current_line, min(current_line + max_lines_per_image, num_lines))

            # Draw top-right lines idx text: "{current_line} / {num_lines}"
            text_coord = (int(img_size[0] - (start_coord[0] / 2)), 2)
            draw.text(text_coord, "{0} / {1}".format(line_idx.start, num_lines), \
                      font=half_font, fill=fgcolor, anchor="rt")  # anchored to right-top

            # Draw lines contained in image from: current_line -> {current_line} + {max_lines_per_image}
            drawn_text = ''.join(txt_content[line_idx]).expandtabs()  # Expand tabs to match original look
            draw.multiline_text(start_coord, drawn_text, font=normal_font, fill=fgcolor, spacing=0)

            # Save image with a [000].png format
            image.save(output_dir + "{0:03d}".format(current_page+1) + ".png")
    finally:
        input_file.close()
