# Quantitative Trading Analysis

Este repositorio contiene material de análisis cuantitativo aplicado al trading. Se incluyen notebooks de Jupyter y scripts en Python enfocados en el desarrollo de estrategias algorítmicas de inversión, análisis estadístico, y backtesting. Los principales componentes son:

- **Jupyter Notebooks**: Implementación de estrategias de trading.
- **Python Scripts**: Herramientas para análisis y simulación.
- **Documentación**: Referencias bibliográficas y notas explicativas.

## Requisitos

- Python 3.x
- Paquetes: numpy, pandas, matplotlib, y otros incluidos en `requirements.txt`.

Contribuciones y mejoras son bienvenidas.

Estoy trabajando con un entorno virtual:

Primero de todo descargar [BuildTools](https://visualstudio.microsoft.com/es/visual-cpp-build-tools/)
https://github.com/cgohlke/talib-build/releases

Si no deja instalar la dependencia "zipline" del entorno, lo mejor es bajar un [whl](https://github.com/cgohlke/talib-build) y compilarlo:

python -m venv quant-env
.\quant-env\Scripts\Activate

pip install zipline-reloaded
pip install pandas_ta
pip install setuptools
pip install openpyxl
pip install scipy
pip install scikit-learn