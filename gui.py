import PySimpleGUI as sg
import chatbotClasses as cb
from PIL import Image
import io
def main():
    # Define the window's contents
    keys = ["-OP1-","-OP2-","-OP3-","-OP4-","-OP5-","-OP6-","-OP7-","-OP8-","-OP9-"]
    imgkeys = ["-IM1-","-IM2-","-IM3-","-IM4-","-IM5-","-IM6-","-IM7-","-IM8-","-IM9-"]
    imgsources = ["","","","","","","","",""]

    layout = [  [sg.Text(size=(70,1), key=keys[8])],     # Part 2 - The Layout
                [sg.Image(key=imgkeys[8])],
                [sg.Text(size=(70,1), key=keys[7])],
                [sg.Image(key=imgkeys[7])],
                [sg.Text(size=(70,1), key=keys[6])],
                [sg.Image(key=imgkeys[6])],
                [sg.Text(size=(70,1), key=keys[5])],
                [sg.Image(key=imgkeys[5])],
                [sg.Text(size=(70,1), key=keys[4])],
                [sg.Image(key=imgkeys[4])],
                [sg.Text(size=(70,1), key=keys[3])],
                [sg.Image(key=imgkeys[3])],
                [sg.Text(size=(70,1), key=keys[2])],
                [sg.Image(key=imgkeys[2])],
                [sg.Text(size=(70,1), key=keys[1])],
                [sg.Image(key=imgkeys[1])],
                [sg.Text(size=(70,1), key=keys[0])],
                [sg.Image(key=imgkeys[0])],
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

        for i,line in enumerate(imgkeys):
            try:
                if len(keys)-1-i-2 != -1:
                    image = Image.open(imgsources[len(keys)-1-i-2])
                    image.thumbnail((200, 200))
                    bio = io.BytesIO()
                    image.save(bio, format="PNG")
                    window[imgkeys[len(keys)-1-i]].update(data=bio.getvalue())
                    imgsources[len(keys)-1-i] = imgsources[len(keys)-1-i-2]
                    #print(f"img {len(keys)-1-i} set to img {len(keys)-1-i-2}")
                    
                    window[imgkeys[len(keys)-1-i-2]].update(source="")
                    imgsources[len(keys)-1-i-2] = ""
                    #print(f"img {len(keys)-1-i-2} set to empty")

                    #print(f"img sources: {imgsources}")
            except AttributeError:
                window[imgkeys[len(keys)-1-i]].update(source="")
                imgsources[len(keys)-1-i] = imgsources[len(keys)-1-i-2]

                
            
        #update bottom two rows with most recent user input and bot response
        op, associatedImg = cb.ReadInput.read(values["-INPUT-"]) 
        window[keys[0]].update(op) 
        if associatedImg != "":
            image = Image.open(str(associatedImg))
            image.thumbnail((200, 200))
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            window[imgkeys[0]].update(data=bio.getvalue()) 
            imgsources[0] = associatedImg
            #print("***pinged API")
        window[keys[1]].update("You: {}".format(values["-INPUT-"]))
        
    # Finish up by removing from the screen
    window.close()   

if __name__ == "__main__":
    main()             
    


