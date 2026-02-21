import sys
from cx_Freeze import setup, Executable

# 1. Trimming the fat: List modules we definitely DON'T need
build_exe_options = {
    "packages": ["os"],
    "excludes": [
        "tkinter",
        "unittest",
        "email",
        "http",
        "xml",
        "pydoc",
        "PySide6.QtWebEngine",
        "PySide6.QtWebEngineCore",
        "PySide6.QtQuick",
        "PySide6.QtNetwork",
        "PySide6.QtPdf",
        "PySide6.QtMultimedia",
        "PySide6.QtVirtualKeyboard",
        "PySide6.QtDesigner",
    ],
    # 2. This zips the libraries into one file, saving a huge amount of space
    "zip_include_packages": ["PySide6", "shiboken6"],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Simple bPlist Viewer",
    version="0.1",
    description="Binary Plist Viewer for Forensics",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "binary_plist.py", 
            base=base,
            target_name="bplist-viewer.exe", # Cleaner name
            shortcut_name="bPlist Viewer",
            shortcut_dir="DesktopFolder"
        )
    ],
)