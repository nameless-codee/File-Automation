# File Automation (Python)

A lightweight Python utility to automatically organize downloaded files into appropriate folders and optionally enhance images using Pillow (PIL).

This project includes two scripts:
- `file_automation.py`: Moves files from your `Downloads` folder to categorized destinations (PDF, Text, Word, Pictures, Videos, Music). Prompts to enhance images on the fly.
- `image_editor.py`: Batch enhances all images in a target folder (contrast + sharpen).

---

## Features
- **Auto-sort files by type** from `Downloads` to pre-defined folders.
- **On-demand image enhancement** in `file_automation.py` via a yes/no prompt.
- **Batch image enhancement** in `image_editor.py` with no prompts.
- **Robust error handling** for permissions and missing files.
- **Windows-friendly paths** using raw strings for reliability.

---

## How It Works
- `file_automation.py`:
  - Scans `user_path` for files.
  - Uses `os` and `shutil.move()` to relocate files based on extension:
    - PDFs → `pdf`
    - Text → `txt`
    - Word (`.doc`, `.docx`) → `word`
    - Images (`.jpg`, `.jpeg`, `.png`) → `img`
    - Videos (`.mp4`, `.mkv`) → `video`
    - Music (`.mp3`, `.wav`) → `music`
  - When an image is moved, it asks whether to enhance it. If yes, Pillow:
    - Converts to `RGBA` (safer for filters)
    - Increases contrast by 1.5x
    - Applies a sharpen filter
    - Saves back to the same file path (overwrites)

- `image_editor.py`:
  - Iterates over all images in the `img` folder and applies the same enhancement steps (contrast + sharpen) without prompts.

---

## Project Structure
```
File Automation/
├─ file_automation.py
├─ image_editor.py
└─ README.md
```

---

## Prerequisites
- Python 3.8+
- pip
- Windows OS (paths in code are Windows-specific; works on other OSes with path changes)

### Install dependencies
```powershell
# Optional: create and activate a virtual environment (Windows PowerShell)
python -m venv .venv
. .venv\Scripts\Activate.ps1

# Install Pillow
pip install pillow
```

---

## Configuration
Both scripts currently use hardcoded Windows paths. Update them to match your system.

- In `file_automation.py`:
  - `user_path`: source folder to scan (e.g., your `Downloads`)
  - `pdf`, `txt`, `word`, `img`, `video`, `music`: destination folders

Example (edit these lines):
```python
user_path = r"C:\Users\YOUR_USER\Downloads"
pdf = r"C:\Users\YOUR_USER\OneDrive\Documents\PDF"
txt = r"C:\Users\YOUR_USER\OneDrive\Documents\Text"
word = r"C:\Users\YOUR_USER\OneDrive\Documents\Word"
img = r"C:\Users\YOUR_USER\Pictures"
video = r"C:\Users\YOUR_USER\Videos"
music = r"C:\Users\YOUR_USER\Music"
```

- In `image_editor.py`:
  - `img`: folder containing images to enhance

Example:
```python
img = r"C:\Users\YOUR_USER\Pictures"
```

Tip: Ensure destination folders exist. `shutil.move()` will not create missing directories by default.

---

## Usage

### 1) Auto-organize downloads and optionally enhance images
```powershell
python file_automation.py
```
- The script will print moves like:
  - `C:\Users\...\Downloads\file.pdf → C:\Users\...\Documents\PDF\file.pdf`
- If an image is encountered, you will see a prompt:
  - `Do you want to edit <filename>? (yes/no)`
  - Type `yes` to enhance or `no` to skip.

### 2) Batch enhance all images in a folder
```powershell
python image_editor.py
```
- Enhances all `.jpg`, `.jpeg`, `.png` in the configured `img` folder.
- Overwrites files in place.

---

## Supported Extensions
- PDFs: `.pdf`
- Text: `.txt`
- Word: `.doc`, `.docx`
- Images: `.jpg`, `.jpeg`, `.png`
- Videos: `.mp4`, `.mkv`
- Music: `.mp3`, `.wav`

Add more by extending the `if file.endswith(...)` checks in `file_automation.py`.

---

## Notes & Warnings
- Image edits **overwrite** the original file. Back up if necessary.
- Close files before running to avoid `PermissionError`.
- Paths are **user-specific**; update them before running.
- Designed for Windows pathing. For macOS/Linux, adapt the paths and separators.

---

## Troubleshooting
- **Permission denied**: Ensure the file isn’t open in another program. Try running the shell as Administrator if needed.
- **File not found**: Confirm the source and destination paths exist and are correct.
- **Pillow not found**: Run `pip install pillow` in the active environment.
- **Unicode/path issues**: Keep the `r"..."` raw string prefix for Windows paths.

---

## Roadmap / Ideas
- Config file (e.g., `config.json`) to avoid hardcoded paths
- Create missing directories automatically
- Logging to file with timestamps
- Scheduler integration (Task Scheduler / cron)
- Cross-platform path handling
- Dry-run mode for previewing moves

---

## License
This project is currently unlicensed. Add your preferred license (e.g., MIT) if you plan to distribute.

---

## Credits
- Built with Python standard libraries: `os`, `shutil`
- Image processing by [Pillow](https://python-pillow.org/)
