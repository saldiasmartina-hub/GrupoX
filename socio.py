class Socio:
    MAX_LIBROS = 3  # atributo de clase: el límite vale para todos los socios

    def __init__(self, nombre, dni):
        self._nombre = nombre
        self._dni = dni
        self._libros = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def dni(self):
        return self._dni

    @property
    def libros(self):
        # Devuelve una copia para que no modifiquen la lista interna desde afuera
        return list(self._libros)

    def puede_pedir(self):
        return len(self._libros) < Socio.MAX_LIBROS

    def agregar_libro(self, libro):
        if not self.puede_pedir():
            raise ValueError(
                f"{self._nombre} ya tiene el máximo de {Socio.MAX_LIBROS} libros"
            )
        self._libros.append(libro)

    def quitar_libro(self, libro):
        if libro not in self._libros:
            raise ValueError(f"{self._nombre} no tiene ese libro")
        self._libros.remove(libro)

    def __str__(self):
        return (
            f"{self._nombre} (DNI {self._dni}) - "
            f"{len(self._libros)} libro(s) prestado(s)"
        )
