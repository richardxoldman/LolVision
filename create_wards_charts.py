import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.dates import DateFormatter, SecondLocator
import datetime as dt
import pandas as pd
import cv2


def create_wards_charts(df, team_name: str, lane: str, side: str, generate_with_map_legend: bool):
    lane = lane.lower()
    side = side.lower()
    # lane options: top, mid, bot
    # side options: red, blue
    plt.figure(num=1, figsize=(11, 10), dpi=80)
    df = df[(df["name"] == "normal_" + side) | (df["name"] == "control_" + side)]
    number_of_games = df["directory"].nunique()
    if number_of_games == 1:
        # to prevent ZeroDivisionError
        number_of_games = 2

    for timestamp in (pd.to_datetime("1900-01-01 00:00:00") + dt.timedelta(0, n) for n in range(720)):
        df_for_timestamp = df[df["time"] == timestamp]
        for area_number in range(1, 10):
            local_df = df_for_timestamp[df_for_timestamp["area"] == lane+str(area_number)]
            df_length = len(local_df)

            if df_length > 0:
                local_df = local_df.groupby("directory", group_keys=False).apply(lambda x: x.sample(1))
                df_length = len(local_df)
                first_row = local_df.iloc[0]
                area = int(first_row["area"][-1])
                start_time = first_row["time"]
                end_time = first_row["time"] + dt.timedelta(0, 5)
                color = (1, 0.8 - ((df_length-1) / (number_of_games-1))**(3/2) * 0.8, 0)
                plt.hlines(area, start_time, end_time, color, lw=6, zorder=df_length*2)

    ax = plt.gca()
    ax.xaxis_date()
    ax.xaxis.set_major_formatter(DateFormatter('%M:%S'))
    ax.xaxis.set_major_locator(SecondLocator(interval=60))

    plt.yticks([1, 2, 3, 4, 5, 6, 7, 8, 9], fontsize=13)
    plt.xticks(fontsize=13)

    plt.grid(zorder=1)
    plt.ylim(0, 10)
    plt.xlim(pd.to_datetime("1900-01-01 00:00:00"), pd.to_datetime("1900-01-01 00:12:00"))

    plt.title(f"{team_name}\n{lane.upper()} LANE AREAS - {side.upper()} SIDE WARDS", fontsize=24, pad=20)
    plt.ylabel("Area", fontsize=18, labelpad=20)
    plt.xlabel("Time", fontsize=18, labelpad=20)
    add_legend(number_of_games)

    graph_file_name = f"{team_name}_{lane}_{side}.png"
    plt.savefig(graph_file_name)
    if generate_with_map_legend is True:
        save_graph_with_map_legend(graph_file_name, lane)

    plt.clf()


def add_legend(number_of_games):
    patches = []
    for x in range(number_of_games):
        color = (1, 0.8 - (x / (number_of_games-1))**(3/2) * 0.8, 0)
        patches.append(mpatches.Patch(color=color, label=str(x+1)))

    plt.legend(handles=patches, loc="upper left", fontsize="large", title="Number of wards")


def save_graph_with_map_legend(graph_file_name, lane):
    graph = cv2.imread(graph_file_name)
    map_legend = cv2.imread(f"Maps/sr_{lane}.jpg")

    graph_with_map = cv2.hconcat([map_legend, graph])
    os.remove(graph_file_name)
    cv2.imwrite(graph_file_name, graph_with_map)
