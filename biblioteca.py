class Biblioteca:
    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = {}  # isbn -> Libro
        self._socios = {}  # dni  -> Socio

    @property
    def nombre(self):
        return self._nombre

    def agregar_libro(self, libro):
        if libro.isbn in self._libros:
            raise ValueError(f"Ya existe un libro con ISBN {libro.isbn}")
        self._libros[libro.isbn] = libro

    def registrar_socio(self, socio):
        if socio.dni in self._socios:
            raise ValueError(f"Ya existe un socio con DNI {socio.dni}")
        self._socios[socio.dni] = socio

    def _buscar(self, isbn, dni):
        if isbn not in self._libros:
            raise ValueError(f"No existe un libro con ISBN {isbn}")
        if dni not in self._socios:
            raise ValueError(f"No existe un socio con DNI {dni}")
        return self._libros[isbn], self._socios[dni]

    def prestar(self, isbn, dni):
        libro, socio = self._buscar(isbn, dni)
        # Primero se valida TODO y recién después se modifica,
        # así un préstamo fallido no deja nada a medio hacer.
        if not libro.disponible:
            raise ValueError(f"El libro '{libro.titulo}' no está disponible")
        if not socio.puede_pedir():
            raise ValueError(f"{socio.nombre} ya llegó al máximo de libros")
        libro.prestar()
        socio.agregar_libro(libro)

    def devolver(self, isbn, dni):
        libro, socio = self._buscar(isbn, dni)
        socio.quitar_libro(libro)  # lanza ValueError si el socio no lo tiene
        libro.devolver()

    def libros_disponibles(self):
        return [libro for libro in self._libros.values() if libro.disponible]

    def __str__(self):
        return (
            f"{self._nombre}: {len(self._libros)} libro(s), "
            f"{len(self._socios)} socio(s)"
        )
