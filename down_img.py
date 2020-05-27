import random
import urllib.request
import parser_ali

names = [""]

def download_img(url):
    name = "images/" + str(random.randint(1,100))
    name+=".jpg"

    for i in range(len(names)):
        if i == name:
            name[0]+="2"
            names.append(name)
        else:
            names.append(name)

    urllib.request.urlretrieve(url,name)

try:
    download_img(parser_ali.url_image())
    print(f"Image {names[-1]} has downloaded ")
except Exception as e:
    print("Error, write another url \n",str(e))
