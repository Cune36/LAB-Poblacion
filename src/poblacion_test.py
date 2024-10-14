import poblacion

def lee_poblaciones_test(ruta_fichero):
    Registro = poblacion.lee_poblaciones(ruta_fichero)
    print("Imprimiendo los 3 primeros:")

    for i in range(3):
        print(Registro[i])
    print("Imprimiendo los 3 ultimos:")
    for i in range(3):
        print(Registro[-(i + 1)])

def calcula_paises_test(poblaciones):
    lista_paises = poblacion.calcula_paises(poblaciones)
    for linea in lista_paises:
        print(linea)

def filtra_por_pais_test(poblaciones, nombre_o_codigo):
    lista = poblacion.filtra_por_pais(poblaciones, nombre_o_codigo)
    print(f"Datos de {nombre_o_codigo}:")
    for linea in lista:
        print(linea)
    
def filtra_por_paises_y_anyo_test(poblaciones, anyo, paises):
    lista = poblacion.filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    for linea in lista:
        print(linea)

def muestra_evolucion_poblacion_test(poblaciones, nombre_o_codigo):
    poblacion.muestra_evolucion_poblacion(poblaciones, nombre_o_codigo)

def muestra_comparativa_paises_anyo_test(poblaciones, anyo, paises):
    poblacion.muestra_comparativa_paises_anyo(poblaciones, anyo, paises)

if __name__ == "__main__":
    #lee_poblaciones_test("data\population.csv")
    poblaciones = poblacion.lee_poblaciones("data\population.csv")
    #calcula_paises_test(poblaciones)
    #filtra_por_pais_test(poblaciones,"ESP")
    #filtra_por_paises_y_anyo_test(poblaciones, 2015, {'Spain', 'United Kingdom'})
    #muestra_evolucion_poblacion_test(poblaciones, "ESP")
    muestra_comparativa_paises_anyo_test(poblaciones, 2016, {"China", 'France', 'Mexico', 'Portugal', 'Spain'})