"""
    Proyecto Bimestral
    Segundo Bimestre

    Problemática:
"""


def crearFacebook():
    nombreUsuario = input("Ingresar el nombre del usuario\n")
    edad = int(input("Ingresar la edad\n"))
    ciudad = str(input("Ingresar la ciudad\n"))
    pais = str(input("Ingresar el país\n"))
    correo = str(input("Ingresar el correo electronico\n"))

    datosFacebook = "Los datos para facebook son: \n%s\n%d\n%s\n%s\n%s\n" % (
        nombreUsuario, edad, ciudad, pais, correo)

    return datosFacebook


def crearTwitter():
    nombreUsuario = input("Ingresar el nombre del usuario\n")
    nombres = str(input("Ingresar los nombres\n"))
    apellidos = input("Ingresar los apellidos\n")
    edad = int(input("Ingresar la edad\n"))
    ciudad = str(input("Ingresar la ciudad\n"))
    pais = str(input("Ingresar el país\n"))
    idioma = str(input("Ingresar el idioma\n"))
    correo = str(input("Ingresar el correo electronico\n"))

    datosTwitter = "Los datos para Twitter son: \n%s\n%s\n%s\n%d\n%s\n%s\n%s\n%s\n" % (nombreUsuario, nombres,
                                                                                     apellidos, edad, ciudad, pais, idioma,
                                                                                     correo)

    print(datosTwitter)


def crearWhatsapp():
    nombreUsuario = input("Ingresar el nombre del usuario\n")
    telefono = int(input("Ingresar el numero de telefono\n"))
    edad = int(input("Ingresar la edad\n"))
    ciudad = str(input("Ingresar la ciudad\n"))
    pais = str(input("Ingresar el país\n"))

    datosWhatsapp = "Los datos para Whatsapp son: \n%s\n%d\n%d\n%s\n%s\n" % (
        nombreUsuario, telefono, edad, ciudad, pais)

    return datosWhatsapp


def crearTelegram():
    nombreUsuario = input("Ingresar el nombre del usuario\n")
    telefono = int(input("Ingresar el numero de telefono\n"))
    ciudad = str(input("Ingresar la ciudad\n"))
    pais = str(input("Ingresar el país\n"))
    area = str(input("Ingresar el area de interes\n"))

    datosTelegram = "Los datos para Telegram son: \n%s\n%d\n%s\n%s\n%s\n" % (
        nombreUsuario, telefono, ciudad, pais, area)

    print(datosTelegram)


def crearSignal():
    nombreUsuario = input("Ingresar el nombre del usuario\n")
    telefono = int(input("Ingresar el numero de telefono\n"))
    ciudad = str(input("Ingresar la ciudad\n"))
    pais = str(input("Ingresar el país\n"))
    hobby = str(input("Ingresar el hobby\n"))

    datosSignal = "Los datos para Signal son: \n%s\n%d\n%s\n%s\n%s\n" % (
        nombreUsuario, telefono, ciudad, pais, hobby)

    return datosSignal


def crearInstagram():
    nombreUsuario = input("Ingresar el nombre del usuario\n")
    edad = int(input("Ingresar la edad\n"))
    ciudad = str(input("Ingresar la ciudad\n"))
    correo = str(input("Ingresar el correo electronico\n"))

    datosInstagram = "Los datos para Instagram son: \n%s\n%d\n%s\n%s\n" % (
        nombreUsuario, edad, ciudad, correo)

    print(datosInstagram)


def crearFlickr():
    nombreUsuario = str(input("Ingresar el nombre del usuario\n"))
    correo = str(input("Ingresar el correo electronico\n"))

    datosFlickr = "Los datos para Flickr son: \n%s\n%s\n" % (
        nombreUsuario, correo)

    return datosFlickr


def obtenerMensajefinal(contador):
     mensajeFinal = ["Campaña con poca afluencia",
            "Campaña moderada siga adelante", "Excelente campaña"]
     if contador >= 1 and contador <= 5:
         print(mensajeFinal[0])
     else:
         if contador >= 6 and contador <= 15:
             print(mensajeFinal[1])
         else:
             if contador >= 16:
                 print(mensajeFinal[2])


condicion = True
contador = 0

while (condicion):
    contador = contador + 1

    numero = int(input("Ingrese 1 para crear una cuenta en Facebook\n"
                       "Ingrese 2 para crear una cuenta en Twitter\n"
                       "Ingrese 3 para crear una cuenta en Whatsapp\n"
                       "Ingrese 4 para crear una cuenta en Telegram\n"
                       "Ingrese 5 para crear una cuenta en Signal\n"
                       "Ingrese 6 para crear una cuenta en Instagram\n"
                       "Ingrese 7 para crear una cuenta en Flickr\n"))
    if numero == 1:
        print(crearFacebook())
    else:
        if numero == 2:
            crearTwitter()
        else:
            if numero == 3:
                print(crearWhatsapp())
            else:
                if numero == 4:
                    crearTelegram()
                else:
                    if numero == 5:
                        print(crearSignal())
                    else:
                        if numero == 6:
                            crearInstagram()
                        else:
                            if numero == 7:
                                print(crearFlickr())
                            else:
                                print("Error número fuera de rango")


    salida = input("Ingrese no para seguir ingresando datos de cuentas o si para salir -->\n")
    if salida == "si":
        condicion = False

obtenerMensajefinal(contador)
