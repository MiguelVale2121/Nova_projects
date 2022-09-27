import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def getio (year):
    path = 'C:/Users/User/Downloads/bb21a10summarytables.xlsx'
    # Input output table
    df = pd.read_excel(path,
                            sheet_name = str(year),
                            usecols = "C:L",
                            header = None,
                            skiprows = 52,
                            nrows = 10)
    z = np.array(df,dtype = float) # £ million

    # Output per sector
    dfx = pd.read_excel(path,
                            sheet_name = str(year),
                            usecols = "C:L",
                            header = None,
                            skiprows = 75,
                            nrows = 1)
    x = np.array(dfx, dtype = float)[0] # £ million
    return [z, x]
    # Example: Get input-output data for 2000
    # z, x = getio(2000)
#a)

def outlist ():
    i = 1999
    lista=[]
    while i <= 2019:
        z,x=getio(i)
        soma = sum(x)
        lista.append(soma)
        i = i+1
    return lista

def growth(year):
    if year == 1997:
        return 0
    else:
        z1,x1=getio(year)
        z2,x2=getio(year-1)
        somaatual = sum(x1)
        somaanterior = sum(x2)
        return ((somaatual-somaanterior)/somaanterior)*100

def growthlist ():
    i = 2000
    lista=[]
    while i<=2019:
        taxa = growth(i)
        lista.append(taxa)
        i = i + 1
    return lista
growthlist = growthlist()

def conclusao1 ():
    range1 = 2009-2000
    range2 = 2019-2009
    growthlistI = []
    growthlistII = []
    for i in range(9):
        growthlistI.append(growthlist[i])

    for j in range(10,20):
        growthlistII.append(growthlist[j])
    mediaI = sum(growthlistI)/range1
    mediaII = sum(growthlistII)/range2

    if abs(mediaI - mediaII) < 0.000001: # se forem aproximadamente iguais
        return True
    else:
        return str(False) + " " + "->" + " " + "As taxas de crescimento após e antes da " \
                       "recessão não são aproximadamente iguais"

#b)
def leon(year):
    z,x = getio(year)
    coef_tec = z/x
    dim = coef_tec.shape
    identidade = np.identity(dim[0])
    return np.linalg.inv(identidade - coef_tec)

def leons ():
    i = 2000
    lista = []
    while i <= 2019:
        mat_inv = leon(i)
        lista.append(mat_inv)
        i = i + 1
    return lista
leons = leons()

#c)

def bindex(year):
    leon = leons[year - 2000]
    dim = leon.shape
    n = dim[0]
    matrizunsC = np.ones((dim[0],1))
    matrizunsCT = matrizunsC.transpose()
    n_matrizT = np.multiply(n,matrizunsCT)
    n_matrizT_leon = np.dot(n_matrizT,leon)
    matrizT_leon = np.dot(matrizunsCT,leon)
    matrizT_leon_matriz = np.dot(matrizT_leon,matrizunsC)
    res = n_matrizT_leon/matrizT_leon_matriz
    return res.flatten().tolist()


def blist(s):
    i = 2000
    lista = []
    index = []
    while i <= 2019:
        index = bindex(i)
        lista.append(index[s])
        i = i + 1
    return lista


#d)
def conclusao2():
    agricultura = blist(0)
    producao = blist(1)
    construcao = blist(2)
    contadorA = 0
    contadorP = 0
    contadorC = 0
    for x in agricultura:
        if x > 1:
            contadorA += 1
    for y in producao:
        if y > 1:
            contadorP += 1
    for z in construcao:
        if z> 1:
            contadorC += 1
    if (len(agricultura) == contadorA) and (len(producao) == contadorP) and (len(construcao) == contadorC) :
        return True
    else:
        if (len(agricultura) == contadorA):
            pass
        elif (len(agricultura) != contadorA):
            print( str(False) + " " + "->" + " " + "O setor da agricultura não está fortemente ligado")
            pass
        elif (len(producao) == contadorP):
            pass
        elif (len(producao) != contadorP):
            print(str(False) + " " + "->" + " " + "O setor da producao não está fortemente ligado")
            pass
        elif (len(construcao) == contadorC):
            pass
        elif (len(construcao) != contadorC):
            print(str(False) + " " + "->" + " " + "O setor da construcao não está fortemente ligado")
            pass
        else:
            return False

def buscarMenor(lista):
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    return menor

def conclusao3():
    lista = []
    for i in range(10):
        index = blist(i)
        somatorio = sum(index)
        media = somatorio/len(index)
        lista.append(media)
    indexMenor = lista.index(buscarMenor(lista))
    if indexMenor == 6:
        return True
    else:
        return str(False) + " " + "->" + " " + "O setor imobiliario não é o mais fracamente ligado"