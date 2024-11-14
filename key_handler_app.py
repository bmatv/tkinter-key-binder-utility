import tkinter as tk

# function to run on pressing any key, outputs the key's tk name
# that could be specified in the self.bind in place of "<Key>"

class root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tk key bind tester")
        self.geometry("200x200")
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)

        self.myframe = tk.Frame(self,background='grey')
        self.myframe.grid(row=0,column=0,padx=10,pady=10,sticky='nswe')
        self.myframe.columnconfigure(0,weight=1)
        self.myframe.rowconfigure(0,weight=1)

        self.label = tk.Label(self.myframe,text='Press any key',bg='grey')
        self.label.grid(row=0,column=0,sticky='ew',padx=10,pady=10)
        # Binding ENTER key to function
        self.bind("<Key>", self.key_handler_function)

    def key_handler_function(self, event):
        print(f"You pressed '{event.keysym}' key on the keyboard")
        self.label.configure(text=f"'{event.keysym}'")

# run the application
app = root()
app.mainloop()
