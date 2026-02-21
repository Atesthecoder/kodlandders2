import os
import tkinter
tke = tkinter.Tk()
tke.title("GAMESHOP")
tke.geometry(f"{400}x{200}")
def rtr():
    
    try: 
        os.system("winget install RiotGames.Valorant")
    except:
        os.system("winget install RiotGames.RiotClient")
        os.system("winget install RiotGames.Valorant")
        
button1 = tkinter.Button(tke, text=("VALORANT"),background="yellow", command=rtr)

button1.pack()
tke.mainloop()