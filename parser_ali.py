from bs4 import BeautifulSoup
import requests
import re

url = input("Write Url here")

req = requests.get(url)
html = BeautifulSoup(req.content,"html.parser")

def description(html):
    description = str(html.select("title"))
    description = description[8:-101]
    result = "Your description is - " + str(description)
    return result

def url_image():
    url_image = html.select("meta",{"property":"og:image"})
    url_image = (str(url_image[9])).split('"')
    url_image = url_image[1]
    #result = "Your url to image - " + str(url_image)
    return url_image

def price(html):
    price = html.findAll("script")
    price = price[-3]
    price = price.text
    price = price.split()
    price = price[-10]
    result = "Your price is " + str(price)
    return result

print(price(html))
print(description(html))
