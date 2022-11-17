import dados


if __name__=="__main__":
    opcion=0
    while opcion != 9:
        op=input("\n¿Qué dado desea tirar?\n(1) Dado de 3 caras\n(2) Dado de 4 caras\n(3) Dado de 6 caras\n(4) Dado de 8 caras\n(5) Dado de 10 caras\n(6) Dado de 12 caras\n(7) Dado de 20 caras\n(8) Dado de 100 caras\n(9) Salir\n")

        if op.isdigit():

            opcion=int(op)
            if opcion==1:
                dados.dadod3()
            elif opcion==2:
                dados.dadod4()
            elif opcion==3:
                dados.dadod6()
            elif opcion==4:
                dados.dadod8()
            elif opcion==5:
                dados.dadod10()
            elif opcion==6:
                dados.dadod12()
            elif opcion==7:
                dados.dadod20()
            elif opcion==8:
                dados.dadod100()
            elif opcion==9:
                print("Hasta la próximaaa")
            else:
                print("Opción inválida.")

        else:
            print("Poner números.")