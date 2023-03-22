import os


def check_values_to_save(gui):

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

    is_success = test_data_name(gui, gui.lineEdit_14.text())
    if is_success is False:
        return False

    is_success = test_combo_box_value(gui)
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


def test_data_name(gui, field_value):
    if len(field_value) == 0:
        gui.show_value_error(f"No data name.")
        return False
    if len(field_value) > 20:
        gui.show_value_error(f"Data name cannot be longer than 20.")
        return False

    all_data_names = [gui.comboBox.itemText(i) for i in range(gui.comboBox.count())]

    for data_name in all_data_names:
        if data_name == field_value:
            gui.show_value_error(f"This name is already used!")
            return False

    return True


def test_combo_box_value(gui):
    if gui.comboBox.currentText() != "Custom":
        gui.show_value_error("It is not custom data.")
        return False

    return True
