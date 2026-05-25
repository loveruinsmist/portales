while True:
    print("Conversor de cordenadas de portales")
    print("1. Nether a Overworld")
    print("2. Overworld a Nether")
    print("3. Salir")

    opc = str(input("Seleccione una opción: "))

         if opc == "1":
            x = float(input("Ingrese la coordenada X del portal en el Nether: "))
            z = float(input("Ingrese la coordenada Z del portal en el Nether: "))

            x_overworld = x * 8
            z_overworld = z * 8

            print(f"Las coordenadas del portal en el Overworld son: X: {x_overworld}, Z: {z_overworld}")

        elif opc == "2":
            x = float(input("Ingrese la coordenada X del portal en el Overworld: "))
            z = float(input("Ingrese la coordenada Z del portal en el Overworld: "))

            x_nether = x / 8
            z_nether = z / 8

            print(f"Las coordenadas del portal en el Nether son: X: {x_nether}, Z: {z_nether}")

        elif opc == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción valida.")
