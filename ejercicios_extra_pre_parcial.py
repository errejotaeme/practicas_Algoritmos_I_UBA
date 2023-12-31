import math, pprint
import matplotlib.pyplot as plt
import numpy as np



# E-1 Función que calcula con qué signo del horoscopo chino
# se corresponde el año ingresado
def congruentes(a:int, b:int, m:int) -> bool: #AUX
    return (a % m) == (b % m)

def signo() -> dict[int, str]: #AUX
    d:dict = dict()
    signos:list[str] = ['Mono','Gallo', 'Perro', 'Cerdo', 'Rata', 'Buey', 'Tigre',
                        'Conejo', 'Dragón', 'Serpiente', 'Caballo', 'Cabra']
    for i in range(len(signos)):
        d[i] = signos[i]
    return d

def calendario_chino(n:int) -> str:
    for i in range(12):
        if congruentes(n, i, 12):
            return signo()[i]                      




# E-2 Función que retorna las raíces en R de una cuadrática
def resolvente(a:int, b:int, c:int):
    discriminante:int = (b**2) - (4*a*c)
    res:str = ""
    
    if discriminante > 0:
        res_1:float = (-b + math.sqrt(discriminante)) / 2*a
        res_2:float = (-b - math.sqrt(discriminante)) / 2*a
        res += f"Las raíces son {str(round(res_1, 2))} y {str(round(res_2, 2))}"
        
    elif discriminante == 0:
        res_1 = (-b / 2*a)
        res += f"La raíz es {str(round(res_1, 2))}"
        
    else:
        res += "No tiene solución en R"
    
    return res
        



# E-3 Función que genera la Criba de Eratostenes
def criba_eratostenes(n:int) -> list[int]:
    lista_aux:list[int] = list(range(n + 1))
    lista_aux = lista_aux[2:]
    for a in lista_aux:
        for b in lista_aux:
            if a == b:
                continue
            elif b % a == 0:
                lista_aux.remove(b)
    return lista_aux




# E-4 Funciones que aplican el cifrado César
# Recibe como argumento la ruta a un txt
# y una clave c tal que 1 ⩽ c < 26
def cifrado_cesar(ruta:str, clave:int) -> None:
    with open(ruta, 'r') as archivo:
        contenido = archivo.read()
    lista_de_caracteres: list[str] = [c for c in contenido]
    
    lista_aux: list[str] = []
    for caracter in lista_de_caracteres:
        x:int = ord(caracter)
        if (x >= 65 and x <= 90):
            x += clave
            if x > 90:
                x = 64 + (x % 90)
                lista_aux.append(chr(x))
            else:
                lista_aux.append(chr(x))
        
        elif (x >= 97 and x <= 122):
            x += clave
            if x > 122:
                x = 96 + (x % 122)
                lista_aux.append(chr(x))
            else:
                lista_aux.append(chr(x))
        
        else:
            lista_aux.append(chr(x))
    
    texto_aux:str = ''.join(lista_aux)
    with open(f'{ruta[:-4]}_cifrado.txt', 'w') as archivo:
        archivo.write(texto_aux)
        
        
# Recibe como argumento la ruta al texto cifrado
# y la clave con la que fué cifrado
def descifrado_cesar(ruta:str, clave:int) -> None:
    with open(ruta, 'r') as archivo:
        contenido = archivo.read()
    lista_de_caracteres: list[str] = [c for c in contenido]
    
    lista_aux: list[str] = []
    for caracter in lista_de_caracteres:
        x:int = ord(caracter)
        if (x >= 65 and x <= 90):
            x -= clave
            if x < 65:
                x = 91 - (65 % x)
                lista_aux.append(chr(x))
            else:
                lista_aux.append(chr(x))
        
        elif (x >= 97 and x <= 122):
            x -= clave
            if x < 97:
                x = 123 - (97 % x)
                lista_aux.append(chr(x))
            else:
                lista_aux.append(chr(x))
        
        else:
            lista_aux.append(chr(x))
    
    texto_aux:str = ''.join(lista_aux)
    with open(f'{ruta[:-4]}_descifrado.txt', 'w') as archivo:
        archivo.write(texto_aux)     
    



# E-5 Función que aplica el algoritmo de Euclides y retorna el mcd(a, b)
def euclides(a:int, b:int):
    par: list[int] = [a, b]
    while min(par) > 0:
        par[par.index(max(par))] = max(par) - min(par)
    return max(par)

