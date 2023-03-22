import cv2 as cv
import os.path
from os import listdir
from pathlib import Path


def cut_map_screenshots(screenshot_directories, map_data):
    map_x = map_data["map_x"]
    map_y = map_data["map_y"]
    map_w = map_data["map_w"]
    map_h = map_data["map_h"]

    for directory in screenshot_directories:
        screenshot_names = [x for x in listdir(f"Screenshots/{directory}")]
        create_directory_if_does_not_exist(directory)

        for screenshot_name in screenshot_names:
            image = cv.imread(f"Screenshots/{directory}/{screenshot_name}")
            map_image = image[map_y:map_y + map_h, map_x:map_x + map_w]

            if os.path.isfile(f"ScreenshotsOfTheMap/{directory}/map{screenshot_name[-9:]}") is False:
                cv.imwrite(f"ScreenshotsOfTheMap/{directory}/map{screenshot_name[-9:]}", map_image)


def create_directory_if_does_not_exist(directory):
    Path(f"ScreenshotsOfTheMap/{directory}").mkdir(parents=True, exist_ok=True)
