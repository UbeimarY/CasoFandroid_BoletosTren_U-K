import json

def informacion(nombre, edad, tarjeta, vencimiento, contraseña, puntos):
    usuario = {
        'nombre': nombre,
        'tarjeta': tarjeta,
        'vencimiento': vencimiento,
        'contraseña': contraseña,
        'edad': edad,
        'puntos': puntos
    }
    with open("datos.json", 'w') as archivo:
        json.dump(usuario, archivo)

def escritura():
    with open("datos.json", 'r') as archivo:
        base_de_datos = json.load(archivo)
        return base_de_datos

comprobante1 = ""
comprobante2 = ""
puntos = 0

while True:
    print("Bienvenido a la aplicación\n"
          "1. Registrarse\n"
          "2. Inicio de sesión\n"
          "3. Salir")
    eleccion = int(input("Seleccione una opción: "))
    
    if eleccion == 1:
        nombre = input("Digite su nombre: ")
        edad = input("Digite su edad: ")
        contraseña = input("Digite su contraseña: ")
        tarjeta = input("Digite el número de la tarjeta de crédito: ")
        vencimiento = input("Digite el vencimiento de su tarjeta de crédito: ")
        informacion(nombre, edad, tarjeta, vencimiento, contraseña, puntos)
        print("¡Registro completado! Volviendo al menú de inicio.")

    elif eleccion == 2:
        data = escritura()
        verificacion1 = data['nombre']
        verificacion2 = data['contraseña']
        while comprobante1 != verificacion1 or comprobante2 != verificacion2:
            comprobante1 = input("Por favor, digite su usuario: ")
            comprobante2 = input("Por favor, digite su contraseña: ")
            if comprobante1 != verificacion1 or comprobante2 != verificacion2:
                print("Credenciales incorrectas. Inténtelo nuevamente.")
        
        print("Inicio de sesión exitoso.")
        while True:
            print("1. Compra de aplicaciones\n"
                  "2. Canjeo de premios\n"
                  "3. Salir de sesión")
            entrada = int(input("Seleccione una opción: "))
            
            if entrada == 1:
                print("Bienvenido a la compra de aplicaciones\n"
                      "1. Bard IA - Valor: 10000 puntos\n"
                      "2. Game Console Dev - Valor: 37000 puntos\n"
                      "3. TVInfo Child - Valor: 30000 puntos\n"
                      "4. BokkShelf - Valor: 50000 puntos\n"
                      "5. GPT-15 - Valor: 100000 puntos")
                entrada1 = int(input("Seleccione una aplicación: "))
                if 1 <= entrada1 <= 5:
                    puntos += [0, 10, 20, 40, 5, 25][entrada1]
                    data['puntos'] = puntos
                    with open("datos.json", 'w') as archivo:
                        json.dump(data, archivo)
                    print("¡Felicitaciones por tu compra! Has recibido puntos de bonificación.")
                else:
                    print("Opción inválida.")

            elif entrada == 2:
                total = data['puntos']
                print("Usted tiene un total de", total, "puntos.")
                print("Opciones de canjeo:\n"
                      "1. Descuento del 10% en próxima compra - 50 puntos\n"
                      "2. Suscripción a servicio premium - 150 puntos\n"
                      "3. Acceso a contenido exclusivo - 75 puntos\n"
                      "4. Tickets gratuitos de Cine con gastos pagos - 200 Puntos\n"
                      "5. 50% de  Descuento en productos seleccionados - 150 puntos\n"
                      "6. Compras gratis por 3 días - 100 Puntos")
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1 and total >= 50:
                    puntos -= 50
                    print("¡Has canjeado un descuento del 10% en tu próxima compra!")
                elif opcion == 2 and total >= 150:
                    puntos -= 150
                    print("¡Has canjeado una suscripción a servicio premium!")
                elif opcion == 3 and total >= 75:
                    puntos -= 75
                    print("¡Has canjeado acceso a contenido exclusivo!")
                elif opcion == 4 and total >= 200:
                    puntos -= 200
                    print("¡Has canjeado Tickets gratuitos de Cine con gastos pagos!")
                elif opcion == 5 and total >= 150:
                    puntos -= 150
                    print("¡Has canjeado 50% de  Descuento en productos seleccionados!")
                elif opcion == 6 and total >= 100:
                    puntos -= 100
                    print("¡Has canjeado Compras gratis por 3 días")
                else:
                    print("No tienes suficientes puntos para canjear esta opción.")
                data['puntos'] = puntos
                with open("datos.json", 'w') as archivo:
                    json.dump(data, archivo)

            elif entrada == 3:
                print("Saliendo del modo de canjeo.")
                break
            else:
                print("Opción inválida.")

    elif eleccion == 3:
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
