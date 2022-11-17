import dados

opcion=1
while opcion != 0:
    op=input("\n¿Cuantas caras quiere que tenga el dado?\n(0)Salir\n")

    if op.isdigit():

        if opcion==0:
            print("Hasta la próximaaa")
        opcion=int(op)
        dados.dados_tirar(opcion)   

    else:
        print("Poner números.")