import sys
import plistlib
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QPushButton, QFileDialog, QTextEdit, QLabel)
from PySide6.QtCore import Qt

class PlistViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Binary .plist Viewer (PySide6)")
        self.setGeometry(200, 200, 700, 500)

        # Set up the layout
        self.layout = QVBoxLayout()

        # Instructions Label
        self.label = QLabel("Open a binary or XML .plist file to view its contents:")
        self.layout.addWidget(self.label)

        # Open Button
        self.open_button = QPushButton("Open .plist File", self)
        self.open_button.clicked.connect(self.open_file)
        self.layout.addWidget(self.open_button)

        # Display Area
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)  # Keep it as a viewer
        self.text_edit.setPlaceholderText("Data will appear here...")
        self.layout.addWidget(self.text_edit)

        self.setLayout(self.layout)

    def open_file(self):
        # PySide6 returns a tuple: (file_path, selected_filter)
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Open .plist File", 
            "", 
            "Property List Files (*.plist);;All Files (*)"
        )

        if file_path:
            self.load_plist(file_path)

    def load_plist(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                # plistlib automatically detects if it is Binary or XML
                plist_data = plistlib.load(f)

            # Use recursive formatting for better readability
            formatted_text = self.format_data(plist_data)
            self.text_edit.setPlainText(formatted_text)
            self.label.setText(f"Viewing: {file_path.split('/')[-1]}")

        except Exception as e:
            self.text_edit.setPlainText(f"Error: Could not parse file.\n{str(e)}")

    def format_data(self, data, indent=0):
        """Recursively formats dictionaries and lists for the text display."""
        lines = []
        gap = "    " * indent
        
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    lines.append(f"{gap}{key}:")
                    lines.append(self.format_data(value, indent + 1))
                else:
                    lines.append(f"{gap}{key}: {value}")
        elif isinstance(data, list):
            for i, item in enumerate(data):
                if isinstance(item, (dict, list)):
                    lines.append(f"{gap}[{i}]:")
                    lines.append(self.format_data(item, indent + 1))
                else:
                    lines.append(f"{gap}[{i}]: {item}")
        else:
            return f"{gap}{data}"
            
        return "\n".join(lines)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = PlistViewer()
    viewer.show()
    # In PySide6, it's .exec(), NOT .exec_()
    sys.exit(app.exec())