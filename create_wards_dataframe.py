from os import listdir
import torch
import cv2
import pandas as pd


def create_wards_dataframe(screenshot_directories):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')
    data = []

    for directory in screenshot_directories:
        screenshot_names = [x for x in listdir(f"ScreenshotsOfTheMap/{directory}")]

        for name in screenshot_names:
            image = cv2.imread(f"ScreenshotsOfTheMap/{directory}/{name}")[..., ::-1]
            result = model(image, size=640)

            detected_wards_for_image = result.pandas().xywhn[0]
            timer = name[-9] + name[-8] + ":" + name[-6] + name[-5]
            detected_wards_for_image["time"] = pd.to_datetime(timer, format='%M:%S')
            detected_wards_for_image["directory"] = directory
            data.append(detected_wards_for_image)

    return data
