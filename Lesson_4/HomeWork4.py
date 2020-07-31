f = open("countries.txt") 
Count = 0
Content = f.read() 
CoList = Content.split("\n")
#print (CoList)
import random
RC1 = random.choice(CoList)
a=RC1.split(",")
print("Care este capitala la ", a[0], "?")
print('Variante de raspuns','1 CANBERRA','2 BRIDGETOWN','3',a[1],'4 YAOUNDE')
b = input()
if b.isdigit() :
    b = int(b) 
    if b == 3 :
        print ("Corect")
    else :
        print ("Gresit Capitala  ", a[0], "este", a[1])
