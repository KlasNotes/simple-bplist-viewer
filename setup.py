import sys
from cx_Freeze import setup, Executable

# This tells cx_Freeze what to include
build_exe_options = {
    "packages": ["os", "PySide6"],
    "excludes": [],
}

# This keeps the black terminal window from popping up on Windows
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
            shortcut_name="bPlist Viewer",
            shortcut_dir="DesktopFolder"
        )
    ],
)