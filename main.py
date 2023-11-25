import PySimpleGUI as sg

WIDTH, HEIGHT = 800, 800
custom_font = ('Helvetica', 20)

def main():
    # Define the layout of the window
    layout = [
        [sg.Button('Click me', font = custom_font, size = (20, 10))],
    ]

    # Create the window with a specific size
    window = sg.Window('Bigger PySimpleGUI App', layout, size = (WIDTH, HEIGHT))

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
