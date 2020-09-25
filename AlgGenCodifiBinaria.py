import random

def poblacion_inicial(max_poblacion, cant_gen):
    poblacion=[]
    for i in range(max_poblacion):
        gen=[]
        for j in range(cant_gen):
            if random.random() > 0.5:
                gen.append(1)
            else:
                gen.append(0)
        poblacion.append(gen[:])
    return poblacion

def printPopulation(matriz):
    for i in range(len(matriz)):
        print(i+1,")",formarBinario(matriz[i]))
        
def printAptitud(matriz):
    for i in range(len(matriz)):
        print(i+1,")",formarBinario(matriz[i]),BaseToDec(formarBinario(matriz[i]),2),aptitudF(BaseToDec(formarBinario(matriz[i]),2)))

def BaseToDec(num,b):
    sum = 0
    arr = list(num)
    j = len(num)
    for i in range(len(num)):
        j-=1
        sum += (b**i)*nomenclatura(arr[j])
                
    return sum

def nomenclatura(v):
    valor = 0
    v=v.lower()
    if v == 'a':
        valor = 10
    elif v == 'b':
        valor = 11
    elif v == 'c':
        valor = 12
    elif v == 'd':
        valor = 13
    elif v == 'e':
        valor = 14
    elif v == 'f':
        valor = 15
    else:
        valor = v

    return int(valor)

#print(BaseToDec("1110", 2))

def aptitudF(x):
    return x**2 - 250*x - 25

def formarBinario(arr):
    cad=""
    for i in range(len(arr)):
        cad+=str(arr[i])
    return cad
   
def algoritmo_genetico():
    max_iter=500
    fin=False
    individuos=10#debe ser par
    genes=9
    probCruz=0.7
    cruzPun=5
    probMut=0.05
    poblacion=poblacion_inicial(individuos,genes)
    iteraciones=0

    print("Parámetros:")
    print("- Cantidad de Individuos:",individuos)
    print("- Cantidad de Genes por Individuo:",genes)
    print("- Selección por torneo (2)")
    print("- Probabilidad de Cruzamiento:",probCruz)
    print("- Cruzamiento de un Punto (Punto ",cruzPun,")")
    print("- Probabilidad de Mutación:",probMut)
    print("- Mutación Bit Flip")
    print("- Cantidad de Iteraciones:",max_iter)

    print("")
    
    print("Población Inicial")
    printPopulation(poblacion)
    print("")
    #creación de Mating Pool o cálcular el fitness
    print("Calcular la Aptitud para cada Individuo")
    printAptitud(poblacion)
    while not fin:
        iteraciones=iteraciones+1
        aux=[]
        
        print("")
        print("**** Iteracción ",iteraciones,"****")
        print("Creación de Mating Pool")
        for i in range(individuos):
            
            opc1=random.randrange(0,individuos)
            opc2=random.randrange(0,individuos)
            while opc2 == opc1:
                opc2=random.randrange(0,individuos)
            
            if aptitudF(BaseToDec(formarBinario(poblacion[opc1]),2)) >= aptitudF(BaseToDec(formarBinario(poblacion[opc2]),2)):
                print(i+1,")",opc1+1,"-",opc2+1," => ",opc2+1," => ",formarBinario(poblacion[opc2]))
                aux.append(poblacion[opc2])
            else:
                print(i+1,")",opc1+1,"-",opc2+1," => ",opc1+1," => ",formarBinario(poblacion[opc1]))
                aux.append(poblacion[opc1])

        #Selección de padres
        
        poblacion=[]
        for i in range(individuos//2):
            print("")
            print(i+1,") Selección de padres")
            print("------------------------")
            opc1=random.randrange(0,individuos)#papa
            opc2=random.randrange(0,individuos)#mama
            while opc2 == opc1:
                opc2=random.randrange(0,individuos)

            print(opc1+1,"-",opc2+1," => ",formarBinario(aux[opc1]),"-",formarBinario(aux[opc2]))
                
            hijo1=[]
            hijo2=[]
            print("Cruzamiento")
            if random.random() <= probCruz:
                print("Cruzamiento")
                #cruzamiento
                for j in range(genes):
                    if j<cruzPun:
                        hijo1.append(aux[opc1][j])
                    else:
                        hijo1.append(aux[opc2][j])
                        
                for j in range(genes):
                    if j<cruzPun:
                        hijo2.append(aux[opc2][j])
                    else:
                        hijo2.append(aux[opc1][j])
            else:
                print("Sin cruzamiento")
                hijo1=aux[opc1]
                hijo2=aux[opc2]

            print(formarBinario(hijo1),"-",formarBinario(hijo2))
            #mutación hijo1
            if random.random() <= probMut:
                posicion=random.randrange(0,genes)
                if hijo1[posicion]==1:
                    hijo1[posicion]=0
                else:
                    hijo1[posicion]=1

                print("Mutación 1")
                print("Posición:",posicion,"=>",formarBinario(hijo1))
            else:
                print("Sin mutación 1")

            #mutación hijo2
            if random.random() <= probMut:
                posicion=random.randrange(0,genes)
                if hijo2[posicion]==1:
                    hijo2[posicion]=0
                else:
                    hijo2[posicion]=1

                print("Mutación 2")
                print("Posición:",posicion,"=>",formarBinario(hijo2))
            else:
                print("Sin mutación 2")
                
            #Agregar a la nueve generaciòn a la población
            poblacion.append(hijo1[:])
            poblacion.append(hijo2[:])

        print("")
        print("Nueva Población")
        printPopulation(poblacion)
        print("")
        print("Calcular el Fitness")
        printAptitud(poblacion)

        if max_iter < iteraciones:
            fin = True

algoritmo_genetico()
