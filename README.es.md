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
     python 0_setup_env.py
     ```

   - Este comando creará el entorno virtual `venv-quant` e instalará todas las dependencias de `requirements.txt`. Puedes cambiar el nombre del entorno virtual en el propio archivo si así lo prefieres.

4. **Mensaje de Confirmación**:
   - Si todo se ejecuta correctamente, deberías ver el mensaje:
     ```
     Dependencias instaladas correctamente.
     ```
   - Es normal que veas un mensaje de error como este:
      ```
      Error: zipline_reloaded no se ha instalado. No module named 'zipline_reloaded'
      Error: scikit_learn no se ha instalado. No module named 'scikit_learn'      
      ipykernel instalado correctamente.
      ```
5. **Activar el Entorno Virtual**:
   - Una vez creado el entorno tenemos que activarlo y seleccionarlo desde la `terminal` con el siguiente comando:

     ```bash
     venv-quant\Scripts\activate  # En Windows
     # o
     source venv-quant/bin/activate  # En Linux/Mac
     ```

   - Al activarlo, verás `(venv-quant)` al inicio de la línea de tu terminal, indicando que estás trabajando en el entorno virtual correcto.
   - Para confirmar que se está utilizando el `venv` adicionalmente puedes ejecutar desde la `terminal` el script `1_confirmar_venv.py` utilizando el comando 
      ```
         python 1_confirmar_venv.py
      ```
   - La salida debería mostrar algo similar a :
      ```
         {nombre completo de tu directorio}\venv-quant\Scripts\python.exe
      ```
   
6. **Usar el venv como kernel en archivos .ipynb**
   - Instala `ipykernel` en tu entorno virtual desde la terminal con el comando de más abajo. Esto permite que tu entorno virtual sea registrado como un kernel disponible para Jupyter Notebooks.
   
      ```
      pip install ipykernel
      ```
   -Reinicia VSCode
7. **Selecciona el Entorno Virtual como Kernel en el Notebook de Jupyter**
   - Abre el archivo `.ipynb` en VSCode.
   - En la parte superior derecha del notebook, verás una opción que dice "Select Kernel" o "Seleccionar el kernel".
   - Haz clic en esta opción y selecciona tu entorno virtual `venv-quant` en la lista de intérpretes.
   - Si el kernel no te aparece prueba lo siguiente
  
   7.1. **Agregar el Entorno Virtual a Jupyter Manualmente**
      Si `venv-quant` sigue sin aparecer, puedes agregarlo manualmente como un kernel en Jupyter:
      - Activa el entorno virtual desde la terminal.
      - Usa el siguiente comando para registrar el entorno virtual como un kernel de Jupyter:
      ```
      python -m ipykernel install --user --name=venv-quant --display-name "Python (venv-quant)"
      ```
      - Reinicia VSCode abre el notebook y selecciona "Python (venv-quant)" como kernel.






   7.2. **Verifica la Configuración en `settings.json` de VSCode**
   Si el problema persiste, puedes configurar manualmente el entorno virtual en el archivo `settings.json` de tu proyecto en VSCode:
   - Crea una carpeta llamada .vscode en el directorio raíz de tu proyecto, si no existe.
   - Dentro de .vscode, crea (o edita) el archivo settings.json y añade esta configuración, ajustando la ruta según tu sistema operativo:
   ```
   {
    "python.pythonPath": "${workspaceFolder}/venv-quant/Scripts/python"  // Para Windows
    // "python.pythonPath": "${workspaceFolder}/venv-quant/bin/python"  // Para Linux/macOS
   }
   ```
   - Reinicia VSCode para que detecte la nueva configuración.








8. **Verifica que el Kernel Activo sea el Correcto**
   - Para confirmar que estás usando el entorno `venv-quant`, ejecuta la siguiente celda en tu notebook:
   ```
   import sys
   print(sys.executable)
   ```

   La salida debería mostrar la ruta de tu entorno virtual (venv-quant). Si ves esa ruta, significa que el entorno virtual está activado correctamente en Jupyter Notebooks dentro de VSCode.

 








## 💡 Notas Adicionales

- **Actualizar Dependencias**: Si necesitas añadir más paquetes, agrégalos a `requirements.txt` y vuelve a ejecutar el script `setup_env.py`.
- **Si tienes problemas al importar pandas-ta `import pandas_ta as ta`**: es común encontrarse con errores como ``` ImportError: cannot import name 'Nan' from 'numpy'```al instalar esta librería. Suele deberse a que la librería no se ha instalado correctamente. Te recomiendo realizar lo siguiente:
  - Abre una `terminal` con tu `venv` corriendo, y ejecuta ```pip install pandas_ta``` para instalar la última versión estable. Si quieres también puedes instalar la última versión con ```pip install -U git+https://github.com/twopirllc/pandas-ta```. 
  - Después de esto, reincia en notebook con el botón reiniciar de la parte superior central. 
  - Además de esto, comprueba que has seleccionado correctamente el Kernel de tu entorno virtual para ejecutar el código.
  - Si el problema persiste acude a la [documentación original](https://github.com/twopirllc/pandas-ta?tab=readme-ov-file#features)
- **Contribuciones**: Mejoras, sugerencias y contribuciones son bienvenidas.


Este `README.md` debería ayudarte a configurar y empezar rápidamente con el análisis cuantitativo de trading. ¡Buena suerte con tus investigaciones y estrategias! 📈

---


## 👨‍💻 Desarrollador

Este proyecto fue desarrollado y es mantenido por:

- **Iker Arana**
- [LinkedIn](https://www.linkedin.com/in/iker-arana-0ab741a6/) | [GitHub](https://github.com/aranagarapena?tab=repositories)

Para consultas, sugerencias o colaboración en el proyecto, no dudes en ponerte en contacto.

