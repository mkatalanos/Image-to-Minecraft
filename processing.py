# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 06:28:55 2020

@author: Marios
"""
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
import mc

#SCREENCAP
from mss import mss
from PIL import Image,ImageOps
import pyscreenshot as ImageGrab
import mcpi.minecraft as minecraft


scale=55
ratio=1.333333



def useImg(img,minecraft):
    
    img=cv2.resize(img,(int(scale*ratio),scale))
    mc.drawImage(minecraft,img)
    
    cv2.imshow('Test', np.array(img))
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        sys.exit()
        
        

if __name__=="__main__":        
    mcp=minecraft.Minecraft.create()
    a=0
    ratio=1.77777778
    while True:
        img=ImageGrab.grab(bbox=(1920,244,3840,1080+244))
        
        a+=1
        a=a%1
        if a==0:
            useImg(np.array(ImageOps.mirror(ImageOps.flip(img))),mcp)
