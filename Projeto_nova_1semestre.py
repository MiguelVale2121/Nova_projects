
import pandas as pd
import numpy as np

from numpy import array
from numpy import linalg
from numpy.linalg import matrix_power

path = '/Users/User/Desktop/projeto_Tiago/bb21a10summarytables.xlsx'
# Input output table
df = pd.read_excel(path,sheet_name = 22, usecols = "C:L", header = None, skiprows = 52, nrows = 10)
z = np.array(df,dtype = float) # £ million
# Output por sector
dfx = pd.read_excel(path, sheet_name = 22, usecols = "C:L", header = None, skiprows = 75, nrows = 1)
x = np.array(dfx, dtype = float)[0] # £ million


pathe = '/Users/User/Desktop/projeto_Tiago/ghgintensity_uk.xlsx'
dfem = pd.read_excel(pathe, sheet_name = 0, usecols = "B:X", skiprows = 1, header = None, nrows = 10)
E = np.array(dfem, dtype = float) #Thousand tonnes CO2 /£ million

#a)
def coef_mat(z,x):
    return z/x

#b)

def leon(a, dif=1e-6):
    dim = a.shape
    identity = np.identity(dim[0])
    first = identity
    m = 1
    while(1):
        A = matrix_power(a,m)
        A1 = matrix_power(a,m+1)
        submat = abs(A1- A)
        first = first + A
        maior = np.argmax(submat)
        if (maior < dif):
            return first
        m = 1 + m

def impact_output(a):
    matrizLeon = leon(a)
    soma = np.sum(matrizLeon, axis=0)
    return soma

def maximp(a):
    max = impact_output(a)
    return  "Sector " + str(np.argmax(max) + 1)

#c)
def impact_ghg(a, ghg):
    impacto = list()
    for i in range(len(leon(a))):
        valores = 0
        for j in range(len(leon(a))):
            elementosM= leon(a)[j][i]
            valores = (elementosM / 1000 * ghg[j]) + valores
        impacto = impacto + [valores]
    return impacto


#d)
def wellbeing(a,ghg,p = 50):
    return impact_output(a) - (impact_ghg(a,ghg) * array([p]))


def maxwell(a, ghg, p = 50):
    return "Sector " + str(np.argmax(wellbeing(a,ghg,p)) + 1)

def price_range(a , ghg):
    i=0
    while i < 210:
        if maxwell(a, ghg, i) == maxwell(a, ghg):
            intervalo = list(range(i))
        i+=1
    return [intervalo[0], intervalo[-1]]


