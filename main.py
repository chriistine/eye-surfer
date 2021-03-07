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
    nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen']
    
    if (noun_word[0] == 'open') {
        credential_path = os.path.join(os.path.dirname(__file__), './','chromedriver.exe')
        driver = webdriver.Chrome(credential_path)
        driver.get('https://nationalpost.com/')
    }

    if (noun_word[0] == 'search') {
        driver.get('https://nationalpost.com/')
        title_ld = webnav.search_for_news(noun_word[1], driver)
        title_list = webnav.data_to_title_list(title_ld)
        count = 0
        for title in title_list:
            tts.textToSpeech(nums[count])
            tts.textToSpeech(title)
            count += 1
            sleep(1)
    }

    if (noun_word[0] == 'read') {
        index_news = nums.index(noun[1])
        article_ls = webnav.select_news(title_ld, index_news, driver)
        for string in article_ls:
            tts.textToSpeech(string)
    }

    if (noun_word[0] == 'close') {
        webnav.close_chrome(driver)
    }


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
