import logging
import os
import signal
import sys
import threading

from PIL import Image, ImageDraw
from pystray import Icon, Menu, MenuItem

SRC_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from pipeline.pipeline_init import PipelineInit

POLL_INTERVAL_SECONDS = 5.0

TRAY_ICON_SIZE = 64
TRAY_ICON_COLOR = (30, 144, 255, 255)  # dodger blue
TRAY_ICON_BACKGROUND = (255, 255, 255, 0)

STOP_EVENT = threading.Event()


def create_tray_image():
    image = Image.new("RGBA", (TRAY_ICON_SIZE, TRAY_ICON_SIZE), TRAY_ICON_BACKGROUND)
    draw = ImageDraw.Draw(image)
    draw.ellipse(
        (8, 8, TRAY_ICON_SIZE - 8, TRAY_ICON_SIZE - 8),
        fill=TRAY_ICON_COLOR,
    )
    return image


def run_pipeline_loop():
    pipeline = PipelineInit()

    while not STOP_EVENT.is_set():
        pipeline.run()
        STOP_EVENT.wait(POLL_INTERVAL_SECONDS)


def request_stop(icon, item):
    STOP_EVENT.set()
    icon.stop()


def main():
    signal.signal(signal.SIGTERM, lambda signum, frame: (STOP_EVENT.set(), sys.exit(0)))

    icon = Icon(
        name="pipeline_tray",
        icon=create_tray_image(),
        title="Pipeline: running",
        menu=Menu(
            MenuItem("Stop pipeline", request_stop),
        ),
    )

    get_systray_manager = getattr(icon, "_get_systray_manager", None)
    if get_systray_manager is not None and get_systray_manager() is None:
        logging.warning(
            "No system tray manager is available; running the pipeline without tray controls."
        )
        del icon
        run_pipeline_loop()
        return

    pipeline_thread = threading.Thread(target=run_pipeline_loop, daemon=True)
    pipeline_thread.start()
    icon.run()


if __name__ == "__main__":
    main()
