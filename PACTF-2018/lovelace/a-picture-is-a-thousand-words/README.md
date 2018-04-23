## Problem

Apparently there is something hidden in this [image](https://github.com/unlimited-reagents/writeups-2018/raw/master/PACTF-2018/lovelace/a-picture-is-a-thousand-words/image.jpg)…

## Hint

You’re looking for text—how might you look at the text of the image?

## Writeup

The hint suggests looking at the text of the image, which sounds a whole lot like exif data to me! After running the image through `exiftool`, you get a line that looks like `Artist                          : flag_is_DjKVIXXQRZZrrAd`.

From this, you can reasonably assume that the flag is `DjKVIXXQRZZrrAd`
