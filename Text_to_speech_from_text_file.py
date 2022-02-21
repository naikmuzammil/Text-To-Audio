import pyttsx3
text_speech = pyttsx3.init()
fo=open("C:\\Users\\naikm\\Desktop\\major project\\Text_to_Speech\\file2.txt","r")
ip=fo.read()
fo.close()
text_speech.setProperty("rate",120)
text_speech.say(ip)
text_speech.runAndWait()