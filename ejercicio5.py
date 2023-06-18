import funciones5 as fn

opcion = 0
partes = []
productos = []
precios = []
descripcion = []

while opcion != 4:
    fn.generarMenu()
    try:
        opcion = int(input("Escoge una opción: "))
        if opcion == 1:
            partes = fn.grabarParte(partes,productos,precios,descripcion)
        elif opcion == 2:
            fn.buscar(partes,productos,precios)
        elif opcion == 3:
            fn.imprimir(partes,descripcion,productos,precios)
        elif opcion == 4:
            fn.salir()
            break
        else:
            print("Debes elegir una opción válida.")
    except:
        print("Ingresa un valor numérico.")
