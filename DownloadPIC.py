import  InstaBot.BOT
import requests
from PIL import Image
import os, sys
from InstaBot import Resixe
path = "/Users\Real fadil\Desktop\MEMES/"


x = InstaBot.BOT.GetPicLink( )
m=0
for i in (x):

    r = requests.get(x[m])
    with open("/Users\Real fadil\Desktop\MEMES/py" + str(m) +".png", 'wb') as f:
        f.write(r.content)
    m = m+1
print("here")
dirs = os.listdir( path )
for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)

            imResize = im.resize((500,500), Image.ANTIALIAS)
            imResize.save(f + 'x.png', 'png', quality=90)

print("here")