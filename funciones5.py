def generarMenu():
    menu = ["Grabar","Buscar","Imprimir","Salir"]
    for i in range(len(menu)):
        print(f"{i+1}){menu[i]}")

def grabarParte(partes,productos,precios,descripcion):
    option = 0
    while option != 2:
        validacion = False
        try:
            numeroParte = input("Ingresa el número de parte: ")
            if len(partes) == 0:
                validacion = validarParte(numeroParte)
            else:
                for x in partes:
                    if x == numeroParte:
                        print("Error.El número de parte ya se encuentra en el sistema.")
                    else:
                        validacion = validarParte(numeroParte)
            if validacion == True:
                print("Numero de parte grabado.")
                partes.append(numeroParte)
                ingresarNombre(productos)
                ingresarDescripcion(descripcion)
                ingresarPrecio(precios)
                while True:
                    print("1)Ingresar otro número de parte.")
                    print("2)Salir.")
                    try:
                        continuar = int(input("Ingresa 1 si deseas grabar otro número de parte o 2 para salir: "))
                        if continuar == 1:
                            option = 1
                            break
                        else:
                            option = 2
                            break
                    except:
                        print("Debes ingresar un valor numérico.")
            else:
                print("Debe ingresar un número de parte válido.")
        except:
            print("Numero de parte inválido.")
    print("Información guardada.")
    return partes

def validarParte(numeroParte):
    valor1 = int(numeroParte[:6])
    valor2 = numeroParte[7]
    valor3 = int(numeroParte[8:10])
    guion1 = numeroParte[6]
    if len(numeroParte) == 10 or len(numeroParte)== 13:
        if len(numeroParte) == 10:
            if type(valor1) == int and type(valor3) == int and guion1 == "-" and  validarLetra(valor2):
                return True
            else:
                return False
        if len(numeroParte) == 13:
            valor4 = numeroParte[11]
            valor5 = int(numeroParte[12])
            guion2 = numeroParte[10]
            if type(valor1) == int and type(valor3) == int and guion1 == "-" and validarLetra(valor2) and guion2 == "-" and validarLetra(valor4) and type(valor5) == int:
                return True
            else:
                return False
    else:
        return False

def validarLetra(valor):
    numeros = ["1","2","3","4","5","6","7","8","9","0"]
    for x in valor:
        for i in numeros:
            if x == i:
                return False
            else:
                return True

def imprimir(partes,descripcion,productos,precios):
    while True:
        if len(partes) >= 2:
            print("")
            print("*"*10,"REPORTE DE PRODUCTOS","*"*10)
            print("")
            for i in range(len(partes)):
                print(f"{partes[i]}  {productos[i]}  {descripcion[i]}  {precios[i]}")
            print("")
            print("-"*40)
            break
        else:
            print("Debes tener como mínimo 10 partes almacenados para buscar.")
            break

def ingresarNombre(productos):
    while True:
        try:
            nombreProducto = input("Ingrese nombre del producto.")
            validacion = validarLetra(nombreProducto)
            if validacion == True:
                if len(nombreProducto) > 6:
                    productos.append(nombreProducto)
                    print("El producto se ha guardado correctamente")
                    break
                else:
                    print("El nombre del producto debe tener al menos 6 caracteres.")
            else:
                print("No puedes ingresar números.")
        except:
            print("Debes ingresar valores válidos.")
    return productos

def ingresarPrecio(precios):
    while True:
        try:
            precio = int(input("Ingrese precio: "))
            if precio > 0:
                precios.append(precio)
                print("Precio guardado correctamente.")
                break
            else:
                print("El precio debe ser mayor a 0.")
        except:
            print("Debes ingresar un valor numérico.")

def ingresarDescripcion(descripcion):
    while True:
        try:
            descripcionProducto = input("Ingrese descripcion del producto.")
            if descripcionProducto != "":
                descripcion.append(descripcionProducto)
                print("La descripci+on del producto se ha guardado correctamente")
                break
            else:
                print("Descripción inválida.")
        except:
            print("Debes registrar una descripción válida.")
    return descripcion

def buscar(partes,productos,precios):
    validarCodigoParte = False
    while True:
        if len(partes) >= 2:
            while True:
                try:
                    codigoParte = input("Ingrese número de parte a buscar: ")
                    validado = validarParte(codigoParte)
                    if validado == True:
                        for x in range(len(partes)):
                            if partes[x] == codigoParte:
                                validarCodigoParte = True
                        if validarCodigoParte == True:
                            mostrarInfoProducto(codigoParte,partes,precios,productos)
                        else:
                            print("El código no se encuentra guardado en el sistema.")
                        break
                    else:
                        print("Código de parte inválido.")
                except:
                    print("Debes ingresar un código de parte válido.")
            break
        else:
            print("Debes tener como mínimo 10 partes almacenados para buscar.")
            break
    
def mostrarInfoProducto(codigoParte,partes,precios,productos):
    indice = 0
    for i in range(len(partes)):
        if partes[i] == codigoParte:
            indice = i
    if precios[indice] >= 500:
        print("*"*10,"Información del producto","*"*10)
        print(f"{codigoParte} {productos[indice]} ${precios[indice]}")
    else:
        print("Producto sin stock")

def salir():
    print("Has salido del programa.")
    print("Diego Nahum Altamirano Gallardo.")
    print("Version del programa 1.0.0")