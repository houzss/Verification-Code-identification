#!/usr/bin/python 3
# encoding: utf-8
import os
import pytesseract
from PIL import Image
data=[]
src='C:/Users/bubble sponge/Desktop/Python/6/'
for j in range(0,100):
	image=Image.open(src+str(j).zfill(4)+ '.jpg')
	vcode=pytesseract.image_to_string(image).replace(' ','').replace("*x","*").replace("x*","*").replace("x","*").replace('k','*').replace("l",'').replace('T','').replace('®','*').replace('~','-').replace('O0','0').replace('%','*')
	if vcode !='':
		end=eval(vcode)
		print(vcode+"="+str(end))
	else:
		end=''
		print('NULL')
	data.append(str(j).zfill(4)+':'+vcode+'='+str(end))

	with open("./data.txt","w",encoding='UTF-8') as f:
		for i in data:
			i=str(i)+"\n"
			f.write(i)