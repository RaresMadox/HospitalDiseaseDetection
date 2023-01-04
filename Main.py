import tkinter as tk
import objects as obj

# tk.Frame.grid()
# tk.Label(tk.Frame, text="Meniu Principal", font="Times 20 italic bold").grid(column=0, row=0, padx=10,
#                                                                              pady=(10, 250))
# tk.Button(tk.Frame, text="Adauga Pacient", command=OpenNewWindows()).grid(column=0, row=1, padx=10, pady=10)
# tk.Button(tk.Frame, text="Identifica Boala", command=root.destroy).grid(column=0, row=2, padx=10, pady=10)
# tk.Button(tk.Frame, text="Fisa Medicala", command=root.destroy).grid(column=0, row=3, padx=10, pady=10)
# tk.Button(tk.Frame, text="Quit", command=root.destroy).grid(column=0, row=4, padx=10, pady=10)
# tk.Frame.place(anchor="c", relx=.5, rely=.5)
if __name__ == "__main__":
    app = obj.App()

    app.mainloop()