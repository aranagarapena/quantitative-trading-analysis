import subprocess
import sys
from pathlib import Path
import os

def get_virtualenv_name():
    venv_path = os.environ.get('VIRTUAL_ENV', None)
    if venv_path:
        return os.path.basename(venv_path)  # Extrae solo el nombre del directorio
    return None

def in_virtualenv():
    return (hasattr(sys, 'real_prefix') or 
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix) or 
            'VIRTUAL_ENV' in os.environ)

import subprocess
import sys
from pathlib import Path

# Cambia "venv" si prefieres otro nombre
nombre_venv = "venv-quant"

# Definir el nombre del entorno virtual
venv_dir = Path(nombre_venv)  

# Paso 1: Crear el entorno virtual si no existe
if not venv_dir.exists():
    print("Creando el entorno virtual...")
    subprocess.check_call([sys.executable, "-m", "venv", str(venv_dir)])
    print("Entorno virtual creado en:", venv_dir)
else:
    print("El entorno virtual ya existe.")

# Paso 2: Instalar dependencias desde requirements.txt
requirements_file = Path("requirements.txt")
if requirements_file.is_file():
    print("Instalando dependencias desde requirements.txt...")
    pip_executable = venv_dir / "Scripts" / "pip" if sys.platform == "win32" else venv_dir / "bin" / "pip"
    subprocess.check_call([str(pip_executable), "install", "-r", str(requirements_file)])
    print("Dependencias instaladas correctamente.")
else:
    print("El archivo 'requirements.txt' no se encontró en el directorio actual.")


if in_virtualenv():
    venv_name = get_virtualenv_name()
    print(f"Estás trabajando en un entorno virtual: {venv_name}")
else:
    print("No estás en un entorno virtual.")