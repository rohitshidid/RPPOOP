import tkinter as tk
root= tk.Tk()

label = tk.Label(root,bg="yellow",text = "This is the first label",width=100, height= 10)

label1 = tk.Label(root,bg="skyblue",text = "This is the second label",width = 100, height =10)
label.pack(padx = 12 , pady = 5 )
label1.pack(pady = 5)

root.mainloop()