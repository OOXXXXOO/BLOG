import os
import numpy
from glob import glob
def main():
    
    photopath="source/photos/"
    gallarymd="source/gallary/index.md"
    title="""---
title: gallery
date: 2019-11-30 16:00:17
type: "gallery"
layout: "gallery"
---\n
"""
    with open(gallarymd,"w") as index:
        index.write(title)
        for file in list(glob(photopath+"*.jpeg")):
            filename="![]("+file.replace("source","")+")\n"
            print(filename)
            index.writelines(filename)
            
            
    index.close()

if __name__=='__main__':
    main()