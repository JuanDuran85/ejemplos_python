"""_summary_

Working with pywhatkit library

PyWhatKit is a Python library with various helpful features. It's easy-to-use and does not require you to do any additional setup. Currently, it is one of the most popular library for WhatsApp and YouTube automation. New updates are released frequently with new features and bug fixes.

"""

import pywhatkit as kit
from PIL import Image 

#-----------------------------------------------------------------------------------
# Text to Handwriting using pywhatkit and PIL
#-----------------------------------------------------------------------------------
def text_to_handwriting(text_in):
    kit.text_to_handwriting(text_in,save_to='img1.png') # type: ignore
    Image.open('img1.png')

text_to_handwriting("Escribiendo un nuevo texto")
#-----------------------------------------------------------------------------------