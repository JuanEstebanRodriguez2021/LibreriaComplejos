import math 

def sumacomplex (x,y):
    real = x[0] + y[0]
    imaginario = x[1] + y[1]
    return (real,imaginario)

def restacomplex (x,y):
    real = x[0] - y[0]
    imaginario = x[1] - y[1]
    return (real,imaginario)

def productocomplex (x,y):
    real = (x[0] * y[0]) - (x[1] * y[1])
    imaginario = (x[0] * y[1]) + (x[1] * y[0])
    return (real,imaginario)

def divisioncomplex (x,y):
    divisor = y[0]**2 + y[1]**2
    real = (x[0] * y[0] + x[1] * y[1]) / divisor
    imaginario = (x[1] * y[0] - x[0] * y[1]) / divisor
    return (real, imaginario)

def modulocomplex(z): 
    mod= math.sqrt(z[0]**2 + z[1]**2)
    return mod 

def conjugadocomplex(z): 
    conjugado = (z[0], -z[1])
    return conjugado

def cartesianoa_polarcomplex(z):
    magnitud = math.sqrt(z[0]**2 + z[1]**2)
    angulo = math.atan2(z[1], z[0])
    return (magnitud, angulo)
     
def polara_cartesianocomplex(m):
    real = m[0] * math.cos(m[1])
    imaginario = m[0] * math.sin(m[1])
    return (real, imaginario)


def fasecomplex(m):
    fase = math.atan2(m[1], m[0])
    return fase








if __name__== '__main__':
    print(sumacomplex((4,5),(6,7))) # (4+5i) + (6+7i)
    print(restacomplex((4,5),(6,7))) # (4+5i) - (6+7i)
    print(productocomplex((4,5),(6,7))) # (4+5i) * (6+7i)
    print(divisioncomplex((4,5),(6,7))) # (4+5i) / (6+7i)
    print(modulocomplex((4,5))) #4+5i
    print(conjugadocomplex((4,5))) #4+5i
    print(cartesianoa_polarcomplex((4,5))) #4+5i
    print(polara_cartesianocomplex((6.4031242374328485, 0.8960553845713439))) #6.4031242374328485, 0.8960553845713439
    print(fasecomplex((4,5))) #4+5i
