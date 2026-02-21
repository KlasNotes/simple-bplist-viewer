# Simple bplist Viewer

A lightweight, "quick and dirty" proof-of-concept utility for forensics. This tool is designed to do one thing: rip keys and values out of an Apple binary plist (`.bplist`) and display them side-by-side. 

---

## 📥 Option 1: Easy Windows Install (Recommended)
**No Python or command-line knowledge required.** Use this for a standard Windows installation.

1. **[Download the Latest MSI Installer](https://github.com/KlasNotes/simple-bplist-viewer/releases/latest)**
2. **Run the `.msi` file** to install the app.
3. **Open the shortcut** from your Desktop.

> **Note:** Because this is an unsigned tool, Windows SmartScreen may pop up. Click **More Info** and then **Run Anyway** to finish the install.

---

## 💻 Option 2: Manual Setup (Windows, Linux, or macOS)
**For power users or auditors who want to run the source code directly.**

### 1. Get the Code
* **If you have Git:**
  ```bash
    git clone [https://github.com/KlasNotes/simple-bplist-viewer.git](https://github.com/KlasNotes/simple-bplist-viewer.git)
  ```
  ```bash
    cd simple-bplist-viewer
    ```
* **If you do NOT have Git:** Download the **ZIP file** from the green "Code" button at the top of this page, extract it, and open your terminal inside that folder.

### 2. Run the One-Liner
Copy and paste the command for your specific operating system to create a virtual environment, install dependencies, and launch the app:

**Windows (Command Prompt):**
```cmd
python -m venv venv && venv\Scripts\python -m pip install -r requirements.txt && venv\Scripts\python binary_plist.py
```
**PowerShell:**
```powershell
python -m venv venv ; venv\Scripts\python -m pip install -r requirements.txt ; venv\Scripts\python binary_plist.py
```
**Linux / macOS (Terminal):**
```cmd
python3 -m venv venv && ./venv/bin/pip install -r requirements.txt && ./venv/bin/python3 binary_plist.py
```

---

## 📖 How to Use

1. **Launch the app** using one of the methods described above.
2. **Click the "Open bplist" button** in the main interface.
3. **Select your file:** Browse to the Apple `.plist` or `.bplist` file you wish to examine.
4. **View Results:** The app parses the binary data and displays the keys and values as readable lines of text in the main window.
5. **Extract Data:** You can highlight specific lines of text or use `Ctrl+A` to select all text for copying into your forensic report.#
