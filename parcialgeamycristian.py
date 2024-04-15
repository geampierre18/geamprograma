class parcialgeampierrecristian:
    def __init__(self):
        self.personas = []
        self.universidades = []

    def datos_de_la_persona(self):
        while True:
            print("=" * 18)
            print("datos")
            print("agregar persona")
            print("listar personas")
            print("eliminar persona")
            print("volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_persona()
            elif opcion == "2":
                self.listar_personas()
            elif opcion == "3":
                self.eliminar_persona()
            elif opcion == "4":
                break
            else:
                print("incorrecto. Intente de nuevo.")
        def agregar_persona(self):
        nombre = input("ingrese el nombre de la persona: ")
        apellido = input("ingrese el apellido de la persona: ")
        cedula = input("ingrese el número de cédula de la persona: ")
        edad = input("ingrese la edad de la persona: ")
        correo = input("ingrese el correo electrónico de la persona: ")

        persona = {
            "nombre": nombre,
            "apellido": apellido,
            "cedula": cedula,
            "edad": edad,
            "correo": correo
        }
        self.personas.append(persona)
        print("Persona agregada exitosamente.")

    def listar_personas(self):
        if not self.personas:
            print("No hay personas registradas.")
        else:
            print("Listado de personas:")
            for persona in self.personas:
                print(f"Nombre: {persona['nombre']} {persona['apellido']}")
                print(f"Cédula: {persona['cedula']}")
                print(f"Edad: {persona['edad']}")
                print(f"Correo: {persona['correo']}")
                print("-" * 18)

    def eliminar_persona(self):
        if not self.personas:
            print("No hay personas registradas para eliminar.")
            return

        cedula = input("ingrese el número de cédula de la persona a eliminar: ")
        personas_filtradas = [persona for persona in self.personas if persona['cedula'] != cedula]

        if len(personas_filtradas) == len(self.personas):
            print(f"No se encontró a la persona con la cédula {cedula}.")
        else:
            self.personas = personas_filtradas
            print(f"Persona con cédula {cedula} eliminada correctamente.")

    def gestionar_universidades(self):
        while True:
            print("=" * 18)
            print("GESTIÓN DE UNIVERSIDADES")
            print("Agregar universidad")
            print("Listar universidades")
            print("Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_universidad()
            elif opcion == "2":
                self.listar_universidades()
            elif opcion == "3":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def agregar_universidad(self):
        nombre = input("ingrese el nombre de la universidad: ")
        siglas = input("ingrese las siglas de la universidad (2 letras): ").upper()

        universidad = {
            "nombre": nombre,
            "siglas": siglas
        }
        self.universidades.append(universidad)
        print("Universidad agregada exitosamente.")

    def listar_universidades(self):
        if not self.universidades:
            print("No hay universidades registradas.")
        else:
            print("Listado de universidades:")
            for universidad in self.universidades:
                print(f"Nombre: {universidad['nombre']}")
                print(f"Siglas: {universidad['siglas']}")
                print("-" * 18)

    def eliminar_datos(self):
        confirmacion = input("si hacesesto se eliminara la informacion (S/N): ")
        if confirmacion.lower() == 's':
            self.personas = []
            self.universidades = []
            print("Todos los datos ingresados han sido eliminados.")
        else:
            print("Operación cancelada.")

    def iniciar(self):
        while True:
            print("=" * 30)
            print("PARCIAL GEAMPIERRE Y CRISTIAN")
            print("Datos de la persona")
            print("Gestionar universidades")
            print("Eliminar todos los datos")
            print("Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.datos_de_la_persona()
            elif opcion == "2":
                self.gestionar_universidades()
            elif opcion == "3":
                self.eliminar_datos()
            elif opcion == "4":
                print(" adios")
                break
            else:
                print("Opción no válida, intenta de nuevo.")
if __name__ == "__main__":
    parcial = parcialgeampierrecristian()
    parcial.iniciar()
