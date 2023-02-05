import googletrans 
from googletrans import Translator
#print(googletrans.LANGUAGES)
t = Translator()
a = t.translate("Xin chào", src = "vi", dest = "en")
b = a.text