import PySimpleGUI as sg

# Define the layout for the main screen
layout_main_screen = [
    [sg.Text("Welcome to 'The Adventure Book'!", size=(30, 2), justification='center', font=("Comic Sans MS", 16))],
    [sg.Text("Once upon a time, in a faraway land...", size=(60, 5), justification='center', font=("Comic Sans MS", 14))],
    [sg.Text("You find yourself standing at a fork in the road. Which path will you choose?", size=(60, 3), justification='center', font=("Comic Sans MS", 12))],
    [sg.Button("Take the left path", key="-LEFT_PATH-", size=(20, 2), font=("Comic Sans MS", 12)), sg.Button("Take the right path", key="-RIGHT_PATH-", size=(20, 2), font=("Comic Sans MS", 12))]
]

# Define the layout for the left path
layout_left_path = [
    [sg.Text("You chose the left path.", size=(30, 2), justification='center', font=("Comic Sans MS", 16))],
    [sg.Text("As you walk along the winding trail, you stumble upon a hidden treasure chest.", size=(60, 5), justification='center', font=("Comic Sans MS", 14))],
    [sg.Text("What will you do?", size=(60, 3), justification='center', font=("Comic Sans MS", 12))],
    [sg.Button("Open the chest", key="-OPEN_CHEST-", size=(20, 2), font=("Comic Sans MS", 12)), sg.Button("Continue on the path", key="-CONTINUE_LEFT-", size=(20, 2), font=("Comic Sans MS", 12))]
]

# Define the layout for the right path
layout_right_path = [
    [sg.Text("You chose the right path.", size=(30, 2), justification='center', font=("Comic Sans MS", 16))],
    [sg.Text("The path leads you to a majestic waterfall cascading down into a crystal clear pool.", size=(60, 5), justification='center', font=("Comic Sans MS", 14))],
    [sg.Text("What will you do?", size=(60, 3), justification='center', font=("Comic Sans MS", 12))],
    [sg.Button("Swim in the pool", key="-SWIM_POOL-", size=(20, 2), font=("Comic Sans MS", 12)), sg.Button("Continue on the path", key="-CONTINUE_RIGHT-", size=(20, 2), font=("Comic Sans MS", 12))]
]

# Create the main window
window = sg.Window("The Adventure Book", layout_main_screen)

# Event loop
while True:
    event, _ = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "-LEFT_PATH-":
        window.close()
        window = sg.Window("The Adventure Book", layout_left_path)

    if event == "-RIGHT_PATH-":
        window.close()
        window = sg.Window("The Adventure Book", layout_right_path)

    if event == "-OPEN_CHEST-":
        sg.popup("You found a precious gem inside the chest!")

    if event == "-CONTINUE_LEFT-":
        sg.popup("You continue on the path, eager for new adventures!")

    if event == "-SWIM_POOL-":
        sg.popup("You enjoy a refreshing swim in the pool.")

    if event == "-CONTINUE_RIGHT-":
        sg.popup("You continue on the path, ready to explore further!")

# Close the window
window.close()
