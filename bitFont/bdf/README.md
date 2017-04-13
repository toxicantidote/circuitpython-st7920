This folder was used to process .bdf files for pixel typefaces acquired originally from u8g2 Arduino library

The pilfont utility from PIL (Pillow Fork) was used to generate .pil and .pbm files extracting the typefaces into a PIL-compatible format.

For each typeface, a .png named after the typeface was generated in the rendered folder showing all printable characters, and a folder named after the typeface was generated with a single .png for each printable character in the typeface for reference.

Finally a python BitFont file was authored, found in the ../faces/ module containing all the bitmap information from the original fonts. These .py files can be used in projects to plot the typefaces using an arbitrary x,y renderer.`
