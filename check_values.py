import os


def check_values(gui):

    if check_directories(gui) is False:
        return False

    inputs = [
        [gui.lineEdit_2.text(), "Map X"],
        [gui.lineEdit_3.text(), "Map Y"],
        [gui.lineEdit_4.text(), "Map W"],
        [gui.lineEdit_5.text(), "Map H"],
        [gui.lineEdit_6.text(), "Timer X"],
        [gui.lineEdit_7.text(), "Timer Y"],
        [gui.lineEdit_8.text(), "Timer W"],
        [gui.lineEdit_9.text(), "Timer H"],
        [gui.lineEdit_10.text(), "First Width Between Timer Digits"],
        [gui.lineEdit_11.text(), "Second Width Between Timer Digits"],
        [gui.lineEdit_12.text(), "Third Width Between Timer Digits"],
    ]

    for x in inputs:
        field_value = x[0]
        field_name = x[1]
        is_success = test_int_field(gui, field_value, field_name)
        if is_success is False:
            return False

    is_success = test_confidence_threshold(gui, gui.lineEdit.text())
    if is_success is False:
        return False

    is_success = test_team_name(gui, gui.lineEdit_13.text())
    if is_success is False:
        return False

    return True


def test_int_field(gui, field_value, field_name):
    try:
        field_value = int(field_value)
    except:
        gui.show_value_error(f"Cannot convert given value to integer in {field_name}.")
        return False

    if field_value < 0:
        gui.show_value_error(f"Value cannot be less than 0 in {field_name}.")
        return False

    return True


def test_confidence_threshold(gui, field_value):
    try:
        field_value = float(field_value)
    except:
        gui.show_value_error(f"Cannot convert given type to float in confidence threshold.")
        return False

    if field_value <= 0 or field_value >= 1:
        gui.show_value_error(f"Confidence threshold value must be between 0 and 1.")
        return False

    return True


def test_team_name(gui, field_value):
    if len(field_value) == 0:
        gui.show_value_error(f"No team name.")
        return False
    if len(field_value) > 20:
        gui.show_value_error(f"Team name cannot be longer than 20.")
        return False

    return True


def check_directories(gui):
    if not os.path.isdir('IncorrectScreenshots'):
        gui.show_value_error(f"Missing directory: IcorrectScreenshots")
        return False
    if not os.path.isdir('Maps'):
        gui.show_value_error(f"Missing directory: Maps")
        return False
    if not os.path.isdir('Screenshots'):
        gui.show_value_error(f"Missing directory: Screenshots")
        return False
    if not os.path.isdir('ScreenshotsOfTheMap'):
        gui.show_value_error(f"Missing directory: ScreenshotsOfTheMap")
        return False
    if not os.path.isdir('Templates'):
        gui.show_value_error(f"Missing directory: Templates")
        return False

    screenshot_directories = [x for x in os.listdir("Screenshots") if os.path.isdir(os.path.join("Screenshots", x))]
    if len(screenshot_directories) == 0:
        gui.show_value_error(f"No game direcotries in: Screenshots")
        return False

    return True
