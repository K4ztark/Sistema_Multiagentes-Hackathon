from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class EstimarPrecioInput(BaseModel):

    argument: str = Field(..., description="Ejemplo: 'aumentar produccion 80 %, o disminuir produccion 70 %', o aumentar produccion 4 %, o disminuir produccion 4 %")

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
    argument : str = Field(..., description="Ejemplo: 'aumentar precio 80 %, o disminuir precio 70 %, o aumentar precio 4 %, o disminuir precio 4 %'")
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
        elif palabras2 == "disminuirprecio":
            produccion_nueva=100000*(1-(0.0045*porcentaje2))
            return f"Si se disminuye el presupuesto de producción un {porcentaje2}%, la producción nueva de autos seria de {produccion_nueva} autos por semestre"

class EstimarDemandaInput(BaseModel):
    argument: str = Field(...,description="Ejemplo: 'aumentar precio 80 %, o disminuir precio 70 %, o aumentar precio 4 %, o disminuir precio 4 %'")

class EstimarDemanda(BaseTool):
    name: str = "EstimarDemanda"
    description: str = (
        "Estimar como cambia la demanda en cuestion al cambio del precio de los carros"
    )
    args_schema: Type[BaseModel] = EstimarDemandaInput

    def _run(self, argument: str) -> str:
        lista3=argument.strip().lower().split(" ")
        if len(lista3) < 3:
            return "Error: el input debe tener el formato 'aumentar/disminuir precio n %'"
        palabras3="".join(lista3[0:2])
        porcentaje3=int((lista3[2]).replace("%",""))
        if palabras3 == "aumentarprecio":
            precio_inicial=85000000
            precio_nuevo=85000000+((porcentaje3/100)*85000000)
            cambio_precio=(precio_nuevo-precio_inicial)/precio_inicial
            cambio_demanda=-0.50*cambio_precio
            demanda_nueva=4000*(1+cambio_demanda)
            return f"La demanda nueva después de aumentar el precio {porcentaje3}% es de {demanda_nueva} autos mensuales"
        elif palabras3 == "disminuirprecio":
            precio_inicial = 85000000
            precio_nuevo = 85000000 - ((porcentaje3/100)*85000000)
            cambio_precio = (precio_nuevo - precio_inicial) / precio_inicial
            cambio_demanda = -0.50 * cambio_precio   #Si el precio se disminuye cambio precio es negativo, luego cambio demanda es positivo (la demanda incrementa si el precio es menor)
            demanda_nueva = 4000 * (1 + cambio_demanda)
            return f"La demanda nueva después de disminuir el precio {porcentaje3}% es de {demanda_nueva} autos mensuales"


class InformeCompetencia(BaseTool):
    name: str = "InformeCompetencia"
    description: str = (
        "Devuelve un informe simulado sobre el comportamiento reciente de empresas competidoras del sector automotriz."
    )
    def _run(self) -> str:
        #Este es un informe ficticio (simulado) para ver como responde el agente con esta herramienta personalizada
        informe = """
            Informe de Competencia:

            - **Toyota**: Ha aumentado su producción en un 5% este trimestre debido a la alta demanda de autos híbridos.
            - **Renault**: Redujo sus precios un 7% para captar mayor cuota de mercado en LATAM.
            - **Changan**: Introdujo nuevos modelos eléctricos con precios un 9% por debajo del promedio.
            - **Chevrolet**: Está enfocando su estrategia en vehículos SUV y ha aumentado su inversión en marketing digital.

Este comportamiento puede afectar la demanda en los segmentos de autos económicos y eléctricos.
"""
        return informe

class EstimarCrecimientoInput(BaseModel):
    argument: str = Field(...,description="Ejemplo: 'aumentar precio 80 %, o disminuir precio 70 %, o aumentar precio 6 %, o disminuir precio 6 %'")

class EstimarCrecimiento(BaseTool):
    name: str = "EstimarCrecimiento"
    description: str = (
        "Devuelve el crecimiento aproximado de una empresa respecto al aumento o disminución de precios"
    )
    args_schema: Type[BaseModel] = EstimarCrecimientoInput

    def _run(self, argument: str) -> str:
        lista4 = argument.strip().lower().split(" ")
        if len(lista4) < 3:
            return "Error: el input debe tener el formato 'aumentar/disminuir precio n %'"
        palabras4 = "".join(lista4[0:2])
        porcentaje4 = int((lista4[2]).replace("%", ""))

        if palabras4 == "aumentarprecio":
            tasa_impacto=0.005
            crecimiento=1040000000000*((porcentaje4/100)*tasa_impacto) #1040000000000 es los ingresos promedios de una empresa automovilistica semestralmente.
            crecimiento_porcentaje=(crecimiento*100)/1040000000000
            return f"Después de aumentar los precios {porcentaje4}% la empresa ha crecido {crecimiento_porcentaje}%"
        elif palabras4 == "disminuirprecio":
            tasa_impacto=0.007
            crecimiento = 1040000000000 * ((porcentaje4/100) * tasa_impacto)
            crecimiento_porcentaje = (crecimiento * 100) / 1040000000000
            return f"Después de aumentar los precios {porcentaje4}% la empresa ha crecido {crecimiento_porcentaje}%"

