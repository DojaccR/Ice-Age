from tkinter import *

class GUI:
    
    def __init__(self):
        window = Tk()
        window.geometry("1920x1080")
        window.title("Ice Age")

        logo = PhotoImage(file='assets/logo.png')
        window.iconphoto(True,logo)
    
        window.mainloop()

    def toMainScreen():
        mainScreen = MainSCreen
        self.destroy()
            
        pass

    def toGameSaveScreen():
        pass

    def toGameCreationScreen():
        pass

    def toGameScreen():
        pass

class MainScreen(GUI):
    pass

class GameScreen(GUI):
    window = Tk()
    window.geometry("1920x1080")
    window.title("Ice Age")

    logo = PhotoImage(file='assets/logo.png')
    window.iconphoto(True,logo)

    def move_up(event):
        label.place(x=label.winfo_x(),y=label.winfo_y()-2)
        
    def draw():
        pass

    def initPlayer():
        window.bind("<w>",move_up)
        player = PhooImage(file='asstes/Player.png')
        label = Label(window,image=player)
        label.place(x=0,y=0)
        
    def __init__(self):
        pass

        
        

