import PIL
from PIL import Image
import os

mywidth = 200
source_dir ='D:\Wallpapers'
destination_dir ='D:\wall'


def resize_pic(old_pic, new_pic, mywidth):
    img = Image.open(old_pic)
    wpercent = (mywidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((mywidth, hsize), PIL.Image.ANTIALIAS)
    img.save(new_pic)


def entire_directory(source_dir, dest_dir, width):
    files = os.listdir(source_dir)
    i = 0

    for file in files:
        i += 1
        old_pic = source_dir + "/" + file
        new_pic = dest_dir + "/" + file
        resize_pic(old_pic, new_pic, width)
        print(i, "done")


entire_directory(source_dir, destination_dir, mywidth)
