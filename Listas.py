def imprimir(LiDes,LiOrd):
    print("\nLista desordenada:")
    for x in range(len(LiDes)):
        print(LiDes[x])
    print("\nLista ordenada:")
    for i in range(len(LiOrd)):
        print(LiOrd[i])

listaDesordenada = [17,5,9,7,1,10,13]
listaOrdenada = listaDesordenada.copy() #Menor a mayor

r = input("Formas de ordenar \n(1)Mayor a menor\n(2)Menor a mayor\n")

if r=="1":
    listaOrdenada.sort(reverse=True)
    imprimir(listaDesordenada,listaOrdenada)
elif r=="2":
    listaOrdenada.sort()
    imprimir(listaDesordenada,listaOrdenada)
else:
    print("ingrese un valor valido")
    
    


