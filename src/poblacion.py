from collections import namedtuple
import csv
from matplotlib import pyplot as plt

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero):
    res = []
    with open(ruta_fichero, encoding= 'UTF-8') as f:
        lector = csv.reader(f)
        for pais, codigo, año, censo in lector:
            pais = str(pais)
            codigo = str(codigo)
            año = int(año)
            censo = int(censo)
            Registro = RegistroPoblacion(pais , codigo , año , censo)
            res.append(Registro)
        return res
    

def calcula_paises(poblaciones):
    res = []
    for linea in poblaciones:
        if linea.pais not in res:
            res.append(linea.pais)
    res.sort
    return res


def filtra_por_pais(poblaciones, nombre_o_codigo):
    '''
    Toma una lista de tuplas de tipo RegistroPoblacion, y el nombre o código de un país,
    y devuelve una lista de tuplas con los datos del país que se pasa como parámetro (año y censo).
    ¡Importante!: el país puede venir expresado en el parámetro nombre_o_codigo con su nombre completo
    o con su código.
    '''
    res = []
    for linea in poblaciones:
        if nombre_o_codigo == linea.pais or nombre_o_codigo == linea.codigo:
            lista = (linea.año, linea.censo)
            res.append(lista)
    return res

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    res = []
    for linea in poblaciones:
        if linea.pais in paises and anyo == (linea.año + 1):
            datos = (linea.pais, linea.censo)
            res.append(datos)
    return res

def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    evolucion = filtra_por_pais(poblaciones, nombre_o_codigo)

    titulo = f"Evolución de la población de {nombre_o_codigo}"
    lista_años = []
    lista_habitantes = []

    for linea in evolucion:
        lista_años.append(linea[0])
        lista_habitantes.append(linea[1])

    plt.title(titulo)
    plt.plot(lista_años, lista_habitantes)
    plt.show()

def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):

    titulo = f"Población en el año {anyo}"
    lista_paises = []
    lista_habitantes = []

    res = []
    for linea in poblaciones:
        if linea.pais in paises and anyo == (linea.año):
            datos = (linea.pais, linea.censo)
            res.append(datos)

    for pais in res:
        lista_paises.append(pais[0])
        lista_habitantes.append(pais[1])

    plt.title(titulo)
    plt.bar(lista_paises, lista_habitantes)
    plt.show()