#!/usr/bin/env python
# coding: utf-8

# <hr>
# <br>
# <h1> IMLEMENTAÇÃO DO ALGORITMO ID3 - DISCIPLNA IA 2021.1 UNI7</h1>
# 
# <h5>Prof: Alexandre    Equipe: Alessandra Santos, Jefferson Moraes e Livia Chaves</h5>
# 
# <br>
# <hr>
# 

# <hr>
# <br>
# 
# ### Importando as bibliotecas
# 
# <br>
# <hr>

# In[1]:


import pandas as pd
import numpy as np
import math
from decimal import Decimal


# <hr>
# <br>
# 
# ### Buscando os valores da classe ou da propriedade
# 
# <br>
# <hr>

# In[2]:


def getKeys(data, val):
    
    # Busca todos os dados da coluna informada na tabela
    
    values = data[val]
    
    
    keys = list()
        
    # filtra os valores da classe ou propriedade
    
    for x in values:
        
        if x not in keys:
        
            keys.append(x)
    
    return keys
    
    


# <hr>
# <br>
# 
# ### Calculando a entropia do conjunto corrente (CE)
# 
# <br>
# <hr>

# In[3]:


def getEntropyOfClass(data,classe):
    
    print('Calculando a entropia da conjunto corrente CE')
    
    # Pega os valores da classe
    
    keys = getKeys(data, classe)
    
  
    
    logs = list()
    
    
    ## Calcula pi * log2(pi) para cada valor da classe
    
    for key in keys:
        
        
        
        is_key =  data[classe]==key
       
        data_key = data[is_key]
    
        print('P(',key,') =', len(data_key),'/', len(data))
        
        p = (len(data_key)/len(data))
            
        log = p * math.log2(p)
        
        logs.append(log)
    
    # Calcula o somatório de pi * log2(pi) dos valores da classe (Entropia)
    
    entropy = 0
    
    for log in logs:
        
        entropy = entropy - log
    
    return entropy
        
    


# <hr>
# <br>
# 
# ### Calculando a entropia de cada propriedade
# 
# 
# <br>
# <hr>

# In[4]:


def getEntropyOfProperty(data, classe, prop):
    
    # Valores da propiedade Ex : Divida : {Alta, Baixa}
    
    keysProp = getKeys(data, prop)
    
    # Valores da classe  Ex : Risco : {Alto, Baixo, Moderado}
    
    keysClasse = getKeys(data, classe)
    
    entropies = list()
    
    freqProp = list()
    
    
    for keyP in keysProp:
        
        
        # Retorna resultados booleano de cada linha da tabela se ela contém o valor corrente ( C1)
        
        isKeyP = data[prop] == keyP
        
        # Busca as linha da tabela que contém o valor corrente (Conjunto C1 {1,2,3})
        
        dataKey = data[isKeyP]
        
        # Contém as o número de vezes que cada valor aparece na tabela
        
        freqProp.append(len(dataKey))
        
        logs = list()
        
        
        # Iterando sobre os valores da classe
        
        for y in keysClasse:
            
            
            # Verifica quais linha da tabela retornada (C1), quais contém o valor da classe corrente (True or False).
            
            isClass = dataKey[classe] == y
        
            
            # Busca as linhas da tabela retornada (C1) , quais contém o valor da classe corrente.
            
            dataClass =  dataKey[isClass] 
           
            # Calcula a frequência do valor na tabela retornada EX:  P(Class = Alta/ C1) = 4/7
        
            p = len(dataClass)/len(dataKey)
        
            # Calcuaa o valore de p * logaritimo base de p
            
            if p != 0:
                log = p * math.log2(p)
                logs.append(log)
            else:
                logs.append(p)
        
        # Realiza o somátorio da valores obitidos para encontra a entropia do valor da classe no conjunto C1
        
        entropy = logs[0] *-1
        
        for i in range(1,len(logs)):
            
            
            entropy = entropy - logs[i]
        
        # Lista das entropias de cada valor da propriedade
        entropies.append(entropy)
    
    entropyProp = 0 
    
    entropVsFreq = list()
    
    # 1 - Realiza a mutiplação das entropias dos valores da propriedade pela a sua frequência     
    # 2 - Somatorioa das mutiplicações para encontras a entropia da propriedade
    
    for i in range(len(entropies)):
        
        v = entropies[i] * (freqProp[i]/len(data))
        entropyProp = entropyProp+v
    return entropyProp


# In[5]:


# Calcla do ganho de cada propriedade
def getProfit(CE, Prop):
    
    return CE - Prop

# Busca qual propriedade tem o melhor ganho

def getBestProfit(CE,Props):
    
    profits = list()
    
    for prop in Props:
        profit =getProfit(CE, prop[0])
        profits.append((prop[1],profit))

    return (max(profits))


# In[6]:


def selection():

    # Dados da tabela
    
    data = pd.read_csv('Risco.csv',sep=';')
    

    print(data.head(5))
    
    # Chamada das funções de cálculo de entropia
    
  
    entropyCE = getEntropyOfClass(data,'Risco')
    
    entropyDI = getEntropyOfProperty(data, 'Risco', 'DI')
    
    entropyHC = getEntropyOfProperty(data, 'Risco', 'HC')
    
    entropyGA = getEntropyOfProperty(data, 'Risco', 'GA')
    
    entropyRND = getEntropyOfProperty(data, 'Risco', 'RND')
    
    props = [(entropyDI,'DI'),(entropyHC,'HC'),(entropyGA,'GA'),(entropyRND,'RND')]
    
    
    print('Entropia do conjunto CE:', entropyCE)
    
    print('Entropia da propriedade DI:', entropyDI)
    
    
    print('Entropia da propriedade GA:', entropyGA)
    
    print('Entropia da propriedade HC:', entropyHC)
    
    
    print('Entropia da propriedade RND:', entropyRND)
    
    
    
    getBestProfit(entropyCE,props)
    
    


# In[7]:


selection()


# In[ ]:





# In[ ]:




