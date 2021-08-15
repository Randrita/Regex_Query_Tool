#sentence = str(input("Say......: "))
file = open("language.pdf", 'rb')
reader = PdfFileReader(file)

num_pages = reader.numPages
for p in range(num_pages):
    page = reader.getPage(p)
    text = page.extractText()

from googletrans import Translator
URL_COM = 'translate.google.com'
URL_LV = 'translate.google.lv'
LANG = "bn"
translator = Translator(service_urls=['translate.googleapis.com'])
translation = translator.translate(text, dest=LANG)

print(translation)