# Otra implementación del algoritmo de Euclides
def euclides_2(a:int, b:int):
    par: list[int] = [a, b]
    while min(par) > 0:
        cociente = max(par) // min(par)    
        par[par.index(max(par))] = max(par) - min(par) * cociente
    return max(par)




# E-6 Función que encuentra los coeficientes s, t
# de la Identidad de Bézout: si x⊥y ⟹ (x:y) = 1 = s·x + t·y
def bezout(x:int, y:int) -> str:    
    par:list[int] = [x, y]
    s:int = 1
    t:int = 0    
    divisor_s:int = 0
    divisor_t:int = 1
    lista_aux:list[tuple[int]] = []
    
    # Euclides
    while min(par) > 0:        
        cociente:int = max(par) // min(par)                                     
        par[par.index(max(par))] = max(par) - min(par) * cociente
                
        # Cuenta clave
        resto_s:int = s - cociente * divisor_s
        resto_t:int = t - cociente * divisor_t        
        # Sustitución de valores
        s = divisor_s
        divisor_s = resto_s
        t = divisor_t        
        divisor_t = resto_t
        # Consevr
        lista_aux.append((s, t))

    res:str =f'(±{max(abs(s), abs(t))})·{min(x, y)}  ±  ({min(abs(s), abs(t))})·{max(x, y)}  =  {max(par)}'                     
    return res



