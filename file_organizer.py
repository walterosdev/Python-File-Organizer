#importar Libraries
from pathlib import Path
import shutil
# Definimos las categorías de archivos centralizadas
FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg", ".gif", ".bmp", ".webp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".xls", ".xlsx", ".csv", ".json"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".bat", ".sh", ".py"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "CAD": [".dwg", ".dxf", ".rvt", ".rfa", ".skp", ".3dm", ".ifc", ".nwc", ".nwd", ".ifb", ".shx", ".shp", ".qmd", ".cpg", ".dbf", ".sh", ".prj", ".mdf", ".ldb", ".mdf.lock", ".ldb.lock"],
    "Others": [] # Se manejará por defecto si no encaja en otra
}

class FileOrganizer:
    def __init__(self, source_folder: str):
        # Usamos Pathlib para manejar rutas de forma independiente del S.O.
        self.source_folder = Path(source_folder)

    def organize_files(self):
        if not self.source_folder.exists() or not self.source_folder.is_dir():
            print("Error: Carpeta no encontrada o no es un directorio válido.")
            return

        # 1. Crear carpetas para cada categoría si no existen
        for category in FILE_TYPES.keys():
            folder_path = self.source_folder / category
            folder_path.mkdir(exist_ok=True)

        # 2. Recorrer y mover archivos
        for file_path in self.source_folder.iterdir():
            if file_path.is_file():
                file_extension = file_path.suffix.lower()
                moved = False

                for category, extensions in FILE_TYPES.items():
                    if file_extension in extensions:
                        dest_folder = self.source_folder / category
                        try:
                            shutil.move(str(file_path), str(dest_folder / file_path.name))
                            print(f"Movido: {file_path.name} -> {category}")
                        except Exception as e:
                            print(f"No se pudo mover {file_path.name}: {e}")
                        moved = True
                        break
                
                # Si no cayó en ninguna categoría conocida, va a "Others"
                if not moved and FILE_TYPES["Others"] is not None:
                    dest_folder = self.source_folder / "Others"
                    try:
                        shutil.move(str(file_path), str(dest_folder / file_path.name))
                        print(f"Movido: {file_path.name} -> Others")
                    except Exception as e:
                        print(f"No se pudo mover {file_path.name}: {e}")

        print("¡Archivos organizados exitosamente!")

if __name__ == "__main__":
    # Ajusta esta ruta según tu sistema operativo real (Ej: r"D:\Descargas" para Windows)
    directory_to_organize = r"/mnt/d/HP/Downloads" 
    
    organizer = FileOrganizer(directory_to_organize)
    organizer.organize_files()