class Tarea:
    def __init__(self, titulo, estado="Pendiente"):
        self.titulo = titulo
        self.estado = estado

    def completar(self):
        self.estado = "Completada"

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "estado": self.estado
        }