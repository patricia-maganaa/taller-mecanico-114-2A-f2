# La clase Vehiculo representa el molde (plantilla) base para crear objetos vehículo.
# Declaración de atributos con sus tipos.
class Vehiculo:
    __patente: str
    __anio: int
    __en_taller: bool

    # Constructor que inicializa una nueva instancia de la clase Vehiculo
    def __init__(self, patente: str, anio: int) -> None:
        # Atributo privado encapsulado con doble guión bajo
        self.__patente: str = patente
        # Atributo privado encapsulado con doble guión bajo
        self.__anio: int = anio
        # Inicializa siempre en False ya que un vehículo recién registrado no parte dentro del taller
        self.__en_taller: bool = False

    # Método para ingresar el vehículo al taller
    def ingresar(self) -> None:
        self.__en_taller = True

    # Método para entregar el vehículo (sale del taller)
    def entregar(self) -> None:
        self.__en_taller = False

    @property
    def patente(self) -> str:
        return self.__patente

    @property
    def anio(self) -> int:
        return self.__anio

    @property
    def en_taller(self) -> bool:
        return self.__en_taller

    # Métodos alternativos por compatibilidad
    def obtener_patente(self) -> str:
        return self.patente

    def obtener_anio(self) -> int:
        return self.anio

    def esta_en_taller(self) -> bool:
        return self.en_taller
