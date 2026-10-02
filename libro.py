class Libro:
    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponible = True

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def isbn(self):
        return self._isbn

    @property
    def disponible(self):
        # Solo lectura: no hay setter, así que asignar lanza AttributeError
        return self._disponible

    def prestar(self):
        if not self._disponible:
            raise ValueError(f"El libro '{self._titulo}' ya está prestado")
        self._disponible = False

    def devolver(self):
        if self._disponible:
            raise ValueError(f"El libro '{self._titulo}' no está prestado")
        self._disponible = True

    def __str__(self):
        estado = "Disponible" if self._disponible else "Prestado"
        return f"[{self._isbn}] {self._titulo} - {self._autor} ({estado})"
