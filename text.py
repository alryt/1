import tkinter


def but_onoff(event, button):
    if button == "Игрок А":
        but["text"] = "Игрок Б"
    else:
        but["text"] = "Игрок А"


root = tkinter.Tk()
but = tkinter.Button(root, text="Игрок А", width=30, height=5, bg="grey50", fg="blue")
but.pack(side=tkinter.RIGHT)
but.bind("<Button-1>", lambda event: but_onoff(event, but["text"]))
root.mainloop()