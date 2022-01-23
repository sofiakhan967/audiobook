#install pyttsx3
#install pypdf2
import pyttsx3
import PyPDF2
with open('sample.pdf','rb') as book:
    full_book=""
    reader= PyPDF2.PdfFileReader(book)

    audio_reader= pyttsx3.init()
    audio_reader.setProperty("rate",140)

    for page in range(reader.numPages):
        next_page=reader.getPage(page)
        content=next_page.extractText()
        full_book+=content
        #audio_reader.say(content) #first instance of reading a pdf
    audio_reader.save_to_file(content,"myaudiobook.mp3") #save pdf as a mp3 file 
    audio_reader.runAndWait()
