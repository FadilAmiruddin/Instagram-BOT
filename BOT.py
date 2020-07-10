import re
import requests
from bs4 import BeautifulSoup

def GetPicLink():



    response = requests.get('https://ifunny.co/')

    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    #print (img_tags[2])
    makeitastring = ''.join(map(str, img_tags))
    n = makeitastring.split("src=")

    x =0
    m = []
    for i in n:
        if i.__len__() == 102:
            m.append(i)
   # print(i.__len__())
  #  print("____")
   # print(i)
    #x = x+1

    for i in m:
        if i.__contains__("3.jpg"):
           m.remove(i)

    j=0

    q = []
    for i in m:
     q.append(i[1:100])

    #print(q)
    return q
