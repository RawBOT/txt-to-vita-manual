# Text to Vita Manual Converter

## Description

This program takes a URL to an online text guide or to a local text file, and converts it into a format suitable to use as a Vita game's bubble manual. This can be used to replace the manual of any game, be it Vita, PSP and PSX.

This program works by rendering the text file into a series of PNG files, naming them as `001.png`, `002.png`, and so on, and maximizing as much screen space as possible.

It is intended to be used with text guides, like the ones found in sites like GameFAQs. It is configured to work with text files that follow console line width limitations (=<80 characters per line) and most GameFAQs guides should follow this convention. However, it can be configured into different modes by giving it input arguments (see [usage](#usage)).

If trying to download a GameFAQs guide, use the URL that opens the guide normally, e.g.:
`https://gamefaqs.gamespot.com/[console]/[game-id]/faqs/[faq-id]`

Currently it does not support HTML guides, only text-based ones.

You will need [rePatch-reLoaded](https://github.com/SonicMastr/rePatch-reLoaded) to replace manuals from Vita games.

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
* BeautifulSoup4 `pip install beautifulsoup4`

Here are the usage instructions:

```
Usage: main.py [OPTIONS] FILE_URL

Converts a text file into PNG files to be used as a Vita manual.
If FILE_URL is remote (e.g. Internet), then it will be downloaded and processed.

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
    --vertical          Native Fullscreen, but rotated. Hold your Vita sideways! (544x960)
```

### Examples

Output a local text file as standard "fullscreen" images:  
`python main.py test/test_simple.txt`

Output a local text file as "maxheight" images to a `output/` dir:  
`python main.py --maxheight -o output/ test/test_simple.txt`

Download a text guide and output it:
`python main.py https://example.com/text`

Download a text guide from this repo and output as "native" images:  
`python main.py --native https://raw.githubusercontent.com/RawBOT/txt-to-vita-manual/main/test/test_complex.txt`

Similarly, the stand-alone version (all dependencies included) can be used by by replacing `python main.py` with `txt-to-vita-manual.exe`

`txt-to-vita-manual.exe --fullscreen file.txt`

## Output and Using the Manual on the Vita

PNG files will be output by default to a `manual/` directory in the working dir. Vita games have their `app/` directories encrypted, so you will need [rePatch-reLoaded](https://github.com/SonicMastr/rePatch-reLoaded) to replace their manual. To use them on a bubble on the Vita, there's two options:

### Existing Manual
If the app/bubble you want to modify is a Vita game or a PSX/PSP bubble that already has a manual in the Live Area, then you need to place the `manual/` directory in its repatch folder: `ux0:repatch/<app-id>/sce_sys/manual/`. 

### No manual
If the PSP/PSX bubble you want to add the manual to, does not have a manual already (no "manual" book icon in the Live Area of the bubble), then you need to use [Adrenaline Bubble Manager (ABM)](https://github.com/ONElua/AdrenalineBubbleManager) to inject one.

- Copy the `manual` directory produced by this script to `ux0:ABM/<any-dir>`. Note that the final directory where the PNG files are must be `ux0:ABM/<any-dir>/manual/*.png` 
- On ABM, press `Circle` to modify bubbles, select your desired bubble and press `Cross` to "Inject imgs". 
- Navigate to `<any-dir>`, and you should see `manual` directory in the screen. 
- Press `Start` to "load all images to the bubble", and wait for the process to finish. 
- After this, you'll now see the "manual" icon in the bubble's Live Area.

Vita games without a manual cannot have a manual added.

## FAQ

* I don't want to install rePatch, is there a way to use the manuals?  
  If you don't want to install rePatch, then you can only replace existing manuals on PSX/PSP bubbles that you made. To do this, copy and replace the PNG files in the app/bubble's directory, e.g. `ux0:app/<app-id>/sce_sys/manual`.  
  This directory should already exist (every bubble with a working manual has it), and make sure to remove all files on this directory first. This is not recommended and the rePatch solution is preferable.  
  Note: this will not work on Vita games, as their `app/` directory is encrypted and you cannot replace the manual (even if you did, it won't work).

* When opening the manual, my Vita says that the file is corrupted!  
  This could be due to a variety of reasons:
  1. The images are too big dimension-wise (too wide or too high). I tested all presets and they all work with the Vita. They are designed to stretch the limits of what the Vita allows. If for some reason one preset doesn't work, try another one.
  2. You replaced the encrypted files of a Vita game's manual (usually via FTP or USB). Since the PNG files you copied are not encrypted, they'll look corrupted to the Vita. Please use rePatch to replace Vita game's manuals. There's no current alternative (cannot encrypt the PNG files).

* There's a mix and match between the original manual and the one I made.
  This is a limitation of using rePatch. rePatch can only replace and add new files, it cannot remove existing ones.  
  So if the original manual is 100-pages long (`001.png` to `100.png`), and you replace it with a 60-page manual (`001.png` to `060.png`), the last 40 images will be from the original manual (the original `061.png` to `100.png`).

* What's my game ID? (shown as <app-id> in this README)  
  You can find your game's ID in GameFAQs or any release database. In GameFAQs, it'll be in the `Release Data` section, under the `Product ID` column. Make sure to remove the hyphen (`-`).  
  You could also look around your `ux0:app/` directory and try to find it out by looking at the game icons.

* ABM doesn't let me install the manual images!  
  Make sure that there's a directory between `ux0:ABM/` and `manual/`, for example: `ux0:ABM/AGAMEDIR/manual/`.
