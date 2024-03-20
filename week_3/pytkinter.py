#Python User Interface
import tkinter as tk

#Function to be executed when the button is clicked
def button_click():
    label.config(text="Button Click Me")

#Create tkinter window 
window=tk.Tk()
window.title("Tkinter window")

#label widget
label=tk.Label(window, text="Welcome to python tkinter")
label.pack()

#Create an entry widget
entry = tk.Entry(window)
entry.pack()

#create a button 
button= tk.Button(window, text="Download video", command="button_click")
button.pack()

#Run tkinter
window.mainloop()
#print("Just btw on pass")