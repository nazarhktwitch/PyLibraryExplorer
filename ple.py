import sys
import requests
from PySide6.QtWidgets import (
    QApplication, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox, QWidget
)

class LibraryExplorer(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("PyLibrary Explorer")
        self.setGeometry(100, 100, 500, 400)

        layout = QVBoxLayout()

        self.search_label = QLabel("Search for a Python library by name:")
        layout.addWidget(self.search_label)

        self.search_input = QLineEdit()
        layout.addWidget(self.search_input)

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_library)
        layout.addWidget(self.search_button)

        self.result_list = QListWidget()
        layout.addWidget(self.result_list)

        self.version_button = QPushButton("Get Available Versions")
        self.version_button.clicked.connect(self.get_versions)
        layout.addWidget(self.version_button)

        self.setLayout(layout)

    def search_library(self):
        library_name = self.search_input.text().strip()
        if not library_name:
            QMessageBox.warning(self, "Input Error", "Please enter a library name to search.")
            return

        response = requests.get(f"https://pypi.org/pypi/{library_name}/json")
        if response.status_code == 200:
            data = response.json()
            latest_version = data.get("info", {}).get("version", "Unknown")
            self.result_list.clear()
            self.result_list.addItem(f"Library '{library_name}' is available on PyPI.")
            self.result_list.addItem(f"Latest version: {latest_version}")
        else:
            self.result_list.clear()
            self.result_list.addItem(f"Library '{library_name}' was not found on PyPI.")

    def get_versions(self):
        library_name = self.search_input.text().strip()
        if not library_name:
            QMessageBox.warning(self, "Input Error", "Please enter a library name to check versions.")
            return

        response = requests.get(f"https://pypi.org/pypi/{library_name}/json")
        if response.status_code == 200:
            data = response.json()
            releases = data.get("releases", {})
            versions = sorted(releases.keys(), reverse=True)

            if versions:
                self.result_list.clear()
                self.result_list.addItem(f"Available versions for '{library_name}':")
                for version in versions:
                    self.result_list.addItem(version)
            else:
                self.result_list.clear()
                self.result_list.addItem(f"No versions found for '{library_name}'.")
        else:
            self.result_list.clear()
            self.result_list.addItem(f"Library '{library_name}' was not found on PyPI.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    explorer = LibraryExplorer()
    explorer.show()
    sys.exit(app.exec())
