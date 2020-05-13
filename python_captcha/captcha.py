# -*- conding:utf-8 -*-

from PIL import Image
import os
import math


class VectorCompare:

    # 计算矢量
    def magnitude(self,concordance):
        total = 0
        for word,count in concordance.items():
            total += count ** 2
        return math.sqrt(total)

    # 计算相似度
    def relation(self,concordance1, concordance2):

        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2:
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))

def buildvector(im):
    d1 = {}
    count = 0
    for i in im.getdata():
        d1[count] = i
        count += 1
    return d1

v = VectorCompare()

iconset = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

image_set = []

for letter in iconset:
    for img in os.listdir('./iconset/%s/'%(letter)):
        temp = []
        temp.append(buildvector(Image.open("./iconset/%s/%s"%(letter,img))))
        image_set.append({letter:temp})

im = Image.open("captcha.gif")
'''
his = im.histogram()
values = {}

for i in range(256):
    values[i] = his[i]

values_sorted = sorted(values.items(), key=lambda x:x[1], reverse=True)
for i,j in values_sorted[:10]:
    print(i, j)
'''
im2 = Image.new('P', im.size, 255)

for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        if pix == 220 or pix == 227:
            im2.putpixel((y,x), 0)
#im2.show()
#im2.save('new.gif')

'''
im2 = Image.open('new.gif')
print(im2.histogram())
'''

in_letter = False
found_letter = False
start = 0
end = 0
letter = []

for y in range(im2.size[0]):
    for x in range(im2.size[1]):
        pix = im2.getpixel((y,x))
        if pix != 255:
            in_letter = True

    if found_letter == False and in_letter == True:
        found_letter = True
        start = y

    if found_letter == True and in_letter == False:
        found_letter = False
        end = y
        letter.append((start, end))

    in_letter = False

#print(letter)

for l in letter:
    im3 = im2.crop((l[0], 0, l[1], im2.size[1]))

    guess = []

    for image in image_set:
        for x, y in image.items():
            if len(y) != 0:
                guess.append((v.relation(y[0], buildvector(im3)), x))

    guess.sort(reverse=True)
    print(guess[0])
