import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import mss
import datetime
import locale
import pyautogui
locale.setlocale(locale.LC_ALL, "pt_BR")
sct = mss.mss()

while True:
    scr = sct.grab({
        'left': 40,
        'top': 0,
        'width': 1920,
        'height': 1080
    })

    time = sct.grab({
        'left': 1652,
        'top': 841,
        'width': 250,
        'height': 25
    })

    timeImg = np.array(time)
    timeImg = cv2.cvtColor(timeImg, cv2.COLOR_BGR2GRAY)
    timeImg = cv2.threshold(timeImg, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    timeImg = np.array(timeImg)

    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    temp_dateTime = pytesseract.image_to_string(timeImg, lang='eng', config='--psm 7')
    if isinstance(temp_dateTime, str):
        try:
            temp_dateTime = temp_dateTime.replace("♀", "").strip()
            dateTime = datetime.datetime.strptime(temp_dateTime.lstrip(), '%a %m %b %Y %H:%M')
        except Exception as e:
            pass
    img = np.array(scr)
    output = cv2.resize(img, (1280, 720))

    cv2.imshow('output', timeImg)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        running = False
        break
    