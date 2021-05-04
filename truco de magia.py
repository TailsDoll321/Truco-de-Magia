import random as rd

mesa_cartas = dict()
cambio_mesa=dict()
fila = None
it=0

cartas = {1: "♠A", 2 : "♠2", 3: "♠3", 4: "♠4", 5: "♠5", 6: "♠6", 7: "♠7", 8: "♠8", 9: "♠9",10: "♠10", 11: "♠J", 12: "♠Q", 13: "♠K",
          14: "♥A", 15 : "♥2", 16: "♥3", 17: "♥4", 18: "♥5", 19: "♥6", 20: "♥7", 21: "♥8", 22: "♥9", 23: "♥10", 24: "♥J", 25: "♥Q", 26: "♥K",
           27: "♦A", 28 : "♦2", 29: "♦3", 30: "♦4", 31: "♦5", 32: "♦6", 33: "♦7", 34: "♦8", 35: "♦9", 36: "♦10", 37: "♦J", 38: "♦Q", 39: "♦K",
           40: "♣A", 41 : "♣2", 42: "♣3", 43: "♣4", 44: "♣5", 45: "♣6", 46: "♣7", 47: "♣8", 48: "♣9", 49: "♣10", 50: "♣J", 51: "♣Q", 52: "♣K"}

mesanum = len(mesa_cartas)

while mesanum!=21:

    x = rd.randint(1,52)
    mesa_cartas[x] = cartas[x]
    mesanum= len(mesa_cartas)
    #print(mesanum)

def p_mesa():
    global mesa_cartas
    
    n=1
    res = n%3
    for k in mesa_cartas:
        res = n%3
        if res==1:
            print("\t",mesa_cartas[k],"\t",end=" ")
        else:
            print(mesa_cartas[k],"\t",end=" ")
        n+=1
        if res ==0:
            print("\n")
    print("\t 1 \t 2 \t 3")
    print("Escoja mentalmente una de las <<cartas>> del <<tablero>> y diga en que columna se encuentra")
p_mesa()

def fnum():
    global fila
    fila=0
    while fila==None or fila<=0 or fila>=4:
        try:
            fila=int(input("Mi carta esta en la fila:  "))
            if fila<=0 or fila>=4:
                print("\nTiene que ser un numero entero, entre el 1 y el 3\n")
        except:
            print("\nTiene que ser un numero entero, entre el 1 y el 3\n")
    return fila
fnum()

def nuevamesa(num):

    global cambio_mesa, mesa_cartas,it
    n=1
    fila1=dict()
    fila2=dict()
    fila3=dict()
    
    for k in mesa_cartas:
        res=n%3
        if res==1:
            fila1[k]=mesa_cartas[k]
        if res==2:
            fila2[k]=mesa_cartas[k]
        if res==0:
            fila3[k]=mesa_cartas[k]
        n+=1
    if num==1:
        fila2.update(fila1)
        fila2.update(fila3)
        cambio_mesa=fila2
    else:
        if num==2:
            fila1.update(fila2)
            fila1.update(fila3)
            cambio_mesa=fila1
        else:
            fila1.update(fila3)
            fila1.update(fila2)
            cambio_mesa=fila1

    it+=1
    #print(fila1)
    return cambio_mesa,it

nuevamesa(fila)
mesa_cartas=cambio_mesa
#cambio_mesa.clear()
p_mesa()
fnum()

nuevamesa(fila)
mesa_cartas=cambio_mesa
#cambio_mesa.clear()
p_mesa()
fnum()

nuevamesa(fila)
mesa_cartas=cambio_mesa
#cambio_mesa.clear()
p_mesa()

pre = mesa_cartas.values()
pre=list(pre)
truco = pre[10]
print("\nLa carta que escogio es ", truco)
