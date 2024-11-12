# Quantitative Trading Analysis

Este repositorio contiene material de análisis cuantitativo aplicado al trading. Se incluyen notebooks de Jupyter y scripts en Python enfocados en el desarrollo de estrategias algorítmicas de inversión, análisis estadístico, y backtesting. Los principales componentes son:

- **Jupyter Notebooks**: Implementación de estrategias de trading.
- **Python Scripts**: Herramientas para análisis y simulación.
- **Documentación**: Referencias bibliográficas y notas explicativas.

## Requisitos

- Python 3.x
- Paquetes: numpy, pandas, matplotlib, y otros incluidos en `requirements.txt`.

Contribuciones y mejoras son bienvenidas.

En el repo hay un script para crear un entorno viertual de trabajo con todas las dependencias instaldas, pero:
- Primero de todo recomiendo descargar [BuildTools](https://visualstudio.microsoft.com/es/visual-cpp-build-tools/) 

Durante la instalación del venv:
- Si no deja instalar la dependencia "zipline" del entorno, lo mejor es bajar un [whl](https://github.com/cgohlke/talib-build) y compilarlo:

Si ejecutas el fichero 'setup_env.py' se creará el entorno 'vev-quant'

Si se ejecuta todo correctamente debería mostrar un mensaje tipo:
_Dependencias instaladas correctamente._

Para activar el entorno virtual, ejecuta:
    python -m venv quant-env
    .\quant-env\Scripts\Activate
