# Simple bPlist Viewer

### 🔬 Project Status: Proof of Concept
This is a small utility created as a **Proof of Concept (PoC)** to explore parsing binary `.plist` files and rendering them in a Python-based GUI. 

The current version is a "quick and dirty" data dump designed to verify that:
1. Binary Apple property lists can be read reliably with `plistlib`.
2. Data can be formatted and displayed in a clean, readable hierarchy in PySide6.
3. Standalone Windows executables can be built automatically via GitHub Actions.

**Note:** This is a test app. The UI is minimal and focuses on functional data output rather than advanced features or high-performance rendering of massive files.
