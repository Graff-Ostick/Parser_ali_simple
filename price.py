import parser_ali

html = parser_ali.html

def all_number(html):
    price = html.findAll("script")
    price =price[-3]
    price = price.text
    return(price)

text=all_number(html)
list = []

def rec(i):
    if text[i].isnumeric() or text[i]==' ' or text[i]==',' or text[i]=='.':
        result = text[i] + rec(i+1)
    else:
        result = ''
    return result


i = 0
while i<len(text):
    if text[i].isnumeric():
        list.append(rec(i))
        i+=len(rec(i))
    i+=1
print(list)
