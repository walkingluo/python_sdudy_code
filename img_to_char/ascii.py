# -*- coding:utf-8 -*-

from PIL import Image
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file')
#parser.add_argument('-o', '--output')
parser.add_argument('--width', type=int, default=80)
parser.add_argument('--height', type=int, default=80)

args = parser.parse_args()

img = args.file
width = args.width
height = args.height
#output = args.output

ascii_char = list(r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
length = len(ascii_char)

def get_char(r, g, b, alpha=256):

    if alpha == 0:
        return ' '

    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = 255 / length

    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    im = Image.open(img)
    '''
    gray_img = im.convert('LA')
    gray_img.save('gray_img.png')
    '''
    gray_im = Image.open('gray_img.png')
    im = im.resize((width, height), Image.NEAREST)
    gray_im = gray_im.resize((width, height), Image.NEAREST)

    txt = ""
    print(im.getpixel((30,60)))
    print(gray_im.getpixel((30,60)))
    gray_im.show()
    '''
    for i in range(height):
        for j in range(width):
            txt += get_char(*im.getpixel((j,i)))

        txt += '\n'

    print(txt)

    with open("output.txt", 'w') as f:
        f.write(txt)
    '''