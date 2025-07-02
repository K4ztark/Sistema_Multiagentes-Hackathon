from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class EstimarPrecioInput(BaseModel):

    argument: str = Field(..., description="Ejemplo: 'aumentar produccion 80 %'")


class EstimarPrecio(BaseTool):
    name: str = "EstimarPrecio"
    description: str = (
        "Estimar cómo quedan los precios de los autos tras aumentar o disminuir la producción"
    )
    args_schema: Type[BaseModel] = EstimarPrecioInput

    def _run(self, argument: str) -> str:
        lista=argument.strip().lower().split(" ")

        if len(lista) < 3:
            return "Error: el input debe tener el formato 'aumentar produccion 80 %'"

        palabras="".join(lista[0:2])
        porcentaje=int(lista[2])

        if palabras == "aumentarproduccion":
            precio_nuevo = 85000000 * (1-(0.003*porcentaje))
            return f"Si se aumenta la producción un {porcentaje}%, el nuevo precio del auto será de {precio_nuevo} pesos."

        elif palabras == "disminuirproduccion":
            precio_nuevo=85000000*(1+(0.003*porcentaje))
            return f"Si se disminuye la producción un {porcentaje}%, el nuevo precio del auto será de {precio_nuevo} pesos."

        return "Error: la acción debe ser 'aumentar produccion' o 'disminuir produccion'."

