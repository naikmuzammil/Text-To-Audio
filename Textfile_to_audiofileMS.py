from gtts import gTTS
with open("C:\\Users\\naikm\\Desktop\\sample.txt", encoding = "utf-8") as file:
    file = file.read()
speak = gTTS(file,lang='en')
speak.save("audio_new11.mp4")
    