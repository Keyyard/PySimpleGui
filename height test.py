import PySimpleGUI as gui

layout = [
    [gui.Text("Nhap chieu cao cua ban")],
    [gui.Input(key="input_value"),gui.Text("Cm"),gui.Button("OK",key="OK")],
    [gui.Text("Chieu cao cua ban la:"),gui.Text("",key="result"),gui.Text("Cm")]
]

window = gui.Window("Chieu cao cua ban",layout)

while True:
    event,values = window.read()
    if event == gui.WIN_CLOSED:
        break

    window["result"].update(values["input_value"])