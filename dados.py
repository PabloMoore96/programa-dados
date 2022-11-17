import random

# --------------------------------------------------------------------------------D3--------------------------------------------------------------------------
def dadod3():

    cant=input("Ingresar la cantidad de dados d3 a tirar:\n")

    while not cant.isnumeric():
        cant=input("Ingresar la cantidad de dados d3 a tirar (ingresar números):\n")
    
    cant=int(cant)
    for i in range(cant):
        dado= random.randint(1,3)
        print (f"El dado {i+1} sacó: {dado}")
    
    input("Enter para continuar")


# --------------------------------------------------------------------------------D4--------------------------------------------------------------------------
def dadod4():

    cant=input("Ingresar la cantidad de dados d4 a tirar:\n")

    while not cant.isnumeric():
        cant=input("Ingresar la cantidad de dados d4 a tirar (ingresar números):\n")
    
    cant=int(cant)
    for i in range(cant):
        dado= random.randint(1,4)
        print (f"El dado {i+1} sacó: {dado}")
    
    input("Enter para continuar")

# --------------------------------------------------------------------------------D6--------------------------------------------------------------------------
def dadod6():

    cant=input("Ingresar la cantidad de dados d6 a tirar:\n")
    while not cant.isnumeric():
        cant=input("Ingresar la cantidad de dados d6 a tirar (ingresar números):\n")
    
    cant=int(cant)
    for i in range(cant):
        dado= random.randint(1,6)
        print (f"El dado {i+1} sacó: {dado}")
    
    input("Enter para continuar")

# --------------------------------------------------------------------------------D8--------------------------------------------------------------------------
def dadod8():

    cant=input("Ingresar la cantidad de dados d8 a tirar:\n")
    while not cant.isnumeric():
        cant=input("Ingresar la cantidad de dados d8 a tirar (ingresar números):\n")
    
    cant=int(cant)
    for i in range(cant):
        dado= random.randint(1,8)
        print (f"El dado {i+1} sacó: {dado}")
    
    input("Enter para continuar")

# --------------------------------------------------------------------------------D10-------------------------------------------------------------------------
def dadod10():
    cant=input("Ingresar la cantidad de dados d10 a tirar:\n")
    while not cant.isnumeric():
        cant=input("Ingresar la cantidad de dados d10 a tirar (ingresar números):\n")
    
    cant=int(cant)
    for i in range(cant):
        dado= random.randint(1,10)
        print (f"El dado {i+1} sacó: {dado}")
    
    input("Enter para continuar")

# --------------------------------------------------------------------------------D12-------------------------------------------------------------------------
def dadod12():
    cant=input("Ingresar la cantidad de dados d12 a tirar:\n")
    while not cant.isnumeric():
        cant=input("Ingresar la cantidad de dados d12 a tirar (ingresar números):\n")
    
    cant=int(cant)
    for i in range(cant):
        dado= random.randint(1,12)
        print (f"El dado {i+1} sacó: {dado}")
    
    input("Enter para continuar")

# --------------------------------------------------------------------------------D20-------------------------------------------------------------------------
def dadod20():
    cant=input("Ingresar la cantidad de dados d20 a tirar:\n")
    while not cant.isnumeric():
        cant=input("Ingresar la cantidad de dados d20 a tirar (ingresar números):\n")
    
    cant=int(cant)
    for i in range(cant):
        dado= random.randint(1,20)
        print (f"El dado {i+1} sacó: {dado}")
    
    input("Enter para continuar")

# --------------------------------------------------------------------------------D100------------------------------------------------------------------------
def dadod100():
    cant=input("Ingresar la cantidad de dados d100 a tirar:\n")
    while not cant.isnumeric():
        cant=input("Ingresar la cantidad de dados d100 a tirar (ingresar números):\n")
    
    cant=int(cant)
    for i in range(cant):
        dado= random.randint(1,100)
        print (f"El dado {i+1} sacó: {dado}")
    
    input("Enter para continuar")