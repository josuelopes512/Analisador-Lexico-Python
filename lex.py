import re
import pandas as pd
import numpy as np

def arquivo(arq): # Abre Arquivo
    file = open(arq, 'r')
    lista = file.readlines()
    return lista
    
def tratarArq(lista): # trata lista e converte
    tmd = " ".join(lista.split())
    tws = re.split(r' ', tmd)
    return tws

def remComments(lista): #Remove Quaisquer comentarios
    k = []
    ret = ""
    comentario = []
    f = lista
    if(re.search(r'^@(\w*\s?)*$|@(\w*\s?)*$|@(\w*\s?).*', f)):
        list(k)
        k = re.split(r'\@',f)
        for i in k:
            if(re.search(r'[a-zA-Z]',i)):
                k.remove(i)
        return k[0]
    else:
        return lista

def verExp(lista): # verifica se tem alguma letra alfabetica
    teste=[0]
    list(lista)
    if (re.search(r'[a-zA-Z]',lista)):
        raise Exception("Erro: não é aceito caractere")
    else:
    #Remover os os espaços em exceço
        demo = " ".join(lista.split())
        teste =re.split(r' ', demo)
    return lista

# def verExpr(lista): # ler tudo duma só vez, mas iria da erro
#     seq = []
#     for l in range(0, len(lista)):
#         seq.insert(l,verExp(lista[l]))
#     return seq

def transformar(lista):
    listaNova=[]
    for a in lista:
        if(a[0]!='(') and a[-1]!=')':
            listaNova.append(a)
        elif(a[0]=='('):
            listaNova.append(a[0])
            listaNova.append(a[1:])
        elif( a[-1]==')'):
            listaNova.append(a[:-1])
            listaNova.append(a[-1])
    return listaNova

def filtrarTokensNum(listx): # filtra os numeros
    lista = list(listx)
    print()
    x1 = []
    xv = [' '.join(lista)]
    fc = list(xv[0])
    # print("FILTNUM: "+str(fc))
    for i in fc:
        if(re.search(r'[(^\()]', i)):
            fc.remove(i)

    tmp1 = [''.join(fc)]
    tmp2 = tmp1[0]
    tmp3 = " ".join(tmp2.split())
    tmp4 = re.split(r' ', tmp3)

    x1= filter(lambda i: re.search(r'(?i)\d',i,re.I), tmp4)
    numeros= list(x1)
    return numeros

def filtrarParEsq(lista): # filtra os parenteses esquerdo
    x2 = []
    x2t = []
    x_parentEsqu = []

    for te in range(0, len(lista)):
        if(re.search(r'\(',lista[te])):
            x2t.append(lista[te])

    if(x2t == []):
        x2 = filter(lambda i:re.search(r'[(^\()]', i),x2t)
        x_parentEsqu=list(x2)
        return x_parentEsqu
    else:
        x2t2 = list(x2t[0])
        x2 = filter(lambda i:re.search(r'[(^\()]', i),x2t2)
        x_parentEsqu=list(x2)
        return x_parentEsqu

def filtrarParDir(lista): # filtra os parenteses direito
    x3 = []
    x3t = []
    x_parentDir = []

    for te in range(0, len(lista)):
        if(re.search(r'\)',lista[te])):
            x3t.append(lista[te])
    if(x3t == []):
        x3 = filter(lambda i:re.search(r'[(^\)]', i),x3t)
        x_parentDir=list(x3)
        return x_parentDir
    else:
        x3t3 = list(x3t[0])
        x3 = filter(lambda i:re.search(r'[(^\)]', i),x3t3)
        x_parentDir=list(x3)
        return x_parentDir

def filtrarOperadores(lista): # filtra os operadores
    operations = []
    for i in lista:
        if re.findall(r'[- / * + **]',i):
            operations.append(i)
    return operations

def gerarTabelaAddTk(nm, pardir, paresq, op, lst):  # gera assocciacoes para criação da tabela
    tk = []
    #Definindo tipo para operações e parênteses
    table_of_operations = {'*':'Mutiplicacao', '**':'Potenciacao','+':'Soma', '-':'Subtracao', '/': 'Divisao'} 
    table_of_parenthesis={'(':'ParentEsq', ')':'ParentDir'}

    for i in lst:
        if i in op and i not in nm:
            tk.append(table_of_operations[i])
        elif i in paresq:
            tk.append(table_of_parenthesis[i])
        elif i in pardir:
            tk.append(table_of_parenthesis[i])
        else:
            tk.append(i)
    
    return tk

def gerarTabelaTipoTk(nm, pardir, paresq, op, list):  # gera a tabela
    result = []
    z = []
    # list(result)
    lista = list
    # print(lista)
    tipo=[]
    token = gerarTabelaAddTk(nm, pardir, paresq, op, list)
    #Adicionando para tabela tipo
    for i in lista:
        if i in op and i not in nm:
            tipo.append('Operador')
        elif i in paresq:
            tipo.append('Pontuação')
        elif i in pardir:
            tipo.append('Pontuação')    
        else:
            tipo.append('Numero') 

    
    result = zip(lista,tipo,token)
    return result

def rodar(lista):  # executa todos os passos na chamada
    strtexto = lista
    tmp0 = remComments(strtexto) # retira comnetario
    tmp1 = verExp(tmp0) # verifica a expressao
    vectortexto = tratarArq(tmp1) # trata o vetor
    Tlista = transformar(vectortexto) # transforma em vetor em indice por indice

    if(tmp1):
        TKnum = filtrarTokensNum(vectortexto)
        TKparesq = filtrarParEsq(vectortexto)
        TKpardir = filtrarParDir(vectortexto)
        TKop = filtrarOperadores(vectortexto)
        tabela = gerarTabelaTipoTk(TKnum, TKpardir, TKparesq, TKop, Tlista)
    
        return tabela
    else:
        raise Exception("ERRO !!!")

def exemplo0(arq):
    g = str(arq[0])
    tabela = rodar(g)
    d = list(tabela)
    print("Lexema,  Tipo,  Valor")
    for i in d:
        print(i)
    print(" ")
    print(" ")


def exemplo1(arq):
    g = str(arq[1])
    tabela = rodar(g)
    d = list(tabela)
    print("Lexema,  Tipo,  Valor")
    for i in d:
        print(i)
    print(" ")
    print(" ")

def exemplo2(arq):
    g = str(arq[2])
    tabela = rodar(g)
    d = list(tabela)
    print("Lexema,  Tipo,  Valor")
    for i in d:
        print(i)
    print(" ")
    print(" ")

def exemplo3(arq):
    g = str(arq[3])
    tabela = rodar(g)
    d = list(tabela)
    print("Lexema,  Tipo,  Valor")
    for i in d:
        print(i)
    print(" ")
    print(" ")

def main():
    arq = arquivo('input.txt')
    #linhas Comentadas
    # exemplo0(arq)
    # exemplo1(arq)

    #linhas com instruções
    exemplo2(arq)
    exemplo3(arq)


main()
