# 🍎 Simple bplist Viewer

A lightweight, "quick and dirty" proof-of-concept utility for forensics. This tool is designed to do one thing: rip keys and values out of an Apple binary plist (`.bplist`)—common in **Cellebrite Premium** full filesystem extractions.

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
git clone https://github.com/KlasNotes/simple-bplist-viewer.git
cd simple-bplist-viewer

```


* **If you do NOT have Git:** Download the **ZIP file** from the green "Code" button at the top of this page, extract it, and open your terminal inside that folder.

### 2. First-Time Run (The One-Liner)

Copy and paste the command for your OS to create a virtual environment, install dependencies, and launch the app:

**Windows (Command Prompt):**

```cmd
python -m venv venv && venv\Scripts\python -m pip install -r requirements.txt && venv\Scripts\python binary_plist.py

```

**Windows (PowerShell):**

```powershell
python -m venv venv ; venv\Scripts\python -m pip install -r requirements.txt ; venv\Scripts\python binary_plist.py

```

**Linux / macOS (Terminal):**

```bash
python3 -m venv venv && ./venv/bin/pip install -r requirements.txt && ./venv/bin/python3 binary_plist.py

```

---

## 📖 How to Use

### 🚀 Launching After Setup

The next time you need to use the tool, you don't need the "One-Liner." Just run these from the project folder:

* **Windows:** `venv\Scripts\python binary_plist.py`
* **macOS/Linux:** `source venv/bin/activate && python3 binary_plist.py`

### 🔍 Analysis Steps

1. **Open bplist:** Click the button in the main interface.
2. **Select your file:** Browse to the Apple `.plist` or `.bplist` file (often found in `\private\var\mobile\...` in full filesystem extractions).
3. **View Results:** The app "rips" the binary data into readable lines of text.
4. **Extract Data:** Highlight specific lines or use `Ctrl+A` to copy data directly into your forensic report or timeline.

### Official Apple View (Reference for Comparison)

Use this image to see how the source data is structured in a professional IDE compared to the simplified text output of this tool:

<img width="912" height="525" alt="image" src="https://github.com/user-attachments/assets/3d4f3fb0-ecb9-4c97-afa9-2a3b6f1727f7" />
