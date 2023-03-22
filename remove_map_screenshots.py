import os
from os import listdir


def remove_map_screenshots(screenshot_directories):
    for directory in screenshot_directories:
        screenshot_names = [x for x in listdir(f"ScreenshotsOfTheMap/{directory}")]

        for screenshot_name in screenshot_names:
            os.remove(f"ScreenshotsOfTheMap/{directory}/{screenshot_name}")
        os.rmdir(f"ScreenshotsOfTheMap/{directory}/")
