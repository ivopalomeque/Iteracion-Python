lenguajes = ["Python", "Java", "C++", "C#", "JavaScript", "Typescript", "PHP"]
sistemas_operativos = ["Windows", "Linux", "Mac", "Android", "IOS"]
stack_tecnologicos = ["Angular", "React", "Vue", "Flutter", "Express", "Laravel"]

while True:
    print("1. Visualizar lenguajes de programación")
    print("2. Visualizar sistemas operativos")
    print("3. Visualizar Stack Tecnológicos")
    print("0. Salir")
    print("---------------------------------------")

    opcion = int(input("Seleccione una opción: "))
    listaSeleccionada = []

    if opcion == 1:
        listaSeleccionada = lenguajes
    elif opcion == 2:
        listaSeleccionada = sistemas_operativos
    elif opcion == 3:
        listaSeleccionada = stack_tecnologicos
    elif opcion == 0:
        break
    else:
        print("Opción no válida")
        print("---------------------------------------")
        continue
    for item in listaSeleccionada:
        print(item)
    print("---------------------------------------")