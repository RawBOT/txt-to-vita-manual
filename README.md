# Text to Vita Manual Converter

## Description

This script converts a text file into a format suitable to use as a Vita's Bubble manual. This works by rendering the text file into a series of PNG files, naming them as 001.png, 002.png, and so on, and maximizing as much space as possible.

It is intended to be used with text guides, like the ones found in sites like GameFAQs. It is configured to work with text files that follow console line width limitations (<80 characters per line) and most GameFAQs guides should follow this convention. With a font size of 22, it fits 22 lines per image. However, it can be configured by modifying the parameters in the script, such as changing the font, the font size, the number of lines in an image, etc.

<!-- 
![manual-1](img/manual-1.jpg)
![manual-2](img/manual-2.jpg)
![manual-3](img/manual-3.jpg)
-->

<table>
<tr>
<td><img src="img/manual-1.jpg"/></td>
<td><img src="img/manual-2.jpg"/></td>
<td><img src="img/manual-3.jpg"/></td>
</tr>
</table> 

## Modes

* **Fullscreen:** Native Fullscreen (960x544)
* **Native Width Scrollable:** Native Width with Scrolling (960x750)
* **Max Height Scrollable:** Max Possible Height with Scrolling (480x1500)
* **Minimum Width Scrollable:** Minimum Width with Scrolling (544x1420)
* **Best Width Scrollable:** 720px Width with Scrolling (720x1072)
* **Vertical:** Native Fullscreen, but rotated. Hold your Vita sideways! (544x960)

### Examples

[Link to examples](https://github.com/RawBOT/txt-to-vita-manual/tree/main/img)

<table>
<tr>
<td>Fullscreen</td>
<td>Best Width Scrollable</td>
<td>Vertical</td>
</tr>
<tr>
<td><img src="img/example_fullscreen/001.png"/></td>
<td><img src="img/example_best_width_scrollable/001.png" /></td>
<td><img src="img/example_vertical/001.png"/></td>
</tr>
</table>

## Usage

The script has the following dependencies:
* Python 3
* Pillow `pip install Pillow`

Here are the usage instructions:

```
Usage: main.py [OPTIONS] FILE

Converts a text file into PNG files to be used as a Vita manual

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -o DIR, --outputdir=DIR
                        Output images to DIR
  -v, --verbose         Outputs detailed status per file.

  Vita Manual Mode, default="fullscreen":
    --fullscreen        Native Fullscreen (960x544)
    --native            Native Width with Scrolling (960x750)
    --maxheight         Max Possible Height with Scrolling (480x1500)
    --minwidth          Minimum Width with Scrolling (544x1420)
    --midwidth          720px Width with Scrolling (720x1072)
    --vertical          Native Fullscreen, but rotated. Hold your Vita
                        sideways! (544x960)
```

For example, to output the standard "fullscreen" images:  
`python main.py file.txt`

Another example, to output "maxheight" images to a `output/` dir:  
`python main.py --maxheight -o output/ file.txt`



Similarly, the stand-alone version (all dependencies included) can be used by by replacing `python main.py` with `txt-to-vita-manual.exe`

`txt-to-vita-manual.exe --fullscreen file.txt`

## Output and Using the Manual on the Vita

PNG files will be outputted to an `Manual/` directory in the working dir. To use them on a bubble on the Vita, there's two options:

### Existing Manual
If the app/bubble you want to modify is a Vita game, or if it is a PSX/PSP bubble that already has a manual in the Live Area, then just copy and replace the PNG files in the app/bubble's directory, e.g. `ux0:app/<app-id>/sce_sys/Manual`. 

Note: this directory should already exist (every bubble with a working manual has it), and make sure to remove all files on this directory first.

### No manual
If the bubble you want to add the manual to doesn't have a manual already (No "manual" book icon in the Live Area of the bubble), then you need to use [Adrenaline Bubble Manager (ABM)](https://github.com/ONElua/AdrenalineBubbleManager).

- Copy the `Manual` directory produced by this script to `ux0:ABM/<any-dir>`. Note that the final directory where the PNG files are must be `ux0:ABM/<any-dir>/Manual/*.png` 
- On ABM, press `Circle` to modify bubbles, select your desired bubble and press `Cross` to "Inject imgs". 
- Navigate to `<any-dir>`, and you should see `Manual` in the screen. 
- Press `Start` to "load all images to the bubble", and wait for the process to finish. 
- After this, you'll now see the "manual" icon in the bubble's Live Area.
