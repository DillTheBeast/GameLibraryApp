import PySimpleGUI as sg

def main():
    # Define the layout of the window
    layout = [
        [sg.Button('Click me')],
    ]

    # Create the window
    window = sg.Window('Simple PySimpleGUI App', layout)

    # Event loop
    while True:
        event, values = window.read()

        # If the user closes the window or clicks the button, exit the loop
        if event == sg.WINDOW_CLOSED or event == 'Click me':
            break

    # Close the window
    window.close()

    # Display a message in the console
    print('Button clicked!')

if __name__ == '__main__':
    main()
