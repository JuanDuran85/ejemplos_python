'''
Using langdetect library

To detect the language of the text. 
langdetect supports 55 languages out of the box by ISO 639-1 codes
'''

from langdetect import detect

text_in: str = input("Enter any text in any language: ")
print(f"The language is: {detect(text_in)}")
