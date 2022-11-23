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

class GameScreen:

    def __init__():
        
        window = Tk()
        window.geometry("1920x1080")
        window.title("Ice Age")
        playerImage = PhotoImage(file='assets/Player.png')
        player = Label(window,image=playerImage)
        player.place(x=0,y=0)
    def move_up(event):
        print(player.winfo_x())
        #player.place(x=player.winfo_x(),y=player.winfo_y()-2)        
    window.bind("<w>",move_up)
    logo = PhotoImage(file='assets/logo.png')
    window.iconphoto(True,logo)

    window.mainloop()
        
    def draw():
        pass
        

    def __init__(self):
        pass

        
        

