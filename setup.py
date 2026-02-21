import sys
import uuid
from cx_Freeze import setup, Executable

# 1. Permanent Upgrade Code (Do not change this once set)
# This allows Windows to recognize updates to the same app.
UPGRADE_CODE = "{C6B1B823-A23E-4D6B-8833-D659E79178C4}"

# 2. Refined Build Options
build_exe_options = {
    "packages": ["os", "PySide6.QtCore", "PySide6.QtGui", "PySide6.QtWidgets"],
    "excludes": [
        "tkinter", "unittest", "email", "http", "xml", "pydoc",
        "PySide6.QtWebEngine", "PySide6.QtWebEngineCore", "PySide6.QtQuick",
        "PySide6.QtNetwork", "PySide6.QtPdf", "PySide6.QtMultimedia",
        "PySide6.QtVirtualKeyboard", "PySide6.QtDesigner",
    ],
    # NOTE: We keep PySide6 out of the zip to prevent "Plugin not found" errors
    "zip_include_packages": ["shiboken6"],
    "include_msi": True,
}

# 3. MSI Specific Configuration
bdist_msi_options = {
    "upgrade_code": UPGRADE_CODE,
    "add_to_path": False,
    "initial_target_dir": r"[ProgramFilesFolder]\SimpleBPlistViewer",
    "install_icon": None, # Add a path to an .ico file here if you have one
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Simple bPlist Viewer",
    version="0.1",
    author="Your Name",
    description="Binary Plist Viewer for Forensics",
    options={
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options,
    },
    executables=[
        Executable(
            "binary_plist.py", 
            base=base,
            target_name="bplist-viewer.exe",
            shortcut_name="bPlist Viewer",
            shortcut_dir="DesktopFolder"
        )
    ],
)
