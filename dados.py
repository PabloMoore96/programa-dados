import random
def dados_tirar(n_caras):
    cant=input("Ingresar la cantidad de dados a tirar:\n")

    while not cant.isnumeric():
        cant=input("Ingresar la cantidad de dados a tirar (ingresar números):\n")
    cant=int(cant)
    for i in range(cant):
        dado=random.randint(1, n_caras)
        print (f"El dado {i+1} sacó: {dado}")
