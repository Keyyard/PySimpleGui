import PySimpleGUI as sg
import math

# Define the layout for the main window
layout = [
    [sg.Text("Nhập phương trình:")],
    [sg.Input(size=(30, 1), key="-EQUATION-")],
    [sg.Radio("Số bước:", "MODE", key="-STEPS_RADIO-", default=True),
     sg.Input(size=(10, 1), key="-STEPS-", disabled=True)],
    [sg.Radio("Epsilon:", "MODE", key="-EPSILON_RADIO-"),
     sg.Input(size=(10, 1), key="-EPSILON-", disabled=False)],
    [sg.Button("Tính", key="-CALCULATE-")],
    [sg.Output(size=(50, 10))]
]

# Create the main window
window = sg.Window("Phương pháp dây", layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "-CALCULATE-":
        equation = values["-EQUATION-"]
        steps = int(values["-STEPS-"]) if values["-STEPS_RADIO-"] else None
        epsilon = float(values["-EPSILON-"]) if values["-EPSILON_RADIO-"] else None

        # Tính nghiệm bằng phương pháp dây
        result = ""

        if steps is not None:
            x_prev = 0
            x = 1

            for i in range(steps):
                fx = eval(equation)
                dfx = eval(equation.replace("x", "(x + 0.001)"))  # Đạo hàm gần đúng
                x_next = x - (fx / dfx)

                if abs(x_next - x_prev) < 0.0001:
                    result = "Nghiệm gần đúng x = " + str(x_next) + " với Số bước = " + str(steps)
                    break

                x_prev = x
                x = x_next

        elif epsilon is not None:
            result = "Nghiệm không tìm thấy với Epsilon = " + str(epsilon)
            x_prev = 0
            x = 1

            for i in range(50):  # Số bước mặc định
                fx = eval(equation)
                dfx = eval(equation.replace("x", "(x + 0.001)"))  # Đạo hàm gần đúng
                x_next = x - (fx / dfx)

                if abs(x_next - x_prev) < epsilon:
                    result = "Nghiệm gần đúng x = " + str(x_next) + " với Epsilon = " + str(epsilon)
                    break

                x_prev = x
                x = x_next

        print(result)

# Close the window
window.close()
