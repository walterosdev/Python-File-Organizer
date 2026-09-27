#Import Libraries
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QMessageBox, QVBoxLayout, QFileDialog
from file_organizer import FileOrganizer

#Define Class y muestra el diseño o interza iniciales en cuanto a formas,tamaños y colores
class PyQtApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App de organizacion POO")
        self.resize(500, 200)
        self.setStyleSheet(
            """
            QWidget {
                background-color: #A77F76;
            }

            QLabel {
                color: #fff;
                font-size: 16px;
                font-weight: bold;
            }

            QLineEdit {
                background-color: #444;
                color: #fff;
            }

            QPushButton {
                background-color: #555;
                color: #fff;
            }
            """
        )
        self.initUI()
    #mostrar la interfaz con los paramentros
    def initUI(self):
        layout = QHBoxLayout()
        self.label = QLabel("Carpeta:", self)
        layout.addWidget(self.label)
        self.text_field = QLineEdit()
        self.text_field.setPlaceholderText("Selecciona la ruta de la carpeta a organizar.")
        layout.addWidget(self.text_field)
        self.examine_button = QPushButton("Examinar", self)
        self.examine_button.clicked.connect(self.select_folder)
        layout.addWidget(self.examine_button)
        self.organize_button = QPushButton("Organizar", self)
        self.organize_button.clicked.connect(self.organize_folder)
        layout.addWidget(self.organize_button)

        self.quit_button = QPushButton("Salir", self)
        self.quit_button.clicked.connect(self.close)
        layout.addWidget(self.quit_button)
        self.setLayout(layout)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Selecciona una Carpeta.")
        if folder:
            self.text_field.setText(folder)
        
    
    def organize_folder(self):
        folder = self.text_field.text().strip()
        if folder:
            organizer = FileOrganizer(folder)
            result=organizer.organize_files()
            if result=="¡Archivos organizados exitosamente!":
                QMessageBox.information(self, "Exito", "Carpeta organizada exitosamente.")
            else:
                QMessageBox.warning(self, "Error", "No se pudo organizar la carpeta.")


    # def submit_action(self):
    #     user_input = self.text_field.text().strip()
    #     if user_input:
    #         QMessageBox.information(self, "Saludo", f"Hola {user_input}!, Bienvenido a mi app")
    #     else:
    #         QMessageBox.warning(self, "Error", "Por favor, ingresa tu nombre.")
    

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = PyQtApp()
    window.show()
    sys.exit(app.exec_())