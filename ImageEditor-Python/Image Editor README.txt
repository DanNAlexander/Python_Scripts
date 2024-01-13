Image Editor README
______________________________

**Installation of Pillow is required to run**


EDITING IMAGE ROTATION THROUGH EDIT:
edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)
remove convert or modify if images have rotated incorrectly.