from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class CustomPopups(QDialog):
    def __init__(self, message, title="Need a hint?", parent=None):
        super().__init__(parent)

        self.setWindowTitle(title)
        self.setWindowFlags(Qt.WindowType.Popup)


        layout = QVBoxLayout()
        message = QLabel(message)
        layout.addWidget(message)
        self.setLayout(layout)