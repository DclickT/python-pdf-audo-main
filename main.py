import pyttsx3,PyPDF2

#insert name of your pdf 
reader = PyPDF2.PdfReader(open('test.pdf', 'rb'))
speaker = pyttsx3.init()

voices = speaker.getProperty('voices')
for voice in voices:
    print(voice.id)

# Set the voice to the Microsoft Zira voice
speaker.setProperty('voice', 'TTS_MS_EN-US_ZIRA_11.0')

# Set the rate of the speech to a slower value
speaker.setProperty('rate', 100)

for page_num in range(len(reader.pages)):
    text = reader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
    
#name mp3 file whatever you would like
speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()

speaker.stop()
