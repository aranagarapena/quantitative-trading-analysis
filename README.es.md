# 📊 Quantitative Trading Analysis

Bienvenido a **Quantitative Trading Analysis**, un repositorio dedicado al análisis cuantitativo aplicado al trading. Aquí encontrarás material para el desarrollo de estrategias algorítmicas, análisis estadístico, y backtesting.

## 📁 Contenido del Repositorio

Este repositorio contiene tres componentes principales:

- **Jupyter Notebooks**: Implementaciones de estrategias de trading que puedes ejecutar y modificar.
- **Python Scripts**: Herramientas en Python para análisis y simulación.
- **Documentación**: Referencias bibliográficas y notas explicativas que ayudan a entender los métodos y teorías aplicadas.

## 🚀 Configuración del Entorno de Trabajo

Para facilitar la configuración de un entorno de trabajo consistente, he incluido un script de configuración (`setup_env.py`) que crea un entorno virtual con todas las dependencias necesarias.

### Requisitos Previos

1. **Python 3.x** instalado en tu sistema.
2. **Paquetes necesarios**: especificados en `requirements.txt`. 

### Preparación y Ejecución del Entorno Virtual

1. **Instalar Herramientas de Compilación (Windows)**:
   - Antes de ejecutar el script, es recomendable descargar e instalar [BuildTools](https://visualstudio.microsoft.com/es/visual-cpp-build-tools/) para evitar problemas con algunas dependencias.
   
2. **Compilar Dependencias Opcionales**:
   - Si encuentras problemas para instalar la dependencia `zipline`, te recomendamos descargar el archivo `.whl` desde [aquí](https://github.com/cgohlke/talib-build) y compilarlo.

3. **Crear y Activar el Entorno Virtual**:
   - Ejecuta el siguiente comando en la terminal desde el directorio del proyecto:

     ```bash
     python setup_env.py
     ```

   - Este comando creará el entorno virtual `venv-quant` e instalará todas las dependencias de `requirements.txt`. Puedes cambiar el nombre del entorno virtual en el propio archivo si así lo prefieres.

4. **Mensaje de Confirmación**:
   - Si todo se ejecuta correctamente, deberías ver el mensaje:
     ```
     Dependencias instaladas correctamente.
     ```

5. **Activar el Entorno Virtual**:
   - Una vez creado el entorno tenemos que activarlo desde la terminalo con el siguiente comando:

     ```bash
     venv-quant\Scripts\activate  # En Windows
     # o
     source venv-quant/bin/activate  # En Linux/Mac
     ```

   - Al activarlo, verás `(venv-quant)` al inicio de la línea de tu terminal, indicando que estás trabajando en el entorno virtual correcto.
6. **Usar el venv como kernel en archivos .ipynb**
   - Instala `ipykernel` con el comando de más abajo. Esto permite que tu entorno virtual sea registrado como un kernel disponible para Jupyter Notebooks.
   
      ```
      pip install ipykernel
      ```
7. **Selecciona el Entorno Virtual como Kernel en el Notebook de Jupyter**
   - Abre el archivo `.ipynb` en VSCode.
   - En la parte superior derecha del notebook, verás una opción que dice "Select Kernel" o "Python: [Interprete actual]".
   - Haz clic en esta opción y selecciona tu entorno virtual `venv-quant` en la lista de intérpretes.
8. **Verifica que el Kernel Activo sea el Correcto**
   - Para confirmar que estás usando el entorno `venv-quant`, ejecuta la siguiente celda en tu notebook:
   ```
   import sys
   print(sys.executable)
   ```

   La salida debería mostrar la ruta de tu entorno virtual (venv-quant). Si ves esa ruta, significa que el entorno virtual está activado correctamente en Jupyter Notebooks dentro de VSCode.


python
Copiar código
 








## 💡 Notas Adicionales

- **Actualizar Dependencias**: Si necesitas añadir más paquetes, agrégalos a `requirements.txt` y vuelve a ejecutar el script `setup_env.py`.
- **Si tienes problemas al importar `import pandas_ta as ta`**: ejecuta ```pip install -U git+https://github.com/twopirllc/pandas-ta```. Si el problema persiste acude a la [documentación original](https://github.com/twopirllc/pandas-ta?tab=readme-ov-file#features)
- **Contribuciones**: Mejoras, sugerencias y contribuciones son bienvenidas.


Este `README.md` debería ayudarte a configurar y empezar rápidamente con el análisis cuantitativo de trading. ¡Buena suerte con tus investigaciones y estrategias! 📈

---


## 👨‍💻 Desarrollador

Este proyecto fue desarrollado y es mantenido por:

- **Iker Arana**
- [LinkedIn](https://www.linkedin.com/in/iker-arana-0ab741a6/) | [GitHub](https://github.com/aranagarapena?tab=repositories)

Para consultas, sugerencias o colaboración en el proyecto, no dudes en ponerte en contacto.

