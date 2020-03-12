from PIL import Image,ImageDraw
import os
import pytesseract
# 图片数量
MIN=0
MAX=50
# 二值化处理

def two_value():
    for i in range(MIN,MAX):
        # 打开文件夹中的图片
        src="C:/Users/bubble sponge/Desktop/Python/Img/"
        src1="C:/Users/bubble sponge/Desktop/Python/Img2/"
        image=Image.open(src+(str(i).zfill(4))+'.jpg')
        # 灰度图
        lim=image.convert('L')
        # 灰度阈值设为165，低于这个值的点全部填白色
        threshold=220
        table=[]
        for j in range(256):
            if j<threshold:
                table.append(0)
            else:
                table.append(1)
        bim=lim.point(table,'1')
        bim.save(src1+(str(i).zfill(4))+'.jpg')

def judge(image,x,y,A,G):
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

def judge1(image,x,y,A,G):
    jx=0
    for i in range(1,A):
        if (x!=0)&((x-i)>0)&((x+i)<350) :
            if image.getpixel((x+i,y))<G:
                jx+=1
            if image.getpixel((x-i,y))<G:
                jx+=1
        else:
            return 1
    return jx

def clearnoise():
    src="C:/Users/bubble sponge/Desktop/Python/Img2/"
    src1="C:/Users/bubble sponge/Desktop/Python/Img3/"
    for i in range(MIN,MAX):
        image = Image.open(src+(str(i).zfill(4))+'.jpg')
        image = image.convert("L")
        w,h=image.size
        draw = ImageDraw.Draw(image)
        for x in range(0,w):
            for y in range(0,h):
                if (judge(image,x,y,4,50)<3)|(judge1(image,x,y,4,50)<3):
                    draw.point((x,y),255)
        image.save(src1+(str(i).zfill(4))+'.jpg')
    

# 识别过程+结果
def recognize():
    src="C:/Users/bubble sponge/Desktop/Python/Img3/"
    src1="C:/Users/bubble sponge/Desktop/Python/"
    f = open(src1+'data.txt','w')
    
    for j in range(MIN,MAX):
        image=Image.open(src+str(j).zfill(4)+ '.jpg')
        vcode=pytesseract.image_to_string(image).replace("(","1").replace(")","1").replace("[","1").replace("]","1").replace("}","1").replace("{","1").replace(' ','').replace("*x","*").replace("x*","*").replace("x","*").replace('k','*').replace("l",'').replace('T','').replace('®','*').replace('~','-').replace('O0','0').replace('%','*').replace("«","*").replace("**","*")
        try:
            if vcode !='':
                end=eval(vcode)
                f.write((str(j).zfill(4))+":"+vcode+"="+str(end)+"\n")
            
            else:
                end=''
                f.write((str(j).zfill(4))+":"+vcode+"=NULL"+"\n")
        except BaseException:
            f.write((str(j).zfill(4))+":"+vcode+"=NULL"+"\n")
        continue
    f.close()




two_value()
clearnoise()
recognize()

