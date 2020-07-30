print ("Ex_1")
print ("Alegeti unitatea de baza 1-Celsius sau 2-Fahrenheit")
a = input("Unitatea:")
if a.isdigit() :
    a = int(a) 
    if a == 1 or a==2 :
        print ("Introduceti valoarea in grade")
        b = input ("Temperatura:")   
        if b.isdigit(): 
            b = int(b)
            if a == 1 :
                print ("Temperatura in grade Fahrenheit",(((9/5)*b)+32),"F")
            elif a == 2 :
                print ("Temperatura in grade Celsius",(((b-32)*5)/9) ,"C")
        else :
            print("valoarea este intorudsa gresit")
    else :
        print ("valoarea este intorudsa gresit ")
else :
    print ("valoarea este intorudsa gresit")


print ("Ex_2")
print ("check palindrom")
s = input()
def palindrome(s):
    rev = ''.join(reversed(s))
    if (s==rev):
        return True
    else : 
        return False
    
ans = palindrome(s)  
  
if (ans): 
    print("Cuvantul este palindrom") 
else: 
    print("Cuvantul nu este palindrom") 


print ("Ex_3")
print("Dati numarul pentru care se va afisa divizorii:")
n=input()
n=int(n)
print("Divizorii numarului ",n," sunt:")
for i in range(1,n,1):
    if n % i==0:
        print(i)
print(n)

print ("Ex_4")
n=0
for i in range(1000,2300,1):
    if ((i % 5==0) and (i % 7==0)):
        n=n+i
print(n)

print ("Ex_5")
string= input("introduceti textul: ")
countnum=0
countlit=0
a = string.split()
for i in a:
    if(i.isdigit()):
        countnum=countnum+1
    countlit=countlit+1
print ("numarul de cifree ste:")
print (countnum)
print ("Numarul de cuvinte este: ")
print (countlit-countnum)