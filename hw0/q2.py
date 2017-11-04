""" Q2 of hw0:  """
#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from PIL import Image


def main():
    """ Main """
    image = Image.open("westbrook.jpg")
    for y in range(0, image.size[1]):
        for x in range(0, image.size[0]):
            orig_px = image.getpixel((x, y))
            new_px = (int(orig_px[0] / 2), int(orig_px[1] / 2), int(orig_px[2] / 2))
            image.putpixel((x, y), new_px)

    image.save("Q2.jpg")


if __name__ == '__main__':
    main()
