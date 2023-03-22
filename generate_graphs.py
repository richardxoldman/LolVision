import os
import pandas as pd
from PyQt5.QtCore import QObject, pyqtSignal

from rename_screenshots import rename_screenshots
from cut_map_screenshots import cut_map_screenshots
from create_wards_dataframe import create_wards_dataframe
from get_wards_areas import get_wards_areas
from create_wards_charts import create_wards_charts
from remove_map_screenshots import remove_map_screenshots


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def __init__(self, data, parent=None):
        QObject.__init__(self, parent)
        self.data = data

    def generate_graphs(self):
        timer_data = self.data["timer_data"]
        map_data = self.data["map_data"]
        widths = self.data["widths_between_timer_digits"]
        widths_between_digits = [widths["first"], widths["second"], widths["third"]]

        screenshot_directories = [x for x in os.listdir("Screenshots") if os.path.isdir(os.path.join("Screenshots", x))]
        self.progress.emit(0)

        rename_screenshots(screenshot_directories, timer_data, widths_between_digits)
        self.progress.emit(1)

        remove_map_screenshots([x for x in os.listdir("ScreenshotsOfTheMap")])
        cut_map_screenshots(screenshot_directories, map_data)
        self.progress.emit(2)

        data_to_create_df = create_wards_dataframe(screenshot_directories)
        if len(data_to_create_df) > 0:
            df = pd.concat(data_to_create_df, ignore_index=True)

            df = df[df["confidence"] > self.data["confidence"]]
            df = get_wards_areas(df)
            self.progress.emit(3)
            create_wards_charts(df, self.data["team_name"], "top", self.data["side"], self.data["generate_with_map"])
            create_wards_charts(df, self.data["team_name"], "mid", self.data["side"], self.data["generate_with_map"])
            create_wards_charts(df, self.data["team_name"], "bot", self.data["side"], self.data["generate_with_map"])

            remove_map_screenshots(screenshot_directories)
            self.finished.emit()
        else:
            self.progress.emit(3)
            self.finished.emit()
