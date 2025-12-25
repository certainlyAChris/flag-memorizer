from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class CustomDialogs(QDialog):
    def __init__(self, message, title="Need a hint?",parent=None):
        super().__init__(parent)

        self.setWindowTitle(title)

        QBtn = (
            QDialogButtonBox.StandardButton.No | QDialogButtonBox.StandardButton.Yes
        )


        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel(message)
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)