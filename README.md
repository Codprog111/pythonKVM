
# Monitor Input Switcher
python -m PyInstaller --onefile --windowed --icon=icon.ico monitor_switcher_tray_hotkey.py

This application allows you to toggle between HDMI and VGA monitor inputs using a system tray icon and a hotkey.

## Features
- Toggle inputs using `Ctrl + Shift + Alt`.
- Access the functionality via a system tray icon.
- Logging for debugging and tracking toggle events.

## Installation
### Prerequisites
- Python 3.x
- Dependencies from `requirements.txt`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/monitor_switcher.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python pythonKVM.py
   ```

### Building a Standalone Executable
Use PyInstaller to create a standalone `.exe`:
```bash
python -m PyInstaller --onefile --windowed --icon=icon.ico pythonKVM.py
```

## Requirements
- `pystray`
- `pillow`
- `keyboard`

Install them using:
```bash
pip install -r requirements.txt
```

## License
MIT License
