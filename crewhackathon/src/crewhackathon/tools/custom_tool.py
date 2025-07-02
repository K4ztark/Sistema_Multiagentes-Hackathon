from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class EstimarPrecioInput(BaseModel):

    argument: str = Field(..., description="Ejemplo: 'aumentar produccion 80 %, o disminuir produccion 70 %'")

class EstimarPrecio(BaseTool):
    name: str = "EstimarPrecio"
    description: str = (
        "Estimar cómo quedan los precios de los autos tras aumentar o disminuir la producción"
    )
    args_schema: Type[BaseModel] = EstimarPrecioInput

    def _run(self, argument: str) -> str:
        lista=argument.strip().lower().split(" ")

        if len(lista) < 3:
            return "Error: el input debe tener el formato 'aumentar produccion n %'"

        palabras="".join(lista[0:2])
        porcentaje=int((lista[2]).replace("%",""))

        if palabras == "aumentarproduccion":
            precio_nuevo = 85000000 * (1-(0.003*porcentaje))
            return f"Si se aumenta la producción un {porcentaje}%, el nuevo precio del auto será de {precio_nuevo} pesos."

        elif palabras == "disminuirproduccion":
            precio_nuevo=85000000*(1+(0.003*porcentaje))
            return f"Si se disminuye la producción un {porcentaje}%, el nuevo precio del auto será de {precio_nuevo} pesos."

        return "Error: la acción debe ser 'aumentar produccion' o 'disminuir produccion'."

class EstimarProduccionInput(BaseModel):
    argument : str = Field(..., description="Ejemplo: 'aumentar precio 80 %, o disminuir precio 70 %'")
class EstimarProduccion(BaseTool):
    name: str = "EstimarProduccion"
    description: str = (
        "Estimar como queda la producción de los autos tras aumentar o disminuir el presupuesto"
    )
    args_schema: Type[BaseModel] = EstimarProduccionInput

    def _run(self, argument: str) -> str:
        lista2 =argument.strip().lower().split(" ")
        if len(lista2) < 3:
            return "Error: el input debe tener el formato 'aumentar precio n %'"
        palabras2="".join(lista2[0:2])
        porcentaje2=int((lista2[2]).replace("%",""))

        if palabras2 == "aumentarprecio":
            produccion_nueva=100000*(1+(0.0045*porcentaje2))
            return f"Si se aumenta el presupuesto de producción un {porcentaje2}%, la producción nueva de autos seria de {produccion_nueva} autos por semestre"
        elif palabras2 == "disminuirproduccion":
            produccion_nueva=100000*(1-(0.0045*porcentaje2))
            return f"Si se disminuye el presupuesto de producción un {porcentaje2}%, la producción nueva de autos seria de {produccion_nueva} autos por semestre"
