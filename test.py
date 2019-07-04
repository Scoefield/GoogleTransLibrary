# coding:utf-8

from google_trans import Translator

# from googletrans import Translator
# translator = Translator(service_urls=['translate.google.cn'])
translator = Translator()
# source = "This is my book.Do you know?"
# text = translator.translate(source, src='zh-cn', dest='en').text
text = translator.translate("This is my book.Do you know?", src='en', dest='zh-cn').text

# print translator.detect("你好").lang

print(text)