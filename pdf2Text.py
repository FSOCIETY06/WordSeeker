"""
Need to search any data from a PDF.
Data present in the PDF is a combination of English, Telugu & Urdu languages.
The font used for Telugu is Shreelipi and for Urdu is Noori Nastaliq.
Format of Data present in PDF will be in .pdf format and some data will be in image format.
We need to search the data present in English, Telugu & Urdu languages which is present in Unicode
as well as in image format.
Sample data set has been uploaded.
"""

import time

import PIL.Image
import pdf2image
import pytesseract
from googletrans import Translator

PDF_PATH = ""
DPI = 200
OUTPUT_FOLDER = None
FIRST_PAGE = None
LAST_PAGE = None
FORMAT = 'jpg'
THREAD_COUNT = 1
USERPWD = None
USE_CROPBOX = False
STRICT = False

index = 0


def pdftopil(PDF_PATH):
    start_time = time.time()
    pil_images = pdf2image.convert_from_path(PDF_PATH, dpi=DPI, output_folder=OUTPUT_FOLDER, first_page=FIRST_PAGE,
                                             last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT, userpw=USERPWD,
                                             use_cropbox=USE_CROPBOX, strict=STRICT)
    print("Time taken for Image Generation: " + str(time.time() - start_time))
    return pil_images


def save_images(pil_images):
    index = 1
    for image in pil_images:
        image.save("C:\\Users\\Kingsmanvk\\PycharmProjects\\selfPRO\\sih\\pages\\page_" + str(index) + ".jpg")
        index += 1
    print("Number of pages :", index - 1)
    return index


def imageWork(PDF_PATH):
    pil_images = pdftopil(PDF_PATH)
    index = save_images(pil_images)
    return index


def textWork(index):
    start_time = time.time()

    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'
    TESSDATA_PREFIX = 'C:\\Program Files\\Tesseract-OCR'
    output = ""

    for i in range(1, index):
        output += pytesseract.image_to_string(
            PIL.Image.open(
                'C:\\Users\\Kingsmanvk\\PycharmProjects\\selfPRO\\sih\\pages\\page_' + str(i) + '.jpg').convert(
                "RGB"),
            lang='urd+tel+eng')
        output += "\n______________________________________________________________________\n"
    print("\nText retrieved :\n")
    print(output)
    print("Time taken for OCR Operation: " + str(time.time() - start_time))
    return output


def search(output, s):
    flag = 0
    # print(set(output.split()))
    # print(s.split())
    for i in s.split():
        if i in output.split():
            flag = 1
        else:
            flag = 0
    if flag:
        print("Found")
        return 1
    else:
        print("Not Found")
        return 0


def translate(s, dest):
    translator = Translator()
    l = translator.translate(s, dest=dest)
    # print(l)
    return l


def main():
    PDF_PATH = "C:\\Users\\Kingsmanvk\\PycharmProjects\\selfPRO\\sih\\demo.pdf"
    # PDF_PATH = input("Enter the address of input file:\n")  # C:\\Users\\Kingsmanvk\\PycharmProjects\\selfPRO\\sih\\demo.pdf
    index = imageWork(PDF_PATH)
    output = textWork(index)
    # print(output.split())
    n = 1
    while n:
        n = int(input("Enter 1 to have a search or 2 for translate operation else enter 0. "))
        if n == 1:
            s = input("Enter the word to search.")
            f = search(output, s)
        elif n == 2:
            s, l = input("Enter the the word to translate and the language to which you wish to translate it.").split()
            print(translate(s, l).text)
        else:
            print("Thank You.")


if __name__ == "__main__":
    main()

