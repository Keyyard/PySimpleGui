import numpy as np
import matplotlib.pyplot as plt
import math
import PySimpleGUI as sg
epsi = 0.0000001
layout = [
    [sg.Text("Nhap a: ")],
    [sg.Input(key="a")],
    [sg.Text("Nhap b:")],
    [sg.Input(key="b")],
    [sg.Button("RUN",key="run")],
    [sg.Text(key="result")]
]
window = sg.Window("PPT: Day Cung",layout)
while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "run":
        a = float(values["a"])
        b = float(values["b"])
        if (a * b > 0):
            result = "Khong co nghiem trong khoang nay"
            window["result"].update(result)
        x = a - (b - a) * a / (b - a)
        if (x * a < 0):
            while abs(x - b) > epsi:
                b = x
                x = a - (b - a) * a / (b - a)
        else:
            while abs(x - a) > epsi:
                a = x
                x = a - (b - a) * a / (b - a)
        x = a - (b - a) * a / (b - a)
        result = "x = " + str(x)
        window["result"].update(result)