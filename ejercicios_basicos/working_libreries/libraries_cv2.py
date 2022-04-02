"""_summary_

    Working with pywhatkit and cv2 libraries to create an image 

"""

import pywhatkit as kit
import cv2

try:
    kit.text_to_handwriting("I can code in Python", save_to="hand_written.png")
    img = cv2.imread("hand_written.png")
    img = cv2.resize(img, (600, 600))
    cv2.imshow("Text to Hand Written", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except Exception as e:
    print(f"Error in: {e}")