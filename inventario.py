matriz_original=[]
def matriz_inventario(matrizx):
    with open("inventario.txt", 'r') as archivo:
        registros = archivo.readlines()
        for datos in registros:
            # Eliminar los espacios en blanco y dividir los datos por ";"
            datos_procesados = datos.strip().split(";")
            # Agregar los datos procesados a la matriz
            matrizx.append(datos_procesados)
    return matrizx

def actualizacion_inventario_agregar(rut,matriz):
    print("Sapo1")
    for fila in matriz:
        print("sapoo2")
        print (f"El producto ,{fila[0]}, tiene, {fila[1]}")
        salida=int((input(f"cual es el nuevo stock")))
        if salida != fila[0]:
                guardar_log(fila[0],fila[1],salida,rut)
        guardar_new_stock(fila[0],salida)
    return
def guardar_log(prd,old,new,rut):
    print("sapo11111")
    registro = f"{prd},{old},{new},{rut}\n"
    with open ("registro_log.txt", 'a') as archivo:
        archivo.write(registro)
    return

def guardar_new_stock(prd,new):
    print("sapo2222")
    registro = f"{prd},{new}\n"
    with open ("new_stock.txt", 'a') as archivo:
        archivo.write(registro)
    return

matriz_inventario(matriz_original)
print(matriz_original)
rut= input("rut del usuario que va a realizar el inventario: ")
actualizacion_inventario_agregar(rut,matriz_original)
