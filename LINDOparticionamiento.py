import numpy as np
from random import randint

costo = True
costoMin = 1
costoMax = 10
cantidadDeZonas = int(input("Zonas: "))

zonas = ["z" + str(x) for x in range(cantidadDeZonas)]
print("Las zonas son", zonas)

cantidadDeAntenas = randint(1, cantidadDeZonas-1)
print("La cantidad de antenas randomizadas son", cantidadDeAntenas)

antenas = {}
for i in range(cantidadDeAntenas):
    colidantes = randint(1, (cantidadDeZonas-1) // 2)
    zonaAntena = np.random.choice(zonas, size=colidantes, replace=False)
    antenas[i] = (tuple(zonaAntena))

print("Antenas: ", antenas)
zonasSinAntena = []

restr = []
for zona in zonas:
    antenasZona = []
    for antena in antenas:
        if zona in antenas[antena]:
            antenasZona.append(antena)
    if len(antenasZona) == 0:
        print("La zona", zona, "no tiene antenas :c")
        "a" + 2
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
    print(a)
    constraints += a + "\n"

fin = open("modelo_LINDO.ltx","w")

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

fin = open("modelo_MZ.mzn", "w")

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