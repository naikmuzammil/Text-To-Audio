from gtts import gTTS
import os
myText = input("Enter the text that to be converted into audio: ")
language = 'en'
output = gTTS(text = myText, lang = language, slow = False)
output.save("output.mp3")
os.system("start output.mp3")