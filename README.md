# Sistema_Multiagentes-Hackathon
## Explicación técnica del problema y el papel de los agentes inteligentes

### Descripción del problema

El sistema simula un escenario económico en el que una empresa de autos ficticia, **'Unautos'**, debe tomar decisiones estratégicas sobre su producción y precios. Estas decisiones afectan directamente a tres sectores clave: el **consumidor**,el **Estado** y los **Inversores**.

Cada decisión impacta el equilibrio entre oferta, demanda y regulación económica. El reto consiste en evaluar estas decisiones desde distintas perspectivas para predecir reacciones del mercado (consumidor, estado e inversores) y tomar decisiones con base a datos fundamentados.

---

### Rol de los agentes inteligentes

El sistema utiliza una arquitectura de **sistema multiagente**, donde cada agente representa a un sector con objetivos, información y criterios distintos:

- **Agente Empresa (Unautos)**  
  Decide aumentar o reducir precios, producción o personal. Su objetivo es maximizar beneficios y mantener liderazgo.

- **Agente Consumidor**  
  Evalúa si seguir comprando según las decisiones de Unautos. Analiza impacto en su presupuesto, calidad y disponibilidad del producto.

- **Agente Estado**  
  Determina si debe intervenir (por ejemplo, ajustando impuestos) en función de las decisiones empresariales. Busca mantener estabilidad económica y equidad.
  
- **Agente Inversores**
  Determinan si es viable seguir aportando capital a la empresa **Unautos**.
---

### Cómo contribuyen los agentes a la solución

Cada agente procesa información específica mediante tareas definidas. Estas tareas usan modelos de lenguaje que simulan razonamiento humano para:

- Predecir consecuencias de decisiones económicas.
- Emitir juicios desde la perspectiva del consumidor y del Estado.
- Generar salidas textuales que se pueden evaluar o integrar a sistemas más amplios de simulación o análisis.

Esta colaboración inteligente permite anticipar conflictos, evaluar escenarios y tomar decisiones más informadas, todo dentro de un entorno automatizado, flexible y replicable.
