#pip install gTTS
# apt-get install mpg321


text = str(input("Enter The Text : "))
from gtts import gTTS
import os
# Language in which you want to convert
language = 'en'
myobj = gTTS(text=text, lang=language, slow=False)
myobj.save("temp_speech.mp3")
os.system("mpg321 temp_speech.mp3")
os.remove("temp_speech.mp3")
