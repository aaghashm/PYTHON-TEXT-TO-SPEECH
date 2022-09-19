def text_to_speech(): 
  from gtts import gTTS
  import os
  text = input('enter your text : ')
  language = input('language --> en (or) fr')
  myText = f"'{text}'"
  output = gTTS (text = myText , lang = language , slow = False)
  output.save ("output.mp3")
  os.system ("start output.mp3")
  
text_to_speech()
