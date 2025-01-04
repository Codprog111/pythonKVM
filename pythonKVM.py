import subprocess
import time
import logging
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw
import keyboard
import threading
from pathlib import Path

# Commands for monitor inputs
COMMAND_HDMI1 = r'"C:\Program Files (x86)\ClickMonitorDDC\ClickMonitorDDC_7_2.exe" s HDMI1'
COMMAND_VGA = r'"C:\Program Files (x86)\ClickMonitorDDC\ClickMonitorDDC_7_2.exe" s VGA'

# Cooldown period (to prevent rapid toggling)
COOLDOWN = 2
last_toggle_time = 0
current_input = "HDMI"  # Assume HDMI is active initially. Change to "VGA" if needed.

# Setup logging
logging.basicConfig(
    filename="monitor_switcher.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def toggle_input(icon):
    """Toggle the monitor input between HDMI and VGA."""
    global current_input, last_toggle_time

    current_time = time.time()
    if current_time - last_toggle_time < COOLDOWN:
        logging.info(
            f"Cooldown active. Please wait {COOLDOWN - (current_time - last_toggle_time):.1f} seconds."
        )
        return

    if current_input == "HDMI":
        subprocess.run(COMMAND_VGA, shell=True)
        current_input = "VGA"
    else:
        subprocess.run(COMMAND_HDMI1, shell=True)
        current_input = "HDMI"

    last_toggle_time = current_time
    logging.info(f"Switched to {current_input}")
    icon.title = f"Current Connection: {current_input}"  # Update tray tooltip


def on_quit(icon, item):
    """Quit the application."""
    logging.info("Exiting Monitor Switcher.")
    icon.stop()


def hotkey_listener(icon):
    """Listen for the hotkey in a separate thread."""
    HOTKEY_TOGGLE = "ctrl+shift+alt"
    logging.info(f"Hotkey {HOTKEY_TOGGLE} registered for toggling inputs.")
    keyboard.add_hotkey(HOTKEY_TOGGLE, lambda: toggle_input(icon))
    keyboard.wait()  # Keep this thread alive for hotkey detection


def main():
    # Path to the icon file
    icon_path = Path("icon.ico")
    if not icon_path.exists():
        logging.warning("Icon file 'icon.ico' not found. Using default image.")
        icon_image = create_default_image()
    else:
        icon_image = Image.open(icon_path)

    # Create the system tray menu
    menu = Menu(
        MenuItem("Toggle Input", lambda icon, item: toggle_input(icon)),
        MenuItem("Quit", on_quit),
    )

    # Create the system tray icon
    icon = Icon("Monitor Switcher", icon_image, menu=menu)
    icon.title = f"Current Connection: {current_input}"  # Initial tooltip

    # Start the hotkey listener in a separate thread
    hotkey_thread = threading.Thread(target=lambda: hotkey_listener(icon), daemon=True)
    hotkey_thread.start()

    logging.info("Monitor Switcher started in the system tray.")
    icon.run()


def create_default_image():
    """Create a default image for the system tray icon."""
    width = 64
    height = 64
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    draw.ellipse((8, 8, width - 8, height - 8), fill="black")
    return image


if __name__ == "__main__":
    main()
