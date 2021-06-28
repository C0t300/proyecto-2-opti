import numpy as np
from random import randint
import os, shutil

def main(cantidadDeZonas = 10, nRun = 0, prints=False):
    costo = True
    costoMin = 1
    costoMax = 10

    zonas = ["z" + str(x) for x in range(cantidadDeZonas)]
    if prints:
        print("Las zonas son", zonas)

    cantidadDeAntenas = randint(1, cantidadDeZonas-1)
    if prints:
        print("La cantidad de antenas randomizadas son", cantidadDeAntenas)

    antenas = {}
    for i in range(cantidadDeAntenas):
        colidantes = randint(1, (cantidadDeZonas-1) // 2)
        zonaAntena = np.random.choice(zonas, size=colidantes, replace=False)
        antenas[i] = (tuple(zonaAntena))

    if prints:
        print("Antenas: ", antenas)
    zonasSinAntena = []

    restr = []
    for zona in zonas:
        antenasZona = []
        for antena in antenas:
            if zona in antenas[antena]:
                antenasZona.append(antena)
        if len(antenasZona) == 0:
            if prints:
                print("La zona", zona, "no tiene antenas :c")
            return False
            zonasSinAntena.append(zona)
        restr.append(antenasZona)

    # problemaSinAntenas = True
    # if problemaSinAntenas:
    #     while(len(zonasSinAntena) > 0):
    #         nuevaAntena = max(antenas) + 1 #int?
    #         newZonasAntena = np.random.choice(zonasSinAntena, size=randint(1, len(zonasSinAntena)), replace=False)
    #         for new in newZonasAntena:
    #             zonasSinAntena.remove(new)
    #         antenas[nuevaAntena] = (tuple(newZonasAntena))

    # print("esto es restr")
    # print(restr)
    # print("ya se acabo restr")
    # print(cantidadDeZonas, len(restr))
    if prints:
        print("output:")
    out = []
    for r in restr:
        buf = ""
        for i in r:
            buf += "x" + str(i) + " + "
        buf = buf[:-2] 
        if buf != "":
            buf += ">= 1"
            out.append(buf)


    constraints = ""
    for a in out:
        if prints:
            print(a)
        constraints += a + "\n"

    fin = open("modelo_LINDO" + str(nRun) + ".ltx","w")

    costos = {}
    objective_function = "Min "
    for a in antenas:
        if costo:
            costo = randint(costoMin, costoMax)
            costos[a] = costo
            objective_function += str(costo) + "x" + str(a) + " + "
        objective_function += "x" + str(a) + " + "

    objective_function = objective_function[:-2]


    fin.write(objective_function)
    fin.write("\n")
    fin.write("st")
    fin.write("\n")
    fin.write(constraints)

    fin.close()

    fin = open("modelo_MZ" + str(nRun) + ".mzn", "w")

    fin.write("var int: utilidad;\n")
    for a in antenas:
        fin.write("var bool: x" + str(a) + ";\n")

    for a in out:
        fin.write("constraint ")
        fin.write(a)
        fin.write(";\n")

    utilidad = "constraint utilidad = "
    for a in antenas:
        if costo:
            utilidad += "x" + str(a) + "*" + str(costos[a]) + " + "
        else:
            utilidad += "x" + str(a) + " + "
        
    utilidad = utilidad[:-2]
    fin.write(utilidad)
    fin.write(";\n")
    fin.write("solve minimize utilidad;\n")
    fin.close()
    return True


try:
    os.mkdir("solve")
except:
    folder = 'solve'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                #print("deleted", file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
os.chdir("solve")
runs = 100
sinSolucion = 0
for i in range(runs):
    cantidadDeZonas = randint(10, 20)
    solucion = main(cantidadDeZonas, i)
    if not solucion:
        sinSolucion += 1
conSolucion = runs-sinSolucion

print("El programa se corrió", runs, "veces")
print("de las cuales,", conSolucion, "tuvieron solucion")
print("y", sinSolucion, "no tuvieron solucion.")