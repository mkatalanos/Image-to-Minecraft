# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 07:08:56 2020

@author: Marios
"""
import requests


def set_size(size,ip):
    sizes={"QQVGA":0,"HQVGA":3,"QVGA":4,"CIF":5,"VGA":6,"SVGA":7,"XGA":8,"SXGA":9,"UXGA":10}
    r=requests.get("http://{}/control?var=framesize&val={}".format(ip,sizes[size]),headers={'Connection':'close'})
    
    
def set_quality(val,ip):
    assert(10<=val<=63)
    r=requests.get("http://{}/control?var=quality&val={}".format(ip,val),headers={'Connection':'close'})
    
def set_brightness(val,ip):
    assert(-2<=val<=2)
    r=requests.get("http://{}/control?var=brightness&val={}".format(ip,val),headers={'Connection':'close'})
    
def set_contrast(val,ip):
    assert(-2<=val<=2)
    r=requests.get("http://{}/control?var=contrast&val={}".format(ip,val),headers={'Connection':'close'})

def set_saturation(val,ip):
    assert(-2<=val<=2)
    r=requests.get("http://{}/control?var=saturation&val={}".format(ip,val),headers={'Connection':'close'})