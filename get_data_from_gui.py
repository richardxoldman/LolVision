def get_data_from_gui(gui):
    data = {
            "map_data": {
                "map_x": int(gui.lineEdit_2.text()),
                "map_y": int(gui.lineEdit_3.text()),
                "map_w": int(gui.lineEdit_4.text()),
                "map_h": int(gui.lineEdit_5.text())
            },
            "timer_data": {
                "timer_x": int(gui.lineEdit_6.text()),
                "timer_y": int(gui.lineEdit_7.text()),
                "timer_w": int(gui.lineEdit_8.text()),
                "timer_h": int(gui.lineEdit_9.text())
            },
            "widths_between_timer_digits": {
                "first": int(gui.lineEdit_10.text()),
                "second": int(gui.lineEdit_11.text()),
                "third": int(gui.lineEdit_12.text())
            },
            "confidence": float(gui.lineEdit.text()),
            "team_name": gui.lineEdit_13.text(),
            "side": gui.comboBox_2.currentText(),
            "generate_with_map": gui.checkBox.isChecked()
        }

    return data

