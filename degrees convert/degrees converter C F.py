# Degrees Converter Program
import PySimpleGUI as gui

units = ["C","F"]

layout = [
    [gui.Text("Degrees Converter")],
    [gui.Input(key="input"),gui.Combo(default_value=units[0],values=units,key="unit")],
    [gui.Button("Convert")],
    [gui.Text("Result:"),gui.Text("",key="result")]
]

window = gui.Window("Degrees Converter",layout)

while True:
    event,values = window.read()
    if event == gui.WIN_CLOSED:
        break
    if event == "Convert":
        if values["unit"] == "C":
            result = float(values["input"])*9/5+32
        else:
            result = (float(values["input"])-32)*5/9
        window["result"].update(round(result,2))