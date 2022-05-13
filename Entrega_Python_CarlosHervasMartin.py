
class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def infoAlumno(self):
        if self.nota >= 5:
            print(f"El alumno: {self.nombre}, tiene una nota de: {self.nota}. Ha aprobado la asignatura.")
        elif 0 <= self.nota < 5:
            print(f"El alumno: {self.nombre}, tiene una nota de: {self.nota}. Ha suspendido la asignatura.")
        

alumno1 = Alumno("Carlos", 8)
alumno1.infoAlumno()

alumno2 = Alumno("Pepe", 3)
alumno2.infoAlumno()