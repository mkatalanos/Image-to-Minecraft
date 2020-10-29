import cv2
from PIL import Image,ImageOps
import requests
import io
import numpy as np
import processing
import config
import mcpi.minecraft as minecraft


ip="192.168.10.99"

url = "http://{}:81/stream".format(ip)

#INVOKE ONLY ONCE
config.set_size("VGA", ip)

r=requests.get(url,stream=True)

prev=None

mc=minecraft.Minecraft.create()
c=0

if(r.status_code == 200):
    raw_bytes = bytes()
    for chunk in r.iter_content(chunk_size=1024):
        raw_bytes += chunk
        a = raw_bytes.find(b'\xff\xd8\xff')
        b = raw_bytes.find(b'\xff\xd9',a)
        if a != -1 and b != -1:
            
            
            jpg = raw_bytes[a:b+2]
            raw_bytes = raw_bytes[b+2:]
            
            imgIo=io.BytesIO(jpg)
            img=Image.open(imgIo)
            
            
            # cvImg=cv2.cvtColor(np.array(img.convert("RGB")),cv2.COLOR_RGB2BGR)
            
            
            c+=1
            c=c % 5
            if(c==0):
                processing.useImg(np.array(ImageOps.mirror(ImageOps.flip(img))),mc)

            
            
            
            
else:
    print("INVALID CODE CAN'T PROCEED")
    
    
