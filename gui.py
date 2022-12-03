import PySimpleGUI as sg
import chatbotClasses as cb
def main():
    # Define the window's contents
    keys = ["-OP1-","-OP2-","-OP3-","-OP4-","-OP5-","-OP6-","-OP7-","-OP8-","-OP9-"]
    layout = [  [sg.Text(size=(70,1), key=keys[8])],     # Part 2 - The Layout
                [sg.Text(size=(70,1), key=keys[7])],
                [sg.Text(size=(70,1), key=keys[6])],
                [sg.Text(size=(70,1), key=keys[5])],
                [sg.Text(size=(70,1), key=keys[4])],
                [sg.Text(size=(70,1), key=keys[3])],
                [sg.Text(size=(70,1), key=keys[2])],
                [sg.Text(size=(70,1), key=keys[1])],
                [sg.Text(size=(70,1), key=keys[0])],
                [sg.Text("Your message: "), sg.Input(key = "-INPUT-",do_not_clear=False), sg.Button("Send"),sg.Button("Quit")]]
    # Create the window
    window = sg.Window("Chat.com", layout)      # Part 3 - Window Defintion

    # Display and interact with the Window
    while True:                                     # Part 4 - Event loop or Window.read call
        event, values = window.read()
        # Do something with the information gathered
        #if the window is closed or quit button clicked, exit event loop
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        #move each line up twice to create scrolling effect
        for i,line in enumerate(keys):
            window[keys[len(keys)-1-i]].update(window[keys[len(keys)-1-i-2]].get())
        #update bottom two rows with most recent user input and bot response
        op = cb.ReadInput.read(values["-INPUT-"]) 
        window[keys[0]].update(op) 
        window[keys[1]].update("You: {}".format(values["-INPUT-"])) 
    # Finish up by removing from the screen
    window.close()   

if __name__ == "__main__":
    main()             
    


