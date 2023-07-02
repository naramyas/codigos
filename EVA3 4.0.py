# Integrantes:
# Luis Aguilera.
# Carlos Figueroa.
# C1-B50-D

import datetime


def creacionUsuario():
    while True:
        try:
            rut = leerRut()
            dv = leerDv()
            rutFinal = validarRut(rut,dv)
            if rutFinal == True:
                global rutx
                rutx = str(rut) + dv
                return rutx
            else:
                print("\nRut incorrecto.")
        except:
            print("\nRut incorrecto.")

def crearContraseña():
    contraseña=input("\nCree su contraseña: ")
    print("\n¡Creación de usuario exitosa!")
    return contraseña

def validarUsuario(rut,contraseña):
    for i in range(3,-1,-1):
        print("\n--------------------------------------------------------------------------------------------")
        verRut = input("\nIngrese su rut completo sin puntos ni guión: ").upper()
        verContra = input("\nIngrese su contraseña: ")
        if contraseña == verContra and rut == verRut:
            print("\n¡Inicio de sesion correcto!")
            return True
        if i-1 == 0:
            print("\nYa no quedan intentos.")
            print("\nUsuario o contraseña incorrecta.")
            return False
        print("\nTe quedan {} intentos.".format(i-1))

def validarRut(rut,dv):
    while True:
        c=2
        suma=0
        while rut>0:
            d=rut%10
            suma+=d*c
            c+=1
            if c>7:
                c=2
            rut=int(rut/10)
        resto=suma%11
        dvv=11-resto
        dvr=""
        if dvv==11:
            dvr="0"
        elif dvv==10:
            dvr="K" or "k"
        else:
            dvr=str(dvv)
        return dv==dvr

def leerRut():
    while True:
        try:
            print("\n--------------------------------------------------------------------------------------------")
            rut=int(input("\nIngrese su rut sin dígito verificador: "))
            if rut < 99999999 and rut > 0:
                return rut
            else:
                print("\nRut incorrecto.")
        except:
            print("\nRut incorrecto.")

def leerDv():
    while True:
        try:
            
            dv=input("\nIngrese su dígito verificador: ").upper()
            if  dv == "K":
                return dv
            elif int(dv)>=0 and int(dv)<= 9:
                return dv
            else:
                print("\nDígito verificador incorrecto.")
        except:
            print("\nRut incorrecto.")

def deposito(saldo):
    while True:
        try:
            global rutx
            global diarioD
            op = int(input("\n¿De Cuánto es el depósito? "))
            diarioD += op
            if diarioD <= 100000:
                if op <= 100000:
                    saldo = validacionsaldoSuma(saldo,op)
                    global historialTransacciones
                    hora_actual=datetime.datetime.now()
                    fecha_actual = datetime.date.today()
                    historialTransacciones += "Depósito        | {}        | {}        | {}    | {} | {}        | \n".format(op,saldo,hora_actual.strftime(" %H:%M "),fecha_actual.strftime(" %d / %m / %y "),rutx) 
                    print("\nDepósito realizado con éxito. ")
                    return saldo
                
                else:
                    print("\nLímite diario excedido.")
            else:
                return print("\nLímite diario excedido.")
        except:
            print("\nIngresa solo números.")

def giro(saldo):
    while True:
        try:
            global diarioG
            op = int(input("\n¿De Cuánto es el giro? "))
            diarioG += op
            if diarioG < 200000:
                if op <= 200000:
                    saldo = validacionsaldoResta(saldo,op)
                    global historialTransacciones
                    hora_actual=datetime.datetime.now()
                    fecha_actual = datetime.date.today()
                    historialTransacciones += "Giro            | {}        | {}        | {}    | {} | -                | \n".format(op,saldo,hora_actual.strftime(" %H:%M "),fecha_actual.strftime(" %d / %m / %y "))
                    print("\nGiro realizado con éxito.")
                    return saldo
                else:
                    print("\nLímite diario excedido.")
            else:
                return print("\nLímite diario excedido.")
        except:
            print("\nIngresa solo números.")

def transferir(saldo):
    while True:
        try:
            destino = input("\nIngrese el nombre del destinatario. ")
            global rutx
            rut=leerRut()
            dv=leerDv()
            validarRut(rut,dv)
            global diarioT
            op = int(input("\n¿Cuánto vas a transferir? "))
            diarioT += op
            if diarioT < 250000:
                if op <= 250000:
                    saldo = validacionsaldoResta(saldo,op)
                    global historialTransacciones
                    hora_actual=datetime.datetime.now()
                    fecha_actual = datetime.date.today()
                    historialTransacciones += "Transferencia   | {}        | {}        | {}    | {} | {}        | \n".format(op,saldo,hora_actual.strftime(" %H:%M "),fecha_actual.strftime(" %d / %m / %y "),rutx)
                    print("\nTransferencia realizada con éxito.")
                    return saldo
                else:
                    print("\nLímite diario excedido.")
            else:
                return print("\nLímite diario excedido.")
        except:
            print("\nIngresa sólo números.")

