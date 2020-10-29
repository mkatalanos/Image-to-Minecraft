# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 19:19:40 2020

@author: Marios
"""
import numpy as np
import mcpi.block as block
import mcpi.minecraft as minecraft
from skimage import io
import os
import re

blocks=[]
with open("blocks.csv",'r') as file:
    lines=file.readlines()

    for line in lines:
        line=line.strip('\n').split(',')
        idx=int(line[0]); data=int(line[1]); averageS=line[2]
        mc_block=(idx,data,np.fromstring(averageS[1:-1],sep=' '))
        blocks.append(mc_block)

# print(blocks)

def colorToBlock(RGB):
    
    #RGB (R,G,B)
    cols=np.array([block[2] for block in blocks])
    color=np.array(RGB)
    #distances=np.sqrt(np.sum((cols-color)**2,axis=1))
    distances=np.linalg.norm(cols-color,axis=1)
    closest_idx=np.argmin(distances)
    
    return blocks[closest_idx]

def blockToMinecraft(b):
    return block.Block(b[0],data=b[1])



def convertImage(img):
    height,width,_=np.shape(img)
    imgArr=np.array(img)
    imgBlocks=[[None for i in range(width)] for j in range(height)]
    for y in range(height):
        for x in range(width):
            rgb=imgArr[y,x]
            block=blockToMinecraft(colorToBlock(rgb))
            imgBlocks[y][x]=block
    return imgBlocks
    

def drawImage(mc,img):
    pos=(0,20,0)
    blocks=convertImage(img)
    height,width,_=np.shape(img)
    
    for y in range(height):
        for x in range(width):
            mc.setBlock(pos[0]+x,pos[1]+y,pos[2],blocks[y][x])
    
            
    
