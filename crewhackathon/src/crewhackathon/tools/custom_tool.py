from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

from ..config import Variable

class EstimarPrecioInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Observar cuanto aumenta o disminuye el precio despues de disminuir o aumentar la produccion.")

class EstimarPrecio(BaseTool):
    name: str = "EstimarPrecio"
    description: str = (
        "Estimar como quedan los precios de los autos tras aumentar o disminuir la producción"
    )
    args_schema: Type[BaseModel] = EstimarPrecioInput

    def _run(self, argument: str) -> str:
        Lista = Variable.topic.split(" ")
        entero = int(Lista[2])
        palabras = "".join(Lista[0:2]).lower()
        if palabras=="aumentar produccion":
            precio_nuevo=85000000*(1-(0.003*entero))
            return (f"Tomando como promedio un auto de 85 millones de pesos,si se aumenta la produccion un {entero}%, entonces el nuevo precio por auto es de {precio_nuevo} millones de pesos")
        elif palabras=="disminuir produccion":
            precio_nuevo=85000000*(1+(0.003*entero))
            return (
                f"Tomando como promedio un auto de 85 millones de pesos,si se disminuye la produccion un {entero}%, entonces el nuevo precio por auto es de {precio_nuevo} millones de pesos")