def comprar(saldo):
    while True:
        try:
            tienda = input("\n¿En qué tienda estás comprando? ")
            op = int(input("\n¿Cuanto es el monto a pagar? "))
            saldo = validacionsaldoResta(saldo,op)
            global historialTransacciones
            hora_actual=datetime.datetime.now()
            fecha_actual = datetime.date.today()
            historialTransacciones += "Compra          | {}        | {}        | {}    | {} | {} | \n".format(op,saldo,hora_actual.strftime(" %H:%M "),fecha_actual.strftime(" %d / %m / %y "),tienda)
            print("\nCompra realizada con éxito.")
            return saldo
        except:
            print("\nIngresa solo números.")

def pagoServicio(saldo):
    while True:
        try:
            servicio = input("\n¿Qué servicio desea pagar? ")
            op = int(input("\n¿Cuanto es el monto a pagar? "))
            saldo = validacionsaldoResta(saldo,op)
            global historialTransacciones
            hora_actual=datetime.datetime.now()
            fecha_actual = datetime.date.today()
            historialTransacciones += "Pago Servicios  | {}        | {}        | {}    | {} | {} | \n".format(op,saldo,hora_actual.strftime(" %H:%M "),fecha_actual.strftime(" %d / %m / %y "),servicio)
            print("\nPago realizado con éxito.")
            return saldo
        except:
            print("\nIngresa solo números.")

def historial():
    print("\n--------------------------------------------------------------------------------------------")
    print("\n                 ¡Historial de Transacciones!")
    print("Transaccion     | Monto       | Saldo       | Hora       | Fecha          | Destino          |")
    print("Saldo Inicial   | 0           | 5000        |   -        |    -           |                  |")
    print(historialTransacciones) 
    print("\n--------------------------------------------------------------------------------------------")
    return                                                                               

def leerRespuestaSN():
    while True:
        respuesta=input("\nDeseas relizar otra operacion (S/N): ").upper()
        if respuesta == "S" or respuesta == "N":
            return respuesta
        else:
            print("\nDebes ingresar solo 'S' o 'N'")

def validacionsaldoSuma(saldo,op):
    while True:
        try:
            if saldo >= 0 and op > 0:
                saldo = saldo + op
                return saldo
            else:
                return print("\nEl monto debe ser mayor a $0.")
        except:
            print("\nSu saldo es insuficiente para realizar la transacción.")
            if leerRespuestaSN() == "N":
                break

def validacionsaldoResta(saldo,op):
    while True:
        try:
            if saldo > 0 and saldo >= op and op > 0:
                saldo = saldo - op
                return saldo
            elif op > saldo:
                return print("Saldo insuficuente.")
            else:
                return print("El monto debe ser mayor a $0.")
        except:
            print("Su saldo es insuficiente para realizar la transacción.")
            if leerRespuestaSN() == "N":
                break

def menu ():
    rut = ""
    contraseña = ""
    global historialTransacciones
    historialTransacciones = ""
    global saldo
    saldo = 5000
    global diarioD
    diarioD = 0
    global diarioG
    diarioG = 0
    global diarioT
    diarioT = 0
    while True:
        try:
            print("\n--------------------------------------------------------------------------------------------")
            print("\n¡Bienvenido a Python Bank!")
            print("\n1.- Ingresar. \n2.- Crear usuario. \n3.- Salir.")
            print("\n--------------------------------------------------------------------------------------------")
            pregunta = int(input("\n¿Que opcion desea realizar? "))
            match pregunta:
                case 1:
                    if validarUsuario(rut,contraseña):
                        while True:
                            try:
                                print("\n--------------------------------------------------------------------------------------------")
                                print("     Menu    ")
                                print("\n1.- Depositar. \n2.- Girar. \n3.- Transferir. \n4.- Comprar. \n5.- Pago de servicios. \n6.- Historial transacciones. \n7.- Cerrar sesion.")
                                print("\n--------------------------------------------------------------------------------------------")
                                pregunta1 = int(input("\n¿Que opcion desea realizar?. "))
                                match pregunta1:
                                    case 1:
                                        saldo = deposito(saldo)
                                    case 2:
                                        saldo = giro(saldo)
                                    case 3:
                                        saldo = transferir(saldo)
                                    case 4:
                                        saldo = comprar(saldo)
                                    case 5:
                                        saldo = pagoServicio(saldo)
                                    case 6:
                                        historial()
                                    case 7:
                                        break
                                if pregunta1 < 1 or pregunta1 > 7:
                                    print("\nIngresa una opcion valida.")
                                if leerRespuestaSN() == "N":
                                    break
                            except:
                                print("\nIngresa una opcion valida.")
                case 2:
                    rut = creacionUsuario()
                    contraseña = crearContraseña()
                case 3:
                    print("\nGracias por operar con Python Bank.")
                    break
            if pregunta < 1 or pregunta > 3:
                print("\nIngresa una opcion valida.")
        except:
            print("\nIngresa una opcion valida.")
        
def asd():
    global hola
    hola = ""
    
#pp
menu()

