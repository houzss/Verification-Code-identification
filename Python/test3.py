#!/usr/bin/python 3
# encoding: utf-8
from PIL import Image,ImageDraw
import os
# 二值化处理
def two_value():
    for i in range(0,100):
        # 打开文件夹中的图片
        image=Image.open('./Img/'+(str(i).zfill(4))+'.jpg')
        # 灰度图
        lim=image.convert('L')
        # 灰度阈值设为165，低于这个值的点全部填白色
        threshold=165
        table=[]
        for j in range(256):
            if j<threshold:
                table.append(0)
            else:
                table.append(1)
        bim=lim.point(table,'1')
        bim.save('./Img2/'+(str(i).zfill(4))+'.jpg')

#去躁
def getPixel(image,x,y,G,N):
    lx=0
    for i in range(1,G):
        if (y!=0)&((y-i)>0)&((y+i)<80) :
            if image.getpixel((x,y+i))<N:
                lx+=1
            if image.getpixel((x,y-i))<N:
                lx+=1
        else:
            return 1
    return lx
 

def clearNoise():
    for  t in range(0,100):
	    image = Image.open('./Img2/'+(str(t).zfill(4))+'.jpg')
	    image = image.convert("L")
	    w,h=image.size
        draw = ImageDraw.Draw(image)
        for x in range(0,w):
            for y in range(0,h):
                if judgeshu(image,x,y,4,50)<3:
                    draw.point((x,y),255)
	    image.save('./Img2/'+(str(t).zfill(4))+'.jpg')

#字符切割
def vertical():
    src = "./Img2/"
    src1 = "./Img3/"
    for j in range(0,100):
        img = Image.open(src + str(j).zfill(4) + ".jpg")
        w, h = img.size
        pixdata = img.load()

        x_array = []
        startX = 0
        endX = 0
        for x in range(w):
            b_count = 0
            for y in range(h):
                if pixdata[x, y] <= 5:
                    b_count += 1
            if b_count > 3.5: #***
                if startX == 0:
                    startX = x
            elif b_count == 0:
                if startX != 0:
                    endX = x
                    x_array.append({'startX': startX, 'endX': endX})
                    startX = 0
                    endX = 0
        for i, item in enumerate(x_array):
            box = (item['startX'], 0, item['endX'], h)
            regin = img.crop(box)
            regin.save(src1 + str(j).zfill(4) + "_" + str(i) + ".jpg")

    for root, dirs, files in os.walk(src1):
        count = 1
        for i in files:
            if i.endswith('.jpg'):

                img = Image.open(src1+i)
                w, h = img.size
                num = 0
                q = 0
                if w < 10 and h > 0:
                    os.remove(src1 + str(i).zfill(4))
                if w > 64 and w < 111 and h > 0:
                    colnum = 2
                    rownum = 1
                    rowheight = h // rownum
                    colwidth = w // colnum
                    for r in range(rownum):
                        for c in range(colnum):
                            box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                            regin = img.crop(box)
                            regin.save(src1 + str(i).zfill(4) + "_" + str(num) + ".jpg")
                            num = num + 1
                    os.remove(src1 + str(i).zfill(4))

                if w > 111 and w<135 and h>0:
                    colnum1 = 3
                    rownum1 = 1
                    rowheight = h // rownum1
                    colwidth = w // colnum1
                    for r in range(rownum):
                        for c in range(colnum):
                            box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                            regin = img.crop(box)
                            regin.save(src1 + str(i).zfill(4) + "_" + str(num) + ".jpg")
                            num = num + 1
                    os.remove(src1 + str(i).zfill(4))

                if w > 135 and w<185 and h>0:
                    colnum2 = 4
                    rownum2 = 1
                    rowheight = h // rownum2
                    colwidth = w // colnum2
                    for r in range(rownum):
                        for c in range(colnum):
                            box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                            regin = img.crop(box)
                            regin.save(src1 + str(i).zfill(4) + "_" + str(num) + ".jpg")
                            num = num + 1
                    os.remove(src1 + str(i).zfill(4))
                if w > 184 and h>0:
                    colnum2 = 4
                    rownum2 = 1
                    rowheight = h // rownum2
                    colwidth = w // colnum2
                    for r in range(rownum):
                        for c in range(colnum):
                            box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                            regin = img.crop(box)
                            regin.save(src1 + str(i).zfill(4) + "_" + str(num) + ".jpg")
                            num = num + 1
                    os.remove(src1 + str(i).zfill(4))




two_value()
clearNoise()    
