import numpy as np
from random import randint

cantidadDeZonas = int(input("Zonas: "))

zonas = ["z" + str(x) for x in range(cantidadDeZonas)]
print("Las zonas son", zonas)

cantidadDeAntenas = randint(0, cantidadDeZonas-1)
print("La cantidad de antenas randomizadas son", cantidadDeAntenas)

antenas = {}
for i in range(cantidadDeAntenas):
    colidantes = randint(1, (cantidadDeZonas-1) // 2)
    zonaAntena = np.random.choice(zonas, size=colidantes, replace=False)
    antenas[i] = (tuple(zonaAntena))

print("Antenas:", antenas)

restr = []
for zona in zonas:
    antenasZona = []
    for antena in antenas:
        if zona in antenas[antena]:
            antenasZona.append(antena)
    if len(antenasZona) == 0:
        print("La zona", zona, "no tiene antenas :c")
    restr.append(antenasZona)

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
        buf += "= 1"
        out.append(buf)

for a in out:
    print(a)