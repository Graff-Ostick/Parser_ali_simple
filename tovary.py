list = []
print("Write q to exit")
while True:
    case = input("Write item ")
    if case == "q":
        break
    price = float(input("Input price *"))
    coins = (price*230)*0.6
    cristal = (price*230)*0.4
    print("price in coins = ",coins," price in cristal = ", cristal  )
    item = case +" price * = "+str(price)+ "$ coins = " + str(coins)+ " cristal = " + str(cristal)
    list.append(item)


with open('file.txt', 'w') as filehandle:
    for listitem in list:
        filehandle.write('%s\n' % listitem)
