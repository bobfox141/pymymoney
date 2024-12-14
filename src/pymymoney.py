#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QUiLoader
from PyQt5.QtWidgets import QFile
from PyQt5.QtWidgets import QIODevice

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_file_name = "../ui/pymymoney.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()
    sys.exit(app.exec())