# E-7 Función que convierte una cadena de carcateres a código Morse
def c_m() -> dict[str, str]: #AUX
    d:dict[str, str] = dict()
    l:list[str] = ['.-','-..','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--',
                   '-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
    n:list[str] = ['------','.----','..---','...--','....-','.....','-....','--...','---..','----.']
    
    x:int = 97
    for i in range(len(l)):
        d[chr(x+i)] = l[i]
    
    x = 48
    for i in range(len(n)):
        d[chr(x+i)] = n[i]
    
    return d

def texto_a_morse(t:str) -> str:
    t = t.lower()
    res:str = ''
    morse:dict[str, str] = c_m()
    for c in t:
        if c == ' ':
            res += c*2
        elif c not in morse.keys():
            continue
        else:        
            res += f'{morse[c]} '
    return res



# E-8 Función que retorna un diccionario con los números entre 1 y n
# convertidos del sistema decimal al sistema de numeración romano
def romanos(n:int)->dict[int, str]:
    d:dict[int, str] = dict()
    for i in range(n):
        d[i+1] = a_romano(i+1)
    return d
     
def a_romano(n:int) -> str: #AUX Recursiva
    res:str = ''
    if  n > 3999999 or n < 0:
        res += "Cifra inválida"
    # Unidades
    if (n < 10):
        if n == 4:
            res += 'IV'
        elif n == 9:
            res += 'IX' 
        else:
            res += 'V' * (n // 5) + 'I' * (n % 5)
    # Decenas < 50
    elif (n >= 10 and n < 50):
        if (n // 10 == 4):
            res += 'XL' + a_romano(n % 10)
        else:
            res += 'X' * (n // 10) + a_romano(n % 10)
    # Decenas > 50
    elif (n >= 50 and n < 100):
        if (n // 10 == 9):
            res += 'XC' + a_romano(n % 10)
        else:
            res += 'L' * (n // 50) + a_romano(n % 50)
    # Centenas < 500    
    elif (n >= 100 and n < 500):
        if (n // 100 == 4):
            res += 'CD' + a_romano(n % 100)
        else:
            res += 'C' * (n // 100) + a_romano(n % 100)
    # Centenas > 500    
    elif (n >= 500 and n < 1000):
        if (n // 100 == 9):
            res += 'CM' + a_romano(n % 100)
        else:
            res += 'D' * (n // 500) + a_romano(n % 500)
    # Millares > 5000    
    elif (n >= 1000 and n < 5000):
        if (n // 1000 == 4):
            res += 'ĪV̄' + a_romano(n % 1000)
        else:
            res += 'M' * (n // 1000) + a_romano(n % 1000)
    # Millares < 5000    
    elif (n >= 5000 and n < 10000):
        if (n // 1000 == 9):
            res += 'ĪX̄' + a_romano(n % 1000)
        else:
            res += 'V̄' * (n // 5000) + a_romano(n % 5000)
    # Decenas de millares < 50000    
    elif (n >= 10000 and n < 50000):
        if (n // 10000 == 4):
            res += 'X̄L̄' + a_romano(n % 10000)
        else:
            res += 'X̄' * (n // 10000) + a_romano(n % 10000)
    # Decenas de millares > 50000    
    elif (n >= 50000 and n < 100000):
        if (n // 10000 == 9):
            res += 'X̄C̄' + a_romano(n % 10000)
        else:
            res += 'L̄' * (n // 50000) + a_romano(n % 50000)
    # Centenas de millares < 500000    
    elif (n >= 100000 and n < 500000):
        if (n // 100000 == 4):
            res += 'C̄D̄' + a_romano(n % 100000)
        else:
            res += 'C̄' * (n // 100000) + a_romano(n % 100000)
    # Centenas de millares > 500000    
    elif (n >= 500000 and n < 1000000):
        if (n // 100000 == 9):
            res += 'C̄M̄' + a_romano(n % 100000)
        else:
            res += 'D̄' * (n // 500000) + a_romano(n % 500000)
    # Millones < 4000000    
    elif (n >= 1000000):
        res += 'M̄' * (n // 1000000) + a_romano(n % 1000000)     
    
    return res 


# Función que retorna la distancia  en kilómetros entre dos puntos 
# del planeta dados en forma de grados decimales (DD)
def distancia(lat_a,long_a, lat_b, long_b) -> str:
    res:float = 0.
    radio_tierra:float = 6378
    if lat_a < -90 or lat_a > 90:
        res = -1.
    elif long_a < -180 or long_a > 180:
        res = -1.
    elif lat_b < -90 or lat_b > 90:
        res = -1.
    elif long_b < -180 or long_b > 180:
        res = -1.
    else:
        a_la:float = math.radians(lat_a)
        a_lo:float = math.radians(long_a)
        b_la:float = math.radians(lat_b)
        b_lo:float = math.radians(long_b)
        d_lat = b_la - a_la
        d_long = b_lo - a_lo
        x:float = (math.sin(d_lat/2)**2 + 
             math.cos(a_la) * 
             math.cos(b_la) * 
             math.sin(d_long/2)**2)
        y:float = 2*math.atan2(math.sqrt(x), math.sqrt(1 - x))     
        res = radio_tierra * y
    
    return f'{round(res, 3)} kilómetros'


# NÚMEROS COMPLEJOS  
    
# Función que grafica en un plano polar
# una lista de números complejos dados en forma binomial 
def graf_polar(c:list[complex], tipo_de_linea='-'):
    
    for x in range(len(c)):
        prueba = str(c[x])
        prueba = prueba[1:-1]    
        vector = plt.polar([np.angle(0), np.angle(c[x])],
                         [np.abs(0), np.abs(c[x])], 
                         label=f'|{prueba}| = {round(abs(c[x]), 2)}, θ = {round(np.angle(c[x]), 4)} rad', 
                         linestyle=tipo_de_linea)
    plt.legend(loc='center right', bbox_to_anchor=(1.30, 0.0), prop={"size":7})
    plt.savefig('complejo_en_plano_polar')
    plt.show()
    

# Función que convierte un complejo de binomial a polar
def a_polar(z:complex) -> str:
    a:int = z.real
    b:int = z.imag
    r:float = math.sqrt(a**2 + b**2)
    arg_z = math.acos(a/r)   
    return f'|{round(r,2)}|·[cos({round(arg_z,7)}) + i·sen({round(arg_z,7)})]' 

# Función que convierte un complejo de polar a binomial
def a_binomial(modulo:float, argumento:float) -> complex:
    a:float = round(math.cos(argumento) * modulo, 2)
    b:float = round(math.sin(argumento) * modulo, 2)
    return complex(a, b)


# Función que halla las raíces enesimas de un complejo
# dado en forma binomial 
def n_raices(c:complex, n:int) -> list[complex]:
    res: list[complex] = []
    res.append(c)
    a:int = c.real
    b:int = c.imag
    r:float = math.sqrt(a**2 + b**2)
    arg_c = math.acos(a/r)  
    
    # Halla cada raíz
    for k in range(n):
        ap: float = (arg_c + (2*k*math.pi)) / n
        if ap > math.pi*2:
            ap -= math.pi*2
        res.append(a_binomial(r**(1/n), ap))
        
    # Genera el plano polar con los números como vectores
    graf_polar(res)
    
    return res[1:]
