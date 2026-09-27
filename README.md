# 📁 Python File Organizer

Una aplicación de escritorio desarrollada con **Python** y **PyQt5** que organiza automáticamente los archivos de una carpeta en subcarpetas según su tipo (imágenes, documentos, videos, etc.).

## ✨ Características

- Interfaz gráfica intuitiva con **PyQt5**
- Organización automática de archivos por categorías:
  - 🖼️ **Images** — `.jpg`, `.png`, `.jpeg`, `.gif`, `.bmp`, `.webp`, `.svg`
  - 📄 **Documents** — `.pdf`, `.doc`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.csv`, `.json`, etc.
  - 🗜️ **Archives** — `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
  - ⚙️ **Executables** — `.exe`, `.msi`, `.bat`, `.sh`, `.py`
  - 🎵 **Music** — `.mp3`, `.wav`, `.aac`, `.flac`
  - 🎬 **Videos** — `.mp4`, `.avi`, `.mkv`, `.mov`
  - 📐 **CAD** — `.dwg`, `.dxf`, `.rvt`, `.rfa`, `.skp`, `.ifc`, etc.
  - 📦 **Others** — Cualquier archivo que no encaje en las categorías anteriores
- Selector visual de carpetas
- Mensajes de confirmación y error

## 🚀 Requisitos previos

- Python 3.8 o superior
- pip

## 📦 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/python_file_organizer.git
cd python_file_organizer
```

2. (Opcional) Crea y activa un entorno virtual:

```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/macOS:
source venv/bin/activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## ▶️ Uso

Ejecuta la aplicación con:

```bash
python pyqt.py
```

1. Haz clic en **Examinar** para seleccionar la carpeta que deseas organizar.
2. Haz clic en **Organizar** para mover los archivos a sus subcarpetas correspondientes.
3. Haz clic en **Salir** para cerrar la aplicación.

## ⚠️ Nota para entornos WSL (Windows Subsystem for Linux)

Si ejecutas la aplicación desde un entorno de desarrollo en **WSL**, es posible que la interfaz gráfica no se inicie correctamente. Para solucionarlo, es necesario establecer la variable de entorno `QT_QPA_PLATFORM` antes de ejecutar el script:

```bash
export QT_QPA_PLATFORM=wayland
python pyqt.py
```

O bien, puedes ejecutarlo en una sola línea:

```bash
QT_QPA_PLATFORM=wayland python pyqt.py
```

> **Requisito adicional:** Asegúrate de tener un servidor de display compatible (como **VcXsrv** o **WSLg**) correctamente configurado en tu sistema Windows.

---

## 🗂️ Estructura del proyecto

```
python_file_organizer/
├── pyqt.py            # Interfaz gráfica (PyQt5)
├── file_organizer.py  # Lógica de organización de archivos
├── requirements.txt   # Dependencias del proyecto
├── .gitignore         # Archivos ignorados por Git
└── README.md          # Documentación del proyecto
```

## 🛠️ Tecnologías utilizadas

- [Python](https://www.python.org/) — Lenguaje principal
- [PyQt5](https://pypi.org/project/PyQt5/) — Framework de interfaz gráfica
- [pathlib](https://docs.python.org/3/library/pathlib.html) — Manejo de rutas multiplataforma
- [shutil](https://docs.python.org/3/library/shutil.html) — Operaciones de archivos

## 📝 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
