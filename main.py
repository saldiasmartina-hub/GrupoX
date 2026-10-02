from libro import Libro
from socio import Socio
from biblioteca import Biblioteca


def demo():
    bib = Biblioteca("Biblioteca POO")
    bib.agregar_libro(Libro("Rayuela", "Cortázar", "978-1"))
    bib.agregar_libro(Libro("Ficciones", "Borges", "978-2"))
    bib.agregar_libro(Libro("El túnel", "Sabato", "978-3"))
    ana = Socio("Ana", "30111222")
    bib.registrar_socio(ana)
    print(bib)

    print("\n--- Ana pide Rayuela ---")
    bib.prestar("978-1", "30111222")
    print(ana)
    print("Disponibles:")
    for libro in bib.libros_disponibles():
        print("  ", libro)

    print("\n--- Otro préstamo de Rayuela (debe fallar) ---")
    try:
        bib.prestar("978-1", "30111222")
    except ValueError as e:
        print("Error:", e)

    print("\n--- Ana devuelve Rayuela ---")
    bib.devolver("978-1", "30111222")
    print(ana)
    print("Cantidad de disponibles:", len(bib.libros_disponibles()))


def probar(condicion, mensaje):
    assert condicion, mensaje


def debe_fallar(funcion, mensaje):
    try:
        funcion()
    except ValueError:
        return
    probar(False, mensaje)


def pruebas():
    # --- Libro ---
    l = Libro("T", "A", "I1")
    probar(l.disponible, "Un libro nuevo debe estar disponible")
    l.prestar()
    probar(not l.disponible, "prestar() no marca el libro como prestado")
    debe_fallar(l.prestar, "No se puede prestar un libro ya prestado")
    l.devolver()
    probar(l.disponible, "devolver() no marca el libro como disponible")
    debe_fallar(l.devolver, "No se puede devolver un libro que no está prestado")
    probar("I1" in str(l) and "T" in str(l), "__str__ debe mostrar ISBN y título")
    try:
        l.disponible = False
        probar(False, "disponible debe ser una propiedad de solo lectura")
    except AttributeError:
        pass

    # --- Socio ---
    s = Socio("Test", "D1")
    probar(len(s.libros) == 0 and s.puede_pedir(), "Un socio nuevo no tiene libros y puede pedir")
    for i in range(3):
        s.agregar_libro(Libro("T", "A", f"X{i}"))
    probar(not s.puede_pedir(), "Con 3 libros el socio no puede pedir más")
    debe_fallar(lambda: s.agregar_libro(Libro("T", "A", "X9")), "No se puede superar el máximo de 3 libros")
    debe_fallar(lambda: s.quitar_libro(Libro("T", "A", "NO")), "No se puede quitar un libro que el socio no tiene")

    # --- Biblioteca ---
    b = Biblioteca("Test")
    for i in range(5):
        b.agregar_libro(Libro("T", "A", f"B{i}"))
    b.registrar_socio(Socio("S", "D1"))
    b.registrar_socio(Socio("R", "D2"))
    debe_fallar(lambda: b.agregar_libro(Libro("T", "A", "B0")), "No se permiten ISBN repetidos")
    debe_fallar(lambda: b.registrar_socio(Socio("X", "D1")), "No se permiten DNI repetidos")
    debe_fallar(lambda: b.prestar("NOEXISTE", "D1"), "prestar debe fallar si el libro no existe")
    debe_fallar(lambda: b.prestar("B0", "NOEXISTE"), "prestar debe fallar si el socio no existe")

    b.prestar("B0", "D1")
    probar(len(b.libros_disponibles()) == 4, "prestar no saca el libro de los disponibles")
    debe_fallar(lambda: b.prestar("B0", "D2"), "No se puede prestar un libro ya prestado")
    debe_fallar(lambda: b.devolver("B0", "D2"), "Un socio no puede devolver un libro que no tiene")

    b.prestar("B1", "D1")
    b.prestar("B2", "D1")
    debe_fallar(lambda: b.prestar("B3", "D1"), "Un socio con 3 libros no puede pedir otro")
    probar(len(b.libros_disponibles()) == 2, "Si el préstamo falla, el libro debe seguir disponible")

    b.devolver("B0", "D1")
    probar(len(b.libros_disponibles()) == 3, "devolver no vuelve a poner el libro como disponible")
    b.prestar("B3", "D1")  # ahora sí puede

    print("\n¡Todas las pruebas pasaron!")


if __name__ == "__main__":
    demo()
    pruebas()
