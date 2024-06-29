import json
from datetime import datetime
import os

ventas = []

def menu():
    opcion = 0
    try:
        opcion = int(input('''\n******** Gestión de ventas de la mejor pizzería del mundo ********     
        1. Registrar una venta
        2. Mostrar todas las ventas
        3. Buscar venta por cliente
        4. Guardar las ventas en un archivo
        5. Cargar ventas desde un archivo
        6. Generar boleta
        7. Anular venta
        8. salir del programa
        Ingrese una opción: '''))
    except ValueError:
        print("Por favor ingrese una opción válida, entre 1 y 7")
        opcion = 0
    return opcion


def registrar():
    print("\n*** Registrar una venta ***")
    while True:
        cliente = input("\nIndique el nombre del cliente para comenzar con el registro de la venta: ").lower()
        cliente_registrado = False

        for cliente_buscar in ventas:
            if cliente_buscar['cliente'] == cliente:
                print(f"El cliente '{cliente}' ya se encuentra registrado")
                cliente_registrado = True
                break
        
        if cliente_registrado:
            continue
        else:
            print(f"Nuevo cliente '{cliente}', ingresar datos de venta:")
            cuaq_p = int(input("Indique la cantidad deseada de Cuatro quesos pequeña ($6.000): "))
            cuaq_m = int(input("Indique la cantidad deseada de Cuatro quesos mediana ($9.000): "))
            cuaq_f = int(input("Indique la cantidad deseada de Cuatro quesos familiar ($12.000): "))
            haw_p = int(input("Indique la cantidad deseada de Hawaiana pequeña ($6.000): "))
            haw_m = int(input("Indique la cantidad deseada de Hawaiana mediana ($9.000): "))
            haw_f = int(input("Indique la cantidad deseada de Hawaiana familiar ($12.000): "))
            nap_p = int(input("Indique la cantidad deseada de Napolitana pequeña ($5.500): "))
            nap_m = int(input("Indique la cantidad deseada de Napolitana mediana ($8.500): "))
            nap_f = int(input("Indique la cantidad deseada de Napolitana familiar ($11.000): "))
            pep_p = int(input("Indique la cantidad deseada de Peperoni familiar ($7.000): "))
            pep_m = int(input("Indique la cantidad deseada de Peperoni familiar ($10.000): "))
            pep_f = int(input("Indique la cantidad deseada de Peperoni familiar ($13.000): "))
            subtotal = (cuaq_p*6000)+(cuaq_m*9000)+(cuaq_f*12000)+(haw_p*6000)+(haw_m*9000)+(haw_f*12000)+(nap_p*5500)+(nap_m*8500)+(nap_f*11000)+(pep_p*7000)+(pep_m*10000)+(pep_f*13000)
            while True:
                try:
                    cat_descuento = int(input('''\nSeleccione una categoría de descuento
                    1. Estudiante diurno: descuento de 12%
                    2. Estudiante vespertino: descuento de 14%
                    3. Administrativo: 10%
                    Seleccione una opción: '''))
                    if cat_descuento not in [1, 2, 3]:
                        raise ValueError("Por favor ingrese una opción válida (1, 2 o 3)")
                    break
                except ValueError as e:
                    print(e)
            if cat_descuento == 1:
                descuento = subtotal * 0.12
            elif cat_descuento == 2:
                descuento = subtotal * 0.14
            elif cat_descuento == 3:
                descuento = subtotal * 0.1
            total = subtotal - descuento
            nueva_venta = {
                'cliente': cliente,
                'cuatro quesos pequeña': cuaq_p, 
                'cuatro quesos mediana': cuaq_m, 
                'cuatro quesos familiar': cuaq_f, 
                'hawaiana pequeña': haw_p, 
                'hawaiana mediana': haw_m, 
                'hawaiana familiar': haw_f, 
                'napolitana pequeña': nap_p, 
                'napolitana mediana': nap_m, 
                'napolitana familiar': nap_f, 
                'peperoni pequeña': pep_p, 
                'peperoni mediana': pep_m, 
                'peperoni familiar': pep_f, 
                'subtotal': subtotal,
                'descuento': descuento,
                'total': total
            }
            ventas.append(nueva_venta)
            print("\nVenta registrada con éxito!")
            break
    return nueva_venta


def mostrar_ventas():
    print("\n*** Resumen de ventas registradas en el sistema ***")
    contador = 0
    for venta in ventas:
        contador += 1
        print("\nDatos de venta:")
        for clave, valor in venta.items():
            print(f"- {clave}: {valor}")


def buscar_venta():
    print("\n*** Buscar venta por cliente ***")
    cliente_buscar = input("\nIngrese el nombre del cliente que desea buscar: ").lower()
    cliente_encontrado = False
    for venta in ventas:
        if venta['cliente'] == cliente_buscar:
            cliente_encontrado = True
            print("El cliente se encuentra registrado en el sistema")
            print(f"\nDatos de la venta asociados al cliente '{cliente_buscar}':")
            for clave, valor in venta.items():
                print(f"- {clave}: {valor}")
            break
    if not cliente_encontrado:
        print(f"El cliente {cliente_buscar} no se encuentra registrado en el sistema. Registre la venta primero, vaya a opción 1 del menú")


