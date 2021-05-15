# EyeSurfer
Voice interactive assistant for visually impaired people or for those who want easier experience surfing the web.

## Inspiration
With the COVID-19 pandemic, we have been more reliant on the internet. However, the internet isn’t all friendly to everyone — especially to the visually impared. There are over 285 million visually impared people around the world, and with their disability it is very hard to search on the internet. EyeSurfer aims to tackle that problem using voice activated searching, so that the visually impaired can surf through the internet, but with their voice.

## What it does
EyeSurfer allows users to use the internet, all with their voice. For example, the user can say the command “I want to see vaccine progress,” then EyeSurfer would get the key word (vaccine) and search that through a news website and read out the relevant titles. Due to the time constraints, we had to limit our search to news-related commands.

## How we built it
This application was built using python, and using the tkinter library for simple GUI display for user interaction. We used the Google Speech-to-text API to convert voice to text, and analyzed the text received using the Google Natural Languages API. Then the web automation/scraping is done through Selenium python scripts, which gets triggered based on the analyzed voice input from the user. Lastly, the results are returned to the user via Google's Text-to-Speech!

## Challenges we ran into
Designing the overall architecture of our project, and integrating the parts together. Figuring out how to deliver our service to users.

We were able to use the Google APIs to interact with the assistant, and we were able to use selenium to navigate through the website. The problem was, HOW to put the two and two together. There were several options: creating a chrome extension, a web application, or a GUI application. Thinking of the limited time frame and our skillset, we decided to use a GUI app to host our service to our users! Using the GUI app also made it MUCH easier for us to integrate our selenium script with our text to speech and speech to text scripts!

## What we learned
Definitely linking all the bits and pieces together. From the Google NLP API to Google Cloud API to finally Selenium, it was tough to bind all libraries into one project. Most of us only had scripting experience and the fact that we had to build some kind of full stack application was a big hurdle
