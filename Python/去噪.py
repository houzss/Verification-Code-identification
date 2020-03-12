#coding:utf-8
import sys,os
from PIL import Image,ImageDraw
 
src="C:/Users/16329/Desktop/验证码样本数据/2/"
src1="C:/Users/16329/Desktop/验证码样本数据/6/"


def judgeshu(image,x,y,A,G):
    lx=0
    for i in range(1,A):
        if (y!=0)&((y-i)>0)&((y+i)<80) :
            if image.getpixel((x,y+i))<G:
                lx+=1
            if image.getpixel((x,y-i))<G:
                lx+=1
        else:
            return 1
    return lx

def clearnoise1():
    for i in range(0,100):
        image = Image.open(src+(str(i).zfill(4))+'.jpg')
        image = image.convert("L")
        w,h=image.size
        draw = ImageDraw.Draw(image)
        for x in range(0,w):
            for y in range(0,h):
                if judgeshu(image,x,y,4,50)<3:
                    draw.point((x,y),255)
        image.save(src1+(str(i).zfill(4))+'.jpg')
    

clearnoise1()