# Copyright (c) 2021 RawBOT

import math, os, sys
from PIL import Image, ImageDraw, ImageFont

class image_config:
    def __init__(self, image_size, font_size, max_lines_per_image, start_coord, rotate) -> None:
        self.image_size = image_size
        self.font_size = font_size
        self.max_lines_per_image = max_lines_per_image
        self.start_coord = start_coord
        self.rotate = rotate

max_imgs = 999
font_path = "fonts/iosevka-fixed-regular.ttf"
fgcolor = "white"
bgcolor = "black"
max_chars_per_line = 80
output_dir = "Manual/"
line_tracker_font_size = 11

def fullscreen_image_config():
    return image_config((960, 544), 21, 23, (40,28), False)

def native_width_scrollable_image_config():
    return image_config((960, 750), 21, 33, (40,26), False)  # native width

def max_height_scrollable_image_config():
    return image_config((480, 1500), 9, 161, (40,26), False)  # max height

def min_width_scrollable_image_config():
    return image_config((544, 1420), 11, 124, (33,26), False)  # "min" width / max height

def best_width_scrollable_image_config():
    return image_config((720, 1072), 15, 68, (40,26), False)  # 720 for less blurriness

def vertical_image_config():
    return image_config((544, 960), 11, 82, (33,30), True)

if __name__ == "__main__":
    config = fullscreen_image_config()
    # config = native_width_scrollable_image_config()
    # config = max_height_scrollable_image_config()
    # config = min_width_scrollable_image_config()
    # config = best_width_scrollable_image_config()
    # config = vertical_image_config()

    os.makedirs(output_dir, exist_ok=True)
    txt_file_path = sys.argv[1]

    # Load fonts
    normal_font = ImageFont.truetype(font_path, size=config.font_size)  # font used for guide text
    half_font = ImageFont.truetype(font_path, size=line_tracker_font_size)  # font used for top-right line idx

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
        num_pages = math.ceil(num_lines/config.max_lines_per_image)  # num. of pages/images (rounded up) in the vita guide

        # Check if predicted number of pages exceed Vita's max of {max_imgs}
        if num_pages > max_imgs:
            max_lines = max_imgs*config.max_lines_per_image
            print("ERROR:The text file exceeds the maximum length allowed!")
            print("      Current: {0}, Max: {1} lines".format(num_lines, max_lines))
            quit()

        # main loop
        for current_page in range(num_pages):
            print("Progress: {0} / {1}".format(current_page+1, num_pages))

            # Initialize image
            image = Image.new("RGB", config.image_size, bgcolor)
            draw = ImageDraw.Draw(image)

            # Draw border
            border_coord = [(int(config.start_coord[0] / 2), int(config.start_coord[1] / 2)), \
                            (int(config.image_size[0] - (config.start_coord[0] / 2)),
                             int(config.image_size[1] - (config.start_coord[1] / 2)))]
            draw.rectangle(border_coord, outline=fgcolor, width=2)

            # line ranges for image
            current_line = current_page * config.max_lines_per_image
            line_idx = slice(current_line, min(current_line + config.max_lines_per_image, num_lines))

            # Draw top-right lines idx text: "{current_line} / {num_lines}"
            text_coord = (int(config.image_size[0] - (config.start_coord[0] / 2)), 2)
            draw.text(text_coord, "{0} / {1}".format(line_idx.start, num_lines), \
                      font=half_font, fill=fgcolor, anchor="rt")  # anchored to right-top

            # Draw lines contained in image from: current_line -> {current_line} + {max_lines_per_image}
            drawn_text = ''.join(txt_content[line_idx]).expandtabs()  # Expand tabs to match original look
            draw.multiline_text(config.start_coord, drawn_text, font=normal_font, fill=fgcolor, spacing=0)

            # Save image with a [000].png format
            if config.rotate:
                image = image.rotate(90, expand=True)
            image.save(output_dir + "{0:03d}".format(current_page+1) + ".png")
    finally:
        input_file.close()
