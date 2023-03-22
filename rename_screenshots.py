import cv2 as cv
import os
import os.path
from os import listdir
from pathlib import Path


def rename_screenshots(screenshot_directories, timer_data, widths_between_digits):
    digit_templates = [cv.imread(f"Templates/TimerDigits/{x}") for x in listdir("Templates/TimerDigits/")]

    timer_x = timer_data["timer_x"]
    timer_y = timer_data["timer_y"]
    timer_w = timer_data["timer_w"]
    timer_h = timer_data["timer_h"]

    changeable_timer_x = timer_x
    for directory in screenshot_directories:
        screenshot_names = [x for x in listdir(f"Screenshots/{directory}")]

        for screenshot_name in screenshot_names:
            image = cv.imread(f"Screenshots/{directory}/{screenshot_name}")
            first_digit_img = image[timer_y:timer_y + timer_h, changeable_timer_x:changeable_timer_x + timer_w]
            first_digit = find_matching_digit(first_digit_img, digit_templates)

            changeable_timer_x += widths_between_digits[0]
            second_digit_img = image[timer_y:timer_y + timer_h, changeable_timer_x:changeable_timer_x + timer_w]
            second_digit = find_matching_digit(second_digit_img, digit_templates)

            changeable_timer_x += widths_between_digits[1]
            third_digit_img = image[timer_y:timer_y + timer_h, changeable_timer_x:changeable_timer_x + timer_w]
            third_digit = find_matching_digit(third_digit_img, digit_templates)

            changeable_timer_x += widths_between_digits[2]
            fourth_digit_img = image[timer_y:timer_y + timer_h, changeable_timer_x:changeable_timer_x + timer_w]
            fourth_digit = find_matching_digit(fourth_digit_img, digit_templates)

            if first_digit == "none" or second_digit == "none" or third_digit == "none" or fourth_digit == "none":
                create_directory_if_does_not_exist(directory)
                os.replace(f"Screenshots/{directory}/{screenshot_name}", f"IncorrectScreenshots/{directory}/{screenshot_name}")
            else:
                timer = get_timer_from_digits(first_digit, second_digit, third_digit, fourth_digit, 0)
                try:
                    os.rename(f"Screenshots/{directory}/{screenshot_name}", f"Screenshots/{directory}/screen{timer}.png")
                except:
                    os.replace(f"Screenshots/{directory}/{screenshot_name}", f"IncorrectScreenshots/{directory}/{screenshot_name}")

            changeable_timer_x = timer_x


def find_matching_digit(digit, digit_templates):
    the_best_result = 0.5
    the_best_matching_digit = "none"

    for template_index in range(10):
        result = cv.matchTemplate(digit, digit_templates[template_index], cv.TM_CCOEFF_NORMED)
        if result > the_best_result:
            the_best_result = result
            the_best_matching_digit = str(template_index)

    return the_best_matching_digit


def get_timer_from_digits(first, second, third, fourth, factor):
    # first, second, third, fourth are digits of the timer mm:ss, factor is number of seconds to add to the timer
    number_of_seconds = int(first) * 600 + int(second) * 60 + int(third) * 10 + int(fourth)
    number_of_seconds += factor
    number_of_minutes = number_of_seconds // 60
    number_of_seconds_without_minutes = number_of_seconds - number_of_minutes * 60

    new_first = str(number_of_minutes // 10)
    new_second = str(int(number_of_minutes - int(new_first) * 10))

    new_third = str(number_of_seconds_without_minutes // 10)
    new_fourth = str(int(number_of_seconds_without_minutes - int(new_third) * 10))

    return new_first + new_second + "_" + new_third + new_fourth


def create_directory_if_does_not_exist(directory):
    Path(f"IncorrectScreenshots/{directory}").mkdir(parents=True, exist_ok=True)
