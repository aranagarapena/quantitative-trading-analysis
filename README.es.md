# 📊 Análisis Cuantitativo de Trading

Bienvenido a **Análisis Cuantitativo de Trading**, un repositorio dedicado al análisis cuantitativo aplicado al trading. Aquí encontrarás recursos para desarrollar estrategias algorítmicas, análisis estadístico y pruebas retrospectivas (*backtesting*).

## 📁 Contenido del Repositorio

Este repositorio contiene tres componentes principales:

- **Jupyter Notebooks**: Implementaciones de estrategias de trading que puedes ejecutar y modificar.
- **Scripts en Python**: Herramientas en Python para análisis y simulación.
- **Documentación**: Referencias bibliográficas y notas explicativas para comprender los métodos y teorías aplicadas.

## 🚀 Configuración del Entorno de Trabajo

Para simplificar la configuración de un entorno de trabajo consistente, se incluye un script de configuración (`setup_env.py`) que crea un entorno virtual con todas las dependencias necesarias.

### Prerrequisitos

1. **Python 3.x** instalado en tu sistema.
2. **Paquetes requeridos**: listados en `requirements.txt`.

### Preparación y Ejecución del Entorno Virtual

1. **Instalar Build Tools (Windows)**:
   - Antes de ejecutar el script, se recomienda descargar e instalar [BuildTools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) para evitar problemas con algunas dependencias.

2. **Compilar Dependencias Opcionales**:
   - Si tienes problemas instalando la dependencia `zipline`, descarga el archivo `.whl` desde [aquí](https://github.com/cgohlke/talib-build) y compílalo.

3. **Crear y Activar el Entorno Virtual**:
   - Ejecuta el siguiente comando en la terminal desde el directorio del proyecto:
     
     ```bash
     python 0_setup_env.py
     ```
   
   - Este comando creará el entorno virtual `venv-quant` e instalará todas las dependencias listadas en `requirements.txt`. Puedes renombrar el entorno virtual en el script si lo necesitas.

4. **Mensaje de Confirmación**:
   - Si la configuración se completa con éxito, deberías ver el siguiente mensaje:
     ```
     Dependencies installed successfully.
     ```
   - Es normal ver errores como estos:
     ```
     Error: zipline_reloaded not installed. No module named 'zipline_reloaded'
     Error: scikit_learn not installed. No module named 'scikit_learn'
     ipykernel installed successfully.
     ```

5. **Activar el Entorno Virtual**:
   - Una vez creado, activa el entorno con el siguiente comando en la terminal:
     
     ```bash
     venv-quant\Scripts\activate  # En Windows
     # o
     source venv-quant/bin/activate  # En Linux/Mac
     ```

   - Al activarlo, `(venv-quant)` aparecerá al inicio de la línea de la terminal, indicando que estás usando el entorno virtual.
   - Para confirmar que estás en el entorno correcto, ejecuta el script `1_confirmar_venv.py` con el siguiente comando:
     ```bash
     python 1_confirmar_venv.py
     ```
   - La salida debería ser algo similar a:
     ```
     {tu ruta de directorio}\venv-quant\Scripts\python.exe
     ```

6. **Usar el Entorno Virtual como Kernel en Archivos `.ipynb`**:
   - Instala `ipykernel` en tu entorno virtual ejecutando:
     ```bash
     pip install ipykernel
     ```
   - Reinicia VSCode.

7. **Seleccionar el Entorno Virtual como Kernel en Jupyter Notebooks**:
   - Abre tu archivo `.ipynb` en VSCode.
   - En la parte superior derecha del notebook, verás una opción llamada "Seleccionar Kernel". Haz clic y elige `venv-quant` de la lista de intérpretes.
   - Si el kernel no aparece, prueba los siguientes pasos:

   7.1. **Agregar Manualmente el Entorno Virtual a Jupyter**:
      - Activa el entorno virtual en la terminal.
      - Registra el entorno como un kernel de Jupyter:
        ```bash
        python -m ipykernel install --user --name=venv-quant --display-name "Python (venv-quant)"
        ```
      - Reinicia VSCode, abre el notebook y selecciona "Python (venv-quant)" como el kernel.

   7.2. **Verificar la Configuración en `settings.json` de VSCode**:
      - Si el problema persiste, configura manualmente el entorno virtual en el archivo `settings.json` del proyecto en VSCode:
        - Crea una carpeta llamada `.vscode` en el directorio raíz del proyecto si no existe.
        - Dentro de `.vscode`, crea (o edita) `settings.json` y agrega la siguiente configuración, ajustando la ruta según tu sistema operativo:
          ```json
          {
           "python.pythonPath": "${workspaceFolder}/venv-quant/Scripts/python"  // Para Windows
           // "python.pythonPath": "${workspaceFolder}/venv-quant/bin/python"  // Para Linux/macOS
          }
          ```
        - Reinicia VSCode para aplicar los nuevos ajustes.

8. **Verificar el Kernel Activo**:
   - Para confirmar que estás usando el entorno `venv-quant`, ejecuta la siguiente celda en tu notebook:
     ```python
     import sys
     print(sys.executable)
     ```
   - La salida debería mostrar la ruta de tu entorno virtual (`venv-quant`). Si ves esto, el entorno virtual está correctamente activado en Jupyter Notebooks dentro de VSCode.

## 💡 Notas Adicionales

- **Actualizar Dependencias**: Si necesitas agregar más paquetes, inclúyelos en `requirements.txt` y vuelve a ejecutar el script `setup_env.py`.
- **Si tienes problemas al importar `pandas-ta` con `import pandas_ta as ta`**: Es común ver errores como ``` ImportError: cannot import name 'Nan' from 'numpy'``` al instalar esta librería. Esto suele ocurrir porque la instalación no se completó correctamente. Para solucionarlo:
  - Abre una terminal con tu entorno virtual activado y ejecuta ```pip install pandas_ta``` para instalar la última versión estable. Alternativamente, instala la versión más reciente directamente desde el repositorio con ```pip install -U git+https://github.com/twopirllc/pandas-ta```.
  - Después de la instalación, reinicia el notebook utilizando el botón de reinicio ubicado en la parte superior central.
  - Asegúrate de que el kernel correcto correspondiente a tu entorno virtual esté seleccionado antes de ejecutar tu código.
  - Si el problema persiste, consulta la [documentación oficial](https://github.com/twopirllc/pandas-ta?tab=readme-ov-file#features).
- **Contribuciones**: Se aceptan mejoras, sugerencias y contribuciones.
