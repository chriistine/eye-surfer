import tkinter as tk
from tkinter import filedialog, Text
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import WebNavigation as webnav
import speechToText as stt
import textToSpeech as tts
import os

root = tk.Tk()
apps = []


def callback(event):
    print("You pressed Enter")
    stt.toAudioFile()
    string_words = stt.speechToText()
    noun_word = stt.extractKeywords(string_words)
    print(noun_word)
    credential_path = os.path.join(os.path.dirname(__file__), './','chromedriver.exe')
    driver = webdriver.Chrome(credential_path)
    driver.get('https://nationalpost.com/')
    title_ld = webnav.searchForNews(noun_word[1], driver)
    article_ls = webnav.select_news(title_ld, 0, driver)
    split_art = webnav.split_article(article_ls)
    for string in split_art:
        tts.textToSpeech(string)





root.bind('<Return>', callback)

canvas = tk.Canvas(root, height=700, width=700, bg="black")
canvas.pack()

# frame = tk.Frame(root, bg="white")
# frame.place(relw=0.8, relheight=0.8, relx=0.1, rely=0.1)

# openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
# openFile.pack()
# runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
# runApps.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')