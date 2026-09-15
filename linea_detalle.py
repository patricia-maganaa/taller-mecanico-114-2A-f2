# Clase LineaDetalle para representar un ítem o línea de detalle con cantidad y precio unitario.
class LineaDetalle:
    def __init__(self, cantidad: int, precio_unitario: float) -> None:
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def subtotal(self) -> float:
        return self.cantidad * self.precio_unitario
