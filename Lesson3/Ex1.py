def convert():
    z = int(input('Selectati actiunea dorita: '))
    if z == 1:
        c = float(input('Introduceti valoarea in grade Celsius: '))
        f = (((9/5)*c)+32)
        print(f)
    elif z == 2:
        f = float(input('Introduceti valoarea in grade Fahrenheit: '))
        c = (((f-32)*5)/9)
        print(c)


print(
    'Acest program :' '\n'
    '1 - Converteaza grade Celsius in Fahrenheit' '\n'
    '2 - Converteaza grade Fahrenheit in Celsius' '\n'
)

convert()
while True:
    flag = input('Repetati? [y/n]: ')

    if flag == 'y':
        convert()
    else:
        break