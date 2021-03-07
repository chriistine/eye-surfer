import tkinter as tk
from tkinter import filedialog, Text
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import WebNavigation as webnav
import os

root = tk.Tk()
apps = []

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename= filedialog.askopenfilename(initialdir="/", title="Select File", 
                                        filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    credential_path = os.path.join(os.path.dirname(__file__), './','chromedriver.exe')
    driver = webdriver.Chrome(credential_path)

    driver.get('https://nationalpost.com/')
    webnav.searchForNews("education", driver)


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relw=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')