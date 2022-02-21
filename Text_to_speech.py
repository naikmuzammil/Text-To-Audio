#pip install pyttsx3
import pyttsx3
text_speech = pyttsx3.init()
answer = input(str("Enter the text that you want to listen in audio :"))
text_speech.setProperty("rate",120)
text_speech.setProperty("rate",120)
text_speech.setProperty("volume",1)
text_speech.say(answer)
text_speech.runAndWait()