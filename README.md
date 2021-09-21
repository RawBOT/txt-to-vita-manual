# Text to Vita Manual Converter

## Description

This script converts a text file into a format suitable to use as a Vita's Bubble manual. This works by rendering the text file into a series of PNG files, naming them as 001.png, 002.png, and so on, and maximizing as much space as possible.

It is intended to be used with text guides, like the ones found in sites like GameFAQs. It is configured to work with text files that follow console line width limitations (<80 characters per line) and most GameFAQs guides should follow this convention. With a font size of 22, it fits 22 lines per image. However, it can be configured by modifying the parameters in the script, such as changing the font, the font size, the number of lines in an image, etc.

## Usage

The script has the following dependencies:
* Python 3
* Pillow `pip install Pillow`

To use it, just pass the text file as the first argument:

`python main.py text-file-example.txt`

Similarly, the stand-alone version (all dependencies included) can be used by passing the text file as an argument:

`txt-to-vita-manual.exe text-file-example.txt`