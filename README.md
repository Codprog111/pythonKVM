
# Monitor Input Switcher

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
   python monitor_switcher_tray_hotkey.py
   ```

### Building a Standalone Executable
Use PyInstaller to create a standalone `.exe`:
```bash
pyinstaller --onefile --windowed monitor_switcher_tray_hotkey.py
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