def guardar_ventas():
    print("*** Guardar ventas en archivo ***")
    with open('ventas.json', 'w', encoding='utf-8') as archivo:
        json.dump(ventas, archivo, ensure_ascii=False, indent=4)
        print("\nDatos guardados con éxito")
        print(f"Sus datos se han guardado en {os.getcwd()}")


def cargar_ventas():
    print("*** Cargar ventas desde archivo ***")
    global ventas
    try:
        with open('ventas.json', 'r', encoding='utf-8') as archivo:
            ventas = json.load(archivo)
            print(f"Ventas cargadas exitosamente desde el directorio {os.getcwd()}")
    except FileNotFoundError:
        print("El archivo de ventas no se ha podido cargar. Archivo no encontrado o ventas no registradas con anterioridad")


def generar_boleta():
    print("\n*** Boleta de venta ***")
    boleta_cliente = input("\nIngrese el nombre del cliente para generar boleta: ").lower()
    boleta_encontrado = False
    fecha_hora_actual = datetime.now()
    fecha_formato = fecha_hora_actual.strftime("%d-%m")
    hora_formato = fecha_hora_actual.strftime("%H:%M:%S")
    for venta in ventas:
        if venta['cliente'] == boleta_cliente:
            boleta_encontrado = True
            print(f'''\n
        ****** Boleta electrónica ******

{fecha_formato}
{hora_formato}

----------------------------------------------------
Detalle

{venta['cuatro quesos pequeña']} pizza cuatro quesos pequeña                     ${venta['cuatro quesos pequeña']*6000}
{venta['cuatro quesos mediana']} pizza cuatro quesos mediana                      ${venta['cuatro quesos mediana']*9000}
{venta['cuatro quesos familiar']} pizza cuatro quesos familiar                     ${venta['cuatro quesos familiar']*12000}
{venta['hawaiana pequeña']} pizza hawaiana pequeña                  ${venta['hawaiana pequeña']*6000}
{venta['hawaiana mediana']} pizza hawaiana mediana                  ${venta['hawaiana mediana']*9000}
{venta['hawaiana familiar']} pizza hawaiana familiar                 ${venta['hawaiana familiar']*12000}
{venta['napolitana pequeña']} pizza napolitana pequeña                   ${venta['napolitana pequeña']*5500}
{venta['napolitana mediana']} pizza napolitana mediana                   ${venta['napolitana mediana']*8500}
{venta['napolitana familiar']} pizza napolitana familiar                  ${venta['napolitana familiar']*11000}
{venta['peperoni pequeña']} pizza napolitana pequeña                   ${venta['peperoni pequeña']*7000}
{venta['peperoni mediana']} pizza napolitana mediana                   ${venta['peperoni mediana']*1000}
{venta['peperoni familiar']} pizza napolitana familiar                  ${venta['peperoni familiar']*13000}
----------------------------------------------------
Subtotal                                      ${round(venta['subtotal'])}
Descuento                                     ${round(venta['descuento'])}

                
Total                                         ${round(venta['total'])}
----------------------------------------------------
            !Gracias por su preferencia!
                ''') 
            break
    if not boleta_encontrado:
        print(f"No hay datos de venta asociados al cliente'{boleta_cliente}', por lo que no es posible generar la boleta")



def anular_venta():
    print("\n*** Anular venta ***")
    cliente_anular = input("\nIngrese el nombre del cliente cuya venta desea anular: ").lower()
    cliente_encontrado = False
    for venta in ventas:
        if venta['cliente'] == cliente_anular:
            cliente_encontrado = True
            print("El cliente se encuentra registrado en el sistema. Procediendo a eliminar la venta")
            ventas.remove(venta)
            print(f"Venta asociada al cliente '{cliente_anular}' anulada exitosamente")
            break
    if not cliente_encontrado:
        print(f"El cliente '{cliente_anular}' no se encuentra registrado en el sistema de ventas. Primero proceda al registro en la opción 1 del menú")


def salir():
    while True:
        try:
            opcion = input("\n¿Está seguro de que desea salir? (1:sí - 2:no)")
            if opcion == 1:
                print("Gracias por su preferencia. Hasta pronto")
                return True
            elif opcion == 2:
                print("Puede continuar operando")
                return False
            else:
                print("Por favor ingrese una opción válida (1:sí - 2:no)")
        except ValueError:
            print("Entrada inválida. Por favor ingrese 1 o 2")


while True:
    opcion = menu()
    if opcion == 1:
        registrar()
    elif opcion == 2:
        mostrar_ventas()
    elif opcion == 3:
        buscar_venta()
    elif opcion == 4:
        guardar_ventas()
    elif opcion == 5:
        cargar_ventas()
    elif opcion == 6:
        generar_boleta()
    elif opcion == 7:
        anular_venta()
    elif opcion == 8:
        if salir():
            break
    else:
        print("Opción no reconocida, por favor seleccione una opción entre 1 y 7")

















