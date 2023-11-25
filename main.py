import PySimpleGUI as sg

WIDTH, HEIGHT = 800, 800
custom_font = ('Helvetica', 20)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (200, 200, 200)
GREY = (169, 169, 169)

def rgbToHex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)

BLACK = rgbToHex(BLACK)
BLUE = rgbToHex(BLUE)
WHITE = rgbToHex(WHITE)
GREY = rgbToHex(GREY)

def main():
    # Define the layout of the window
    layout = [
        [sg.Button('Add a Game', font = custom_font, size = (80, 2), button_color = (WHITE, GREY))],
    ]

    # Create the window with a specific size
    window = sg.Window('Game Library', layout, size = (WIDTH, HEIGHT), background_color = BLACK)

    # Event loop
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Add a Game':
            break

    # Close the window
    window.close()

    # Display a message in the console
    print('Button clicked!')

if __name__ == '__main__':
    main()
