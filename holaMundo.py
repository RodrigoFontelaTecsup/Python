print("Hola mundo")
on = True
while(on == True):
    a = int(input("Ingresa un valor: "))
    b = int(input("Ingresa un valor: "))
    if a > b:
        print(a,"es mayor que",b)
    elif b > a:
        print(b,"es mayor que",a)
    else:
        print(a,"es igual que",b)
        on = False
print("Fin")