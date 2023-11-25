import PySimpleGUI as sg

WIDTH, HEIGHT = 800, 800
custom_font = ('Helvetica', 20)
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREY = (169, 169, 169)

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)

BLACK = rgb_to_hex(BLACK)
WHITE = rgb_to_hex(WHITE)
GREY = rgb_to_hex(GREY)

selected = False

def main():
    # Define the layout of the window
    layout = [
        [sg.Button('Add a Game', font=custom_font, size=(80, 2), button_color=(WHITE, GREY), key='add_game_button')],
    ]

    # Create the window with a specific size
    window = sg.Window('Game Library', layout, size=(WIDTH, HEIGHT), background_color=BLACK)

    # Initialize a flag to track the status of the second window
    second_window_open = False

    # Event loop
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'add_game_button':
            if not second_window_open:
                # Set the flag to indicate that the second window is open
                second_window_open = True

                # Update the label of the button to indicate the current state
                window['add_game_button'].update('Cancel Adding a Game')

                # Create a layout for the second window with an input for the directory
                layout_second = [
                    [sg.Text('Enter a directory:')],
                    [sg.InputText(key='directory'), sg.FileBrowse()],
                    [sg.Button('OK')]
                ]

                # Create the second window
                window_second = sg.Window('Second Window', layout_second, background_color=BLACK)

                # Event loop for the second window
                while True:
                    event_second, values_second = window_second.read()

                    if event_second == sg.WINDOW_CLOSED or event_second == 'OK':
                        break

                # Reset the flag when the second window is closed
                second_window_open = False

                # Update the label of the button to indicate the current state
                window['add_game_button'].update('Add a Game')

                if event_second == 'OK':  # Check if OK button was clicked
                    # Get the entered directory from the input field
                    selected_directory = values_second.get('directory', '')

                    # Do something with the selected directory (print it for now)
                    print(f'Selected directory: {selected_directory}')

                # Close the second window
                window_second.close()

    # Close the main window
    window.close()

    # Display a message in the console
    print('Button clicked!')

if __name__ == '__main__':
    main()
