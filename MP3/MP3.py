import tkinter as tk
from tkinter.filedialog import askopenfilename
from pygame import mixer
root= tk.Tk()

mixer.init()
canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def play ():
	filename = askopenfilename()
	mixer.music.load(filename)
	mixer.music.set_volume(0.7)
   	#img = PhotoImage(file="image/ev_devs.jpg")
    #canvas1.create_window(150, 200, window=label1)
    #canvas1.create_image(20, 20, anchor=NW, image = img)
    mixer.music.play()
    
button1 = tk.Button(text='Play',command=play, bg='brown',fg='white')

canvas1.create_window(150, 150, window=button1)

root.mainloop()
