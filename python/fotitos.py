# -*- coding: utf-8 -*-
import os
import sys

from PIL import Image


VALID_EXTENSIONS = ['.JPG', '.jpg', '.PNG', '.png', '.BMP',  '.bmp']
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


def main(folder, size):
    count = 0
    photos = os.listdir(folder)
    total = len(photos)
    x, y = size.split('x')
    width, height = tuple(int(v) for v in size.split('x'))
    new_folder = '{}/thumbs'.format(folder)
    
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    for photo in photos:
        path = '{}/{}'.format(folder, photo)
        new_path = '{}/{}'.format(new_folder, photo)

        # Check for valid extensions
        ext = os.path.splitext(path)[1]
        if ext not in VALID_EXTENSIONS:
            continue

        img = Image.open(path)

        # Save image with new dimensions
        new_img = img.resize((width, height), Image.ANTIALIAS)
        new_img.save(new_path, quality=100, optimize=True)
        count += 1

        points = CURSOR_UP_ONE + ERASE_LINE + "." * count + "\n"
        sys.stdout.write("{}".format(points))
        sys.stdout.write(
            "Progress: {} of {} \r".format(count, total)
        )
        sys.stdout.flush()

    print("You converted {} images from the {} directory.".format(
        count, folder
    ))
    print("\n")
    print("---- Thanks for using fotitos.py ----")


if __name__ == '__main__':
    #
    # Validate arguments
    #
    if len(sys.argv) == 3:
        folder = sys.argv[1]
        size = sys.argv[2]
    else:
        print("Incorrect arguments")
        exit()

    main(folder, size)


# Usage sample
# python fotitos.py images 268x356

