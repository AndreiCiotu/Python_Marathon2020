print ("determinarea extensiei .py")
a= input("Introdu numele fisierului: ")
a = a.split(".")

if (a[-1]) == 'py':
    print ("true")
elif len(a)==2:
     print ("Extensia fisiereului este ", a[-1])
else :
    print("i dont have an extension")


