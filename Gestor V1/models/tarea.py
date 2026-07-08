class Tarea:
    def __init__(self, titulo, estado="Pendiente"):
        self.titulo = titulo
        self.estado = estado

    def completar(self):
        self.estado = "Completada"